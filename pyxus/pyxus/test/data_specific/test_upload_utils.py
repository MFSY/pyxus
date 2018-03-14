#   Copyright 2018 HumanBrainProject
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from unittest import TestCase

from pyxus.client import NexusClient
from pyxus.test import env_setup
from pyxus.utils.data_upload_utils import DataUploadUtils
from pyxus.utils.schema_or_context_data import SchemaOrContextData


class TestLoader(TestCase):
    exampleSchema = {
        "@id": "https://nexus.humanbrainproject.org/v0/schemas/hbp/test/foo/v0.0.1",
        "@type": "owl:Ontology",
        "@context": {
            "schema": "http://schema.org/",
            "hbp": "https://nexus.humanbrainproject.org/v0/vocab/hbp/core/celloptimization/",
            "this": "https://nexus.humanbrainproject.org/v0/schemas/hbp/test/foo/v0.0.1/shape/",
            "sh": "http://www.w3.org/ns/shacl#",
            "owl": "http://www.w3.org/2002/07/owl#",
            "sex": "http://www.hbp.FIXME.org/hbp_sex_ontology/",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "data": "{{scheme}}://{{host}}/{{prefix}}/schemas/nexus/core/datadownload/v1.0.0/shape/",
            "shapes": {
                "@reverse": "rdfs:isDefinedBy",
                "@type": "@id"
            }
        },
        "shapes": [
            {
                "@id": "hbp:FooShape",
                "@type": "sh:NodeShape",
                "property": [
                    {
                        "path": "hbp:bar",
                        "name": "bar",
                        "description": "Hello FooBar",
                        "maxCount": 1,
                        "datatype": "xsd:string"
                    }
                ],
                "targetClass": "hbp:Foo"
            }
        ]
    }

    def setUp(self):
        env_setup.load_env()
        self.upload_utils = DataUploadUtils(NexusClient())

    def test_upload_schema(self):
        schema_data = SchemaOrContextData('hbp', 'test', 'foo','v0.0.1', self.exampleSchema )
        result = self.upload_utils._create_schema(data=schema_data, force_domain_creation=True, publish=True, update_if_already_exists=True)
        print result

    def test_load_entities(self):
        self.upload_utils.__resolve_entities("dsfsafas{{resolve /hbp/core/person/v0.0.8?q=Lisa}}dsfas{{resolve /hbp/core/foo?q=abc}}fas")

    def test_load_entities_with_filter(self):
        self.upload_utils.__resolve_entities("{{resolve /minds/ethics/authority/v0.0.1/?filter={\"filter\": {\"path\": \"http://schema.org/identifier\", \"value\": \"d5b9290a0b67727d4ba1ca6059dc31a6\", \"op\": \"eq\"}}}}")
