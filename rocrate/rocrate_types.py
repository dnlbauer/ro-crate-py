# Copyright 2019-2025 The University of Manchester, UK
# Copyright 2020-2025 Vlaams Instituut voor Biotechnologie (VIB), BE
# Copyright 2020-2025 Barcelona Supercomputing Center (BSC), ES
# Copyright 2020-2025 Center for Advanced Studies, Research and Development in Sardinia (CRS4), IT
# Copyright 2022-2025 École Polytechnique Fédérale de Lausanne, CH
# Copyright 2024-2025 Data Centre, SciLifeLab, SE
# Copyright 2024-2025 National Institute of Informatics (NII), JP
# Copyright 2025 Senckenberg Society for Nature Research (SGN), DE
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
import typing
from datetime import datetime
from os import PathLike
from typing import TypedDict, Union

if typing.TYPE_CHECKING:
    from rocrate.model import Entity

# Type alias for a dictionary that represents a reference to another Entity
JsonLDReference = TypedDict("JsonLDReference", {"@id": str})

_JsonLDPrimitiveProperty = Union[str, int, float, bool, datetime, JsonLDReference, "Entity"]
_JsonLDPropertyList = list[Union[str, int, float, bool, datetime, JsonLDReference, "Entity"]]

# Type alias for a JSON property
# RO-Crate metadata must be flattened. Therefore, we can restrict possible values to a few non-nested types:
# A property can be either a JSON-LD primitive, a reference to another entity, or a list of these.
JsonLDProperty = Union[
    _JsonLDPrimitiveProperty,
    _JsonLDPropertyList,
]

# Type alias for a dictionary that represents properties of a JSON-LD entity
JsonLDProperties = dict[str, JsonLDProperty]

# Type alias for a dictionary that represents a Json-LD object
JsonLD = TypedDict("JsonLD", {"@context": Union[str, list[str], dict], "@graph": list[JsonLDProperties]})  # type: ignore

# A type alias for a string that represents a path or a path
PathStr = Union[str, PathLike[str]]
