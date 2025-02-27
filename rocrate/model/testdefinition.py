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
from . import SoftwareApplication
from .file import File
from typing import Any


class TestDefinition(File):

    def _empty(self) -> dict[str, Any]:
        return {
            "@id": self.id,
            "@type": ['File', 'TestDefinition']
        }

    @property
    def _default_type(self) -> str:
        return "TestDefinition"

    @property
    def engineVersion(self) -> str:
        return self.get("engineVersion")  # type: ignore

    @engineVersion.setter
    def engineVersion(self, engineVersion: str) -> None:
        self["engineVersion"] = engineVersion

    @property
    def conformsTo(self) -> SoftwareApplication:
        return self.get("conformsTo")  # type: ignore

    @conformsTo.setter
    def conformsTo(self, conformsTo: SoftwareApplication) -> None:
        self["conformsTo"] = conformsTo

    engine = conformsTo
