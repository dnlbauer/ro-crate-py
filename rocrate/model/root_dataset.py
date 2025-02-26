#!/usr/bin/env python

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

from .dataset import Dataset
from ..rocrate_types import PathStr
from ..utils import iso_now
import typing
from typing import Optional

if typing.TYPE_CHECKING:
    from ..rocrate import ROCrate


class RootDataset(Dataset):

    def __init__(self, crate: "ROCrate", source: Optional[PathStr] = None, dest_path: Optional[PathStr] = None,
                 properties: Optional[dict] = None) -> None:
        if source is None and dest_path is None:
            dest_path = "./"
        super().__init__(
            crate,
            source=source,
            dest_path=dest_path,
            fetch_remote=False,
            validate_url=False,
            properties=properties
        )

    def _empty(self) -> dict[str, str]:
        val = {
            "@id": self.id,
            "@type": "Dataset",
            "datePublished": iso_now(),
        }
        return val
