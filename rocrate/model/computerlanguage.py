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
from typing import Optional

from .contextentity import ContextEntity
from ..rocrate_types import JsonLDProperties

if typing.TYPE_CHECKING:
    from ..rocrate import ROCrate


class ComputerLanguage(ContextEntity):

    def _empty(self) -> JsonLDProperties:
        return {
            "@id": self.id,
            "@type": 'ComputerLanguage'
        }

    @property
    def name(self) -> str:
        return self.get("name")  # type: ignore

    @name.setter
    def name(self, name: str) -> None:
        self["name"] = name

    @property
    def alternateName(self) -> str:
        return self.get("alternateName")  # type: ignore

    @alternateName.setter
    def alternateName(self, alternateName: str) -> None:
        self["alternateName"] = alternateName

    @property
    def identifier(self) -> str:
        return self.get("identifier")  # type: ignore

    @identifier.setter
    def identifier(self, identifier: str) -> None:
        self["identifier"] = identifier

    @property
    def url(self) -> str:
        return self.get("url")  # type: ignore

    @url.setter
    def url(self, url: str) -> None:
        self["url"] = url

    # Not listed as a property in "https://schema.org/ComputerLanguage"
    @property
    def version(self) -> str:
        return self.get("version")  # type: ignore

    @version.setter
    def version(self, version: str) -> None:
        self["version"] = version


# See https://w3id.org/workflowhub/workflow-ro-crate/1.0
# (note that it does not specify "version")


def cwl(crate: "ROCrate", version: Optional[str] = None) -> ComputerLanguage:
    id_ = "https://w3id.org/workflowhub/workflow-ro-crate#cwl"
    identifier = "https://w3id.org/cwl/"
    if version:
        identifier = f"{identifier}v{version.lstrip('v')}/"
    properties: JsonLDProperties = {
        "name": "Common Workflow Language",
        "alternateName": "CWL",
        "identifier": {
            "@id": identifier
        },
        "url": {
            "@id": "https://www.commonwl.org/"
        },
    }
    if version:
        properties["version"] = version
    return ComputerLanguage(crate, identifier=id_, properties=properties)


def galaxy(crate: "ROCrate", version: Optional[str] = None) -> ComputerLanguage:
    id_ = "https://w3id.org/workflowhub/workflow-ro-crate#galaxy"
    properties: JsonLDProperties = {
        "name": "Galaxy",
        "identifier": {
            "@id": "https://galaxyproject.org/"
        },
        "url": {
            "@id": "https://galaxyproject.org/"
        }
    }
    if version:
        properties["version"] = version
    return ComputerLanguage(crate, identifier=id_, properties=properties)


def knime(crate: "ROCrate", version: Optional[str] = None) -> ComputerLanguage:
    id_ = "https://w3id.org/workflowhub/workflow-ro-crate#knime"
    properties: JsonLDProperties = {
        "name": "KNIME",
        "identifier": {
            "@id": "https://www.knime.com/"
        },
        "url": {
            "@id": "https://www.knime.com/"
        }
    }
    if version:
        properties["version"] = version
    return ComputerLanguage(crate, identifier=id_, properties=properties)


def nextflow(crate: "ROCrate", version: Optional[str] = None) -> ComputerLanguage:
    id_ = "https://w3id.org/workflowhub/workflow-ro-crate#nextflow"
    properties: JsonLDProperties = {
        "name": "Nextflow",
        "identifier": {
            "@id": "https://www.nextflow.io/"
        },
        "url": {
            "@id": "https://www.nextflow.io/"
        }
    }
    if version:
        properties["version"] = version
    return ComputerLanguage(crate, identifier=id_, properties=properties)


def snakemake(crate: "ROCrate", version: Optional[str] = None) -> ComputerLanguage:
    id_ = "https://w3id.org/workflowhub/workflow-ro-crate#snakemake"
    properties: JsonLDProperties = {
        "name": "Snakemake",
        "identifier": {
            "@id": "https://doi.org/10.1093/bioinformatics/bts480"
        },
        "url": {
            "@id": "https://snakemake.readthedocs.io"
        }
    }
    if version:
        properties["version"] = version
    return ComputerLanguage(crate, identifier=id_, properties=properties)


def compss(crate: "ROCrate", version: Optional[str] = None) -> ComputerLanguage:
    properties: JsonLDProperties = {
        "name": "COMPSs Programming Model",
        "alternateName": "COMPSs",
        "url": "http://compss.bsc.es/",
        "citation": "https://doi.org/10.1007/s10723-013-9272-5"
    }
    if version:
        properties["version"] = version
    return ComputerLanguage(crate, identifier="#compss", properties=properties)


def autosubmit(crate: "ROCrate", version: Optional[str] = None) -> ComputerLanguage:
    properties: JsonLDProperties = {
        "name": "Autosubmit",
        "alternateName": "AS",
        "url": "https://autosubmit.readthedocs.io/",
        "citation": "https://doi.org/10.1109/HPCSim.2016.7568429"
    }
    if version:
        properties["version"] = version
    return ComputerLanguage(crate, identifier="#autosubmit", properties=properties)


LANG_MAP = {
    "cwl": cwl,
    "galaxy": galaxy,
    "knime": knime,
    "nextflow": nextflow,
    "snakemake": snakemake,
    "compss": compss,
    "autosubmit": autosubmit,
}


def get_lang(crate: "ROCrate", name: str, version: Optional[str] = None) -> ComputerLanguage:
    try:
        func = LANG_MAP[name.lower()]
    except KeyError:
        raise ValueError(f"Unknown language: {name}")
    return func(crate, version=version)
