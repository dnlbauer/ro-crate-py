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

from .contextentity import ContextEntity
from .creativework import CreativeWork
from ..rocrate_types import JsonLDProperties

if typing.TYPE_CHECKING:
    from ..rocrate import ROCrate


class SoftwareApplication(ContextEntity, CreativeWork):

    def _empty(self) -> JsonLDProperties:
        return {
            "@id": self.id,
            "@type": 'SoftwareApplication'
        }

    @property
    def name(self) -> str:
        return self.get("name")  # type: ignore

    @name.setter
    def name(self, name: str) -> None:
        self["name"] = name

    @property
    def url(self) -> str:
        return self.get("url")  # type: ignore

    @url.setter
    def url(self, url: str) -> None:
        self["url"] = url

    @property
    def version(self) -> str:
        return self.get("version")  # type: ignore

    @version.setter
    def version(self, version: str) -> None:
        self["version"] = version


PLANEMO_ID = "https://w3id.org/ro/terms/test#PlanemoEngine"


def planemo(crate: "ROCrate") -> SoftwareApplication:
    return SoftwareApplication(crate, identifier=PLANEMO_ID, properties={
        "name": "Planemo",
        "url": {
            "@id": "https://github.com/galaxyproject/planemo"
        }
    })


APP_MAP = {
    "planemo": planemo,
}


def get_app(crate: "ROCrate", name: str) -> SoftwareApplication:
    try:
        func = APP_MAP[name.lower()]
    except KeyError:
        raise ValueError(f"Unknown application: {name}")
    return func(crate)
