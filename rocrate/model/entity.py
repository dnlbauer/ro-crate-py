#!/usr/bin/env python

# Copyright 2019-2025 The University of Manchester, UK
# Copyright 2020-2025 Vlaams Instituut voor Biotechnologie (VIB), BE
# Copyright 2020-2025 Barcelona Supercomputing Center (BSC), ES
# Copyright 2020-2025 Center for Advanced Studies, Research and Development in Sardinia (CRS4), IT
# Copyright 2022-2025 École Polytechnique Fédérale de Lausanne, CH
# Copyright 2024-2025 Data Centre, SciLifeLab, SE
# Copyright 2024-2025 National Institute of Informatics (NII), JP
# Copyright 2025 Senckenberg Society for Nature Research (SGN), DE
# Copyright 2025 European Molecular Biology Laboratory (EMBL), Heidelberg, DE
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
import uuid
from collections.abc import MutableMapping
from datetime import datetime
from typing import Optional, Any, Iterator, TYPE_CHECKING

from dateutil.parser import isoparse

from .. import vocabs
from ..rocrate_types import JsonLDProperties

if TYPE_CHECKING:
    from ..rocrate import ROCrate


class Entity(MutableMapping):

    def __init__(self, crate: "ROCrate", identifier: Optional[Any] = None,
                 properties: Optional[JsonLDProperties] = None) -> None:
        self.crate = crate
        if identifier:
            self.__id = self.format_id(identifier)
        else:
            self.__id = f"#{uuid.uuid4()}"
        self._jsonld = self._empty()
        if properties:
            for name, value in properties.items():
                if name.startswith("@"):
                    self._jsonld[name] = value
                else:
                    self[name] = value

    @property
    def id(self) -> str:
        return self.__id

    # Format the given ID with rules appropriate for this type.
    # For example, Dataset (directory) data entities SHOULD end with /
    def format_id(self, identifier: Any) -> str:
        return str(identifier)

    def __repr__(self) -> str:
        return f"<{self.id} {self.type}>"

    def properties(self) -> JsonLDProperties:
        return self._jsonld

    def as_jsonld(self) -> JsonLDProperties:
        return self._jsonld

    @property
    def _default_type(self) -> str:
        clsName = self.__class__.__name__
        if clsName in vocabs.RO_CRATE["@context"]:
            return clsName
        return "Thing"

    def canonical_id(self) -> str:
        return self.crate.resolve_id(self.id)

    def __hash__(self) -> int:
        return hash(self.canonical_id())

    def _empty(self) -> JsonLDProperties:
        val: JsonLDProperties = {
            "@id": self.id,
            "@type": self._default_type
        }
        return val

    def __getitem__(self, key: str) -> Any:
        v = self._jsonld[key]
        if v is None or key.startswith("@"):
            return v
        values = v if isinstance(v, list) else [v]
        deref_values = []
        for entry in values:
            if isinstance(entry, dict):
                try:
                    id_ = entry["@id"]
                except KeyError:
                    raise ValueError(f"no @id in {entry}")
                else:
                    deref_values.append(self.crate.get(id_, id_))
            else:
                deref_values.append(entry)
        return deref_values if isinstance(v, list) else deref_values[0]

    def __setitem__(self, key: str, value: Any) -> None:
        if key.startswith("@"):
            raise KeyError(f"cannot set '{key}'")
        values = value if isinstance(value, list) else [value]
        for v in values:
            if isinstance(v, dict) and "@id" not in v:
                raise ValueError(f"no @id in {v}")
        ref_values = [{"@id": _.id} if isinstance(_, Entity) else _ for _ in values]
        self._jsonld[key] = ref_values if isinstance(value, list) else ref_values[0]

    def __delitem__(self, key: str) -> None:
        if key.startswith("@"):
            raise KeyError(f"cannot delete '{key}'")
        del self._jsonld[key]

    def popitem(self) -> tuple[str, Any]:
        raise NotImplementedError

    def clear(self) -> None:
        raise NotImplementedError

    def update(self, **kwargs) -> None:  # type: ignore
        raise NotImplementedError

    def __iter__(self) -> Iterator[str]:
        return iter(self._jsonld)

    def __len__(self) -> int:
        return len(self._jsonld)

    def __contains__(self, key: Any) -> bool:
        return key in self._jsonld

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented
        return self.id == other.id and self._jsonld == other._jsonld

    @property
    def type(self) -> str:
        return self._jsonld['@type']

    @property
    def datePublished(self) -> Optional[datetime]:
        d = self.get('datePublished')
        return d if not d else isoparse(d)

    @datePublished.setter
    def datePublished(self, value: datetime | str) -> None:
        try:
            value = value.isoformat()  # type: ignore
        except AttributeError:
            pass
        self['datePublished'] = value

    def delete(self) -> None:
        self.crate.delete(self)

    def append_to(self, key: str, value: Any, compact: bool = False) -> None:
        if key.startswith("@"):
            raise KeyError(f"cannot append to '{key}'")
        current_value = self._jsonld.setdefault(key, [])
        if not isinstance(current_value, list):
            current_value = self._jsonld[key] = [current_value]
        if not isinstance(value, list):
            value = [value]
        current_value.extend([{"@id": _.id} if isinstance(_, Entity) else _ for _ in value])
        if compact and len(current_value) == 1:
            self._jsonld[key] = current_value[0]
