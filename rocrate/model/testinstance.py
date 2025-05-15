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
import typing

from .contextentity import ContextEntity
from ..rocrate_types import JsonLDProperties

if typing.TYPE_CHECKING:
    from . import TestService


class TestInstance(ContextEntity):

    def _empty(self) -> JsonLDProperties:
        return {
            "@id": self.id,
            "@type": 'TestInstance'
        }

    @property
    def _default_type(self) -> str:
        return "TestInstance"

    @property
    def name(self) -> str:
        return self.get("name")  # type: ignore

    @name.setter
    def name(self, name: str) -> None:
        self["name"] = name

    @property
    def resource(self) -> str:
        return self.get("resource")  # type: ignore

    @resource.setter
    def resource(self, resource: str) -> None:
        self["resource"] = resource

    @property
    def runsOn(self) -> "TestService":
        return self.get("runsOn")  # type: ignore

    @runsOn.setter
    def runsOn(self, runsOn: "TestService") -> None:
        self["runsOn"] = runsOn

    @property
    def url(self) -> str:
        return self.get("url")  # type: ignore

    @url.setter
    def url(self, url: str) -> None:
        self["url"] = url

    service = runsOn
