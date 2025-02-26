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

import os
import typing
from pathlib import Path

from .data_entity import DataEntity
from ..rocrate_types import PathStr
from ..utils import is_url
from typing import Optional

if typing.TYPE_CHECKING:
    from ..rocrate import ROCrate


class FileOrDir(DataEntity):

    def __init__(self, crate: "ROCrate", source: Optional[PathStr] = None, dest_path: Optional[PathStr] = None,
                 fetch_remote: bool = False, validate_url: bool = False, properties: Optional[dict] = None,
                 record_size: bool = False) -> None:
        if properties is None:
            properties = {}
        self.fetch_remote = fetch_remote
        self.validate_url = validate_url
        self.record_size = record_size
        self.source = source
        if dest_path:
            dest_path = Path(dest_path)
            if dest_path.is_absolute():
                raise ValueError("if provided, dest_path must be relative")
            identifier = dest_path.as_posix()
        else:
            if not isinstance(source, (str, Path)):
                raise ValueError("dest_path must be provided if source is not a path or URI")
            if is_url(str(source)):
                identifier = os.path.basename(source) if fetch_remote else source
            else:
                identifier = os.path.basename(str(source).rstrip("/"))
        super().__init__(crate, identifier, properties)
