# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vdp/pipeline/v1beta/connector_definition.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.vdp/pipeline/v1beta/connector_definition.proto\x12\x13vdp.pipeline.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x93\x02\n\rConnectorSpec\x12T\n\x16resource_specification\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x04\xe2\x41\x01\x02R\x15resourceSpecification\x12V\n\x17\x63omponent_specification\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructB\x04\xe2\x41\x01\x02R\x16\x63omponentSpecification\x12T\n\x16openapi_specifications\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructB\x04\xe2\x41\x01\x02R\x15openapiSpecifications\"\xc3\x05\n\x13\x43onnectorDefinition\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\x16\n\x03uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x03uid\x12\x14\n\x02id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x05R\x02id\x12\x1a\n\x05title\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03R\x05title\x12\x31\n\x11\x64ocumentation_url\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\x10\x64ocumentationUrl\x12\x18\n\x04icon\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03R\x04icon\x12<\n\x04spec\x18\x07 \x01(\x0b\x32\".vdp.pipeline.v1beta.ConnectorSpecB\x04\xe2\x41\x01\x03R\x04spec\x12<\n\x04type\x18\x08 \x01(\x0e\x32\".vdp.pipeline.v1beta.ConnectorTypeB\x04\xe2\x41\x01\x03R\x04type\x12\"\n\ttombstone\x18\t \x01(\x08\x42\x04\xe2\x41\x01\x03R\ttombstone\x12\x1c\n\x06public\x18\n \x01(\x08\x42\x04\xe2\x41\x01\x03R\x06public\x12\x1c\n\x06\x63ustom\x18\x0b \x01(\x08\x42\x04\xe2\x41\x01\x03R\x06\x63ustom\x12\x1f\n\x08icon_url\x18\x0c \x01(\tB\x04\xe2\x41\x01\x03R\x07iconUrl\x12\x1c\n\x06vendor\x18\r \x01(\tB\x04\xe2\x41\x01\x03R\x06vendor\x12J\n\x11vendor_attributes\x18\x0e \x01(\x0b\x32\x17.google.protobuf.StructB\x04\xe2\x41\x01\x03R\x10vendorAttributes\";\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\x0e\n\nVIEW_BASIC\x10\x01\x12\r\n\tVIEW_FULL\x10\x02:W\xea\x41T\n$api.instill.tech/ConnectorDefinition\x12,connector-definitions/{connector-definition}\"\x95\x02\n\x1fListConnectorDefinitionsRequest\x12&\n\tpage_size\x18\x01 \x01(\x05\x42\x04\xe2\x41\x01\x01H\x00R\x08pageSize\x88\x01\x01\x12(\n\npage_token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01H\x01R\tpageToken\x88\x01\x01\x12L\n\x04view\x18\x03 \x01(\x0e\x32-.vdp.pipeline.v1beta.ConnectorDefinition.ViewB\x04\xe2\x41\x01\x01H\x02R\x04view\x88\x01\x01\x12!\n\x06\x66ilter\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01H\x03R\x06\x66ilter\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\x07\n\x05_viewB\t\n\x07_filter\"\xc8\x01\n ListConnectorDefinitionsResponse\x12]\n\x15\x63onnector_definitions\x18\x01 \x03(\x0b\x32(.vdp.pipeline.v1beta.ConnectorDefinitionR\x14\x63onnectorDefinitions\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12\x1d\n\ntotal_size\x18\x03 \x01(\x05R\ttotalSize\"\xdb\x01\n\x1dGetConnectorDefinitionRequest\x12\x63\n\x04name\x18\x01 \x01(\tBO\x92\x41\x1f\xca>\x1c\xfa\x02\x19\x63onnector_definition.name\xe2\x41\x01\x02\xfa\x41&\n$api.instill.tech/ConnectorDefinitionR\x04name\x12L\n\x04view\x18\x02 \x01(\x0e\x32-.vdp.pipeline.v1beta.ConnectorDefinition.ViewB\x04\xe2\x41\x01\x01H\x00R\x04view\x88\x01\x01\x42\x07\n\x05_view\"}\n\x1eGetConnectorDefinitionResponse\x12[\n\x14\x63onnector_definition\x18\x01 \x01(\x0b\x32(.vdp.pipeline.v1beta.ConnectorDefinitionR\x13\x63onnectorDefinition\"\xa2\x01\n%LookUpConnectorDefinitionAdminRequest\x12\"\n\tpermalink\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\tpermalink\x12L\n\x04view\x18\x02 \x01(\x0e\x32-.vdp.pipeline.v1beta.ConnectorDefinition.ViewB\x04\xe2\x41\x01\x01H\x00R\x04view\x88\x01\x01\x42\x07\n\x05_view\"\x85\x01\n&LookUpConnectorDefinitionAdminResponse\x12[\n\x14\x63onnector_definition\x18\x01 \x01(\x0b\x32(.vdp.pipeline.v1beta.ConnectorDefinitionR\x13\x63onnectorDefinition*\xd6\x01\n\rConnectorType\x12\x1e\n\x1a\x43ONNECTOR_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43ONNECTOR_TYPE_SOURCE\x10\x01\x12\x1e\n\x1a\x43ONNECTOR_TYPE_DESTINATION\x10\x02\x12\x15\n\x11\x43ONNECTOR_TYPE_AI\x10\x03\x12\x1d\n\x19\x43ONNECTOR_TYPE_BLOCKCHAIN\x10\x04\x12\x17\n\x13\x43ONNECTOR_TYPE_DATA\x10\x05\x12\x1b\n\x17\x43ONNECTOR_TYPE_OPERATOR\x10\x06\x42\xe7\x01\n\x17\x63om.vdp.pipeline.v1betaB\x18\x43onnectorDefinitionProtoP\x01ZDgithub.com/instill-ai/protogen-go/vdp/pipeline/v1beta;pipelinev1beta\xa2\x02\x03VPX\xaa\x02\x13Vdp.Pipeline.V1beta\xca\x02\x13Vdp\\Pipeline\\V1beta\xe2\x02\x1fVdp\\Pipeline\\V1beta\\GPBMetadata\xea\x02\x15Vdp::Pipeline::V1betab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vdp.pipeline.v1beta.connector_definition_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.vdp.pipeline.v1betaB\030ConnectorDefinitionProtoP\001ZDgithub.com/instill-ai/protogen-go/vdp/pipeline/v1beta;pipelinev1beta\242\002\003VPX\252\002\023Vdp.Pipeline.V1beta\312\002\023Vdp\\Pipeline\\V1beta\342\002\037Vdp\\Pipeline\\V1beta\\GPBMetadata\352\002\025Vdp::Pipeline::V1beta'
  _CONNECTORSPEC.fields_by_name['resource_specification']._options = None
  _CONNECTORSPEC.fields_by_name['resource_specification']._serialized_options = b'\342A\001\002'
  _CONNECTORSPEC.fields_by_name['component_specification']._options = None
  _CONNECTORSPEC.fields_by_name['component_specification']._serialized_options = b'\342A\001\002'
  _CONNECTORSPEC.fields_by_name['openapi_specifications']._options = None
  _CONNECTORSPEC.fields_by_name['openapi_specifications']._serialized_options = b'\342A\001\002'
  _CONNECTORDEFINITION.fields_by_name['name']._options = None
  _CONNECTORDEFINITION.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['uid']._options = None
  _CONNECTORDEFINITION.fields_by_name['uid']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['id']._options = None
  _CONNECTORDEFINITION.fields_by_name['id']._serialized_options = b'\342A\001\005'
  _CONNECTORDEFINITION.fields_by_name['title']._options = None
  _CONNECTORDEFINITION.fields_by_name['title']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['documentation_url']._options = None
  _CONNECTORDEFINITION.fields_by_name['documentation_url']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['icon']._options = None
  _CONNECTORDEFINITION.fields_by_name['icon']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['spec']._options = None
  _CONNECTORDEFINITION.fields_by_name['spec']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['type']._options = None
  _CONNECTORDEFINITION.fields_by_name['type']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['tombstone']._options = None
  _CONNECTORDEFINITION.fields_by_name['tombstone']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['public']._options = None
  _CONNECTORDEFINITION.fields_by_name['public']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['custom']._options = None
  _CONNECTORDEFINITION.fields_by_name['custom']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['icon_url']._options = None
  _CONNECTORDEFINITION.fields_by_name['icon_url']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['vendor']._options = None
  _CONNECTORDEFINITION.fields_by_name['vendor']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION.fields_by_name['vendor_attributes']._options = None
  _CONNECTORDEFINITION.fields_by_name['vendor_attributes']._serialized_options = b'\342A\001\003'
  _CONNECTORDEFINITION._options = None
  _CONNECTORDEFINITION._serialized_options = b'\352AT\n$api.instill.tech/ConnectorDefinition\022,connector-definitions/{connector-definition}'
  _LISTCONNECTORDEFINITIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTCONNECTORDEFINITIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTCONNECTORDEFINITIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTCONNECTORDEFINITIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTCONNECTORDEFINITIONSREQUEST.fields_by_name['view']._options = None
  _LISTCONNECTORDEFINITIONSREQUEST.fields_by_name['view']._serialized_options = b'\342A\001\001'
  _LISTCONNECTORDEFINITIONSREQUEST.fields_by_name['filter']._options = None
  _LISTCONNECTORDEFINITIONSREQUEST.fields_by_name['filter']._serialized_options = b'\342A\001\001'
  _GETCONNECTORDEFINITIONREQUEST.fields_by_name['name']._options = None
  _GETCONNECTORDEFINITIONREQUEST.fields_by_name['name']._serialized_options = b'\222A\037\312>\034\372\002\031connector_definition.name\342A\001\002\372A&\n$api.instill.tech/ConnectorDefinition'
  _GETCONNECTORDEFINITIONREQUEST.fields_by_name['view']._options = None
  _GETCONNECTORDEFINITIONREQUEST.fields_by_name['view']._serialized_options = b'\342A\001\001'
  _LOOKUPCONNECTORDEFINITIONADMINREQUEST.fields_by_name['permalink']._options = None
  _LOOKUPCONNECTORDEFINITIONADMINREQUEST.fields_by_name['permalink']._serialized_options = b'\342A\001\002'
  _LOOKUPCONNECTORDEFINITIONADMINREQUEST.fields_by_name['view']._options = None
  _LOOKUPCONNECTORDEFINITIONADMINREQUEST.fields_by_name['view']._serialized_options = b'\342A\001\001'
  _globals['_CONNECTORTYPE']._serialized_start=2331
  _globals['_CONNECTORTYPE']._serialized_end=2545
  _globals['_CONNECTORSPEC']._serialized_start=210
  _globals['_CONNECTORSPEC']._serialized_end=485
  _globals['_CONNECTORDEFINITION']._serialized_start=488
  _globals['_CONNECTORDEFINITION']._serialized_end=1195
  _globals['_CONNECTORDEFINITION_VIEW']._serialized_start=1047
  _globals['_CONNECTORDEFINITION_VIEW']._serialized_end=1106
  _globals['_LISTCONNECTORDEFINITIONSREQUEST']._serialized_start=1198
  _globals['_LISTCONNECTORDEFINITIONSREQUEST']._serialized_end=1475
  _globals['_LISTCONNECTORDEFINITIONSRESPONSE']._serialized_start=1478
  _globals['_LISTCONNECTORDEFINITIONSRESPONSE']._serialized_end=1678
  _globals['_GETCONNECTORDEFINITIONREQUEST']._serialized_start=1681
  _globals['_GETCONNECTORDEFINITIONREQUEST']._serialized_end=1900
  _globals['_GETCONNECTORDEFINITIONRESPONSE']._serialized_start=1902
  _globals['_GETCONNECTORDEFINITIONRESPONSE']._serialized_end=2027
  _globals['_LOOKUPCONNECTORDEFINITIONADMINREQUEST']._serialized_start=2030
  _globals['_LOOKUPCONNECTORDEFINITIONADMINREQUEST']._serialized_end=2192
  _globals['_LOOKUPCONNECTORDEFINITIONADMINRESPONSE']._serialized_start=2195
  _globals['_LOOKUPCONNECTORDEFINITIONADMINRESPONSE']._serialized_end=2328
# @@protoc_insertion_point(module_scope)