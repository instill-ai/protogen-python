# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model/model/v1alpha/model_definition.proto
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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*model/model/v1alpha/model_definition.proto\x12\x13model.model.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x80\x04\n\x0fModelDefinition\x12\x17\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x04name\x12\x15\n\x03uid\x18\x02 \x01(\tB\x03\xe0\x41\x03R\x03uid\x12\x13\n\x02id\x18\x03 \x01(\tB\x03\xe0\x41\x03R\x02id\x12\x19\n\x05title\x18\x04 \x01(\tB\x03\xe0\x41\x03R\x05title\x12\x30\n\x11\x64ocumentation_url\x18\x05 \x01(\tB\x03\xe0\x41\x03R\x10\x64ocumentationUrl\x12\x17\n\x04icon\x18\x06 \x01(\tB\x03\xe0\x41\x03R\x04icon\x12K\n\rrelease_stage\x18\x07 \x01(\x0e\x32!.model.model.v1alpha.ReleaseStageB\x03\xe0\x41\x03R\x0creleaseStage\x12;\n\nmodel_spec\x18\x08 \x01(\x0b\x32\x17.google.protobuf.StructB\x03\xe0\x41\x03R\tmodelSpec\x12@\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\ncreateTime\x12@\n\x0bupdate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\nupdateTime:4\xea\x41\x31\x12\x16model-definitions/{id}\x12\x17model-definitions/{uid}\"\xcc\x01\n\x1bListModelDefinitionsRequest\x12%\n\tpage_size\x18\x01 \x01(\x05\x42\x03\xe0\x41\x01H\x00R\x08pageSize\x88\x01\x01\x12\'\n\npage_token\x18\x02 \x01(\tB\x03\xe0\x41\x01H\x01R\tpageToken\x88\x01\x01\x12\x37\n\x04view\x18\x03 \x01(\x0e\x32\x19.model.model.v1alpha.ViewB\x03\xe0\x41\x01H\x02R\x04view\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\x07\n\x05_view\"\xb8\x01\n\x1cListModelDefinitionsResponse\x12Q\n\x11model_definitions\x18\x01 \x03(\x0b\x32$.model.model.v1alpha.ModelDefinitionR\x10modelDefinitions\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12\x1d\n\ntotal_size\x18\x03 \x01(\x05R\ttotalSize\"\x98\x01\n\x19GetModelDefinitionRequest\x12\x37\n\x04view\x18\x02 \x01(\x0e\x32\x19.model.model.v1alpha.ViewB\x03\xe0\x41\x01H\x00R\x04view\x88\x01\x01\x12\x33\n\x13model_definition_id\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x11modelDefinitionIdB\x07\n\x05_viewJ\x04\x08\x01\x10\x02\"r\n\x1aGetModelDefinitionResponse\x12T\n\x10model_definition\x18\x01 \x01(\x0b\x32$.model.model.v1alpha.ModelDefinitionB\x03\xe0\x41\x03R\x0fmodelDefinition*\x9f\x01\n\x0cReleaseStage\x12\x1d\n\x19RELEASE_STAGE_UNSPECIFIED\x10\x00\x12\x17\n\x13RELEASE_STAGE_ALPHA\x10\x01\x12\x16\n\x12RELEASE_STAGE_BETA\x10\x02\x12%\n!RELEASE_STAGE_GENERALLY_AVAILABLE\x10\x03\x12\x18\n\x14RELEASE_STAGE_CUSTOM\x10\x04*;\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\x0e\n\nVIEW_BASIC\x10\x01\x12\r\n\tVIEW_FULL\x10\x02\x42\xe1\x01\n\x17\x63om.model.model.v1alphaB\x14ModelDefinitionProtoP\x01ZBgithub.com/instill-ai/protogen-go/model/model/v1alpha;modelv1alpha\xa2\x02\x03MMX\xaa\x02\x13Model.Model.V1alpha\xca\x02\x13Model\\Model\\V1alpha\xe2\x02\x1fModel\\Model\\V1alpha\\GPBMetadata\xea\x02\x15Model::Model::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model.model.v1alpha.model_definition_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.model.model.v1alphaB\024ModelDefinitionProtoP\001ZBgithub.com/instill-ai/protogen-go/model/model/v1alpha;modelv1alpha\242\002\003MMX\252\002\023Model.Model.V1alpha\312\002\023Model\\Model\\V1alpha\342\002\037Model\\Model\\V1alpha\\GPBMetadata\352\002\025Model::Model::V1alpha'
  _MODELDEFINITION.fields_by_name['name']._options = None
  _MODELDEFINITION.fields_by_name['name']._serialized_options = b'\340A\003'
  _MODELDEFINITION.fields_by_name['uid']._options = None
  _MODELDEFINITION.fields_by_name['uid']._serialized_options = b'\340A\003'
  _MODELDEFINITION.fields_by_name['id']._options = None
  _MODELDEFINITION.fields_by_name['id']._serialized_options = b'\340A\003'
  _MODELDEFINITION.fields_by_name['title']._options = None
  _MODELDEFINITION.fields_by_name['title']._serialized_options = b'\340A\003'
  _MODELDEFINITION.fields_by_name['documentation_url']._options = None
  _MODELDEFINITION.fields_by_name['documentation_url']._serialized_options = b'\340A\003'
  _MODELDEFINITION.fields_by_name['icon']._options = None
  _MODELDEFINITION.fields_by_name['icon']._serialized_options = b'\340A\003'
  _MODELDEFINITION.fields_by_name['release_stage']._options = None
  _MODELDEFINITION.fields_by_name['release_stage']._serialized_options = b'\340A\003'
  _MODELDEFINITION.fields_by_name['model_spec']._options = None
  _MODELDEFINITION.fields_by_name['model_spec']._serialized_options = b'\340A\003'
  _MODELDEFINITION.fields_by_name['create_time']._options = None
  _MODELDEFINITION.fields_by_name['create_time']._serialized_options = b'\340A\003'
  _MODELDEFINITION.fields_by_name['update_time']._options = None
  _MODELDEFINITION.fields_by_name['update_time']._serialized_options = b'\340A\003'
  _MODELDEFINITION._options = None
  _MODELDEFINITION._serialized_options = b'\352A1\022\026model-definitions/{id}\022\027model-definitions/{uid}'
  _LISTMODELDEFINITIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTMODELDEFINITIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTMODELDEFINITIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTMODELDEFINITIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _LISTMODELDEFINITIONSREQUEST.fields_by_name['view']._options = None
  _LISTMODELDEFINITIONSREQUEST.fields_by_name['view']._serialized_options = b'\340A\001'
  _GETMODELDEFINITIONREQUEST.fields_by_name['view']._options = None
  _GETMODELDEFINITIONREQUEST.fields_by_name['view']._serialized_options = b'\340A\001'
  _GETMODELDEFINITIONREQUEST.fields_by_name['model_definition_id']._options = None
  _GETMODELDEFINITIONREQUEST.fields_by_name['model_definition_id']._serialized_options = b'\340A\002'
  _GETMODELDEFINITIONRESPONSE.fields_by_name['model_definition']._options = None
  _GETMODELDEFINITIONRESPONSE.fields_by_name['model_definition']._serialized_options = b'\340A\003'
  _globals['_RELEASESTAGE']._serialized_start=1371
  _globals['_RELEASESTAGE']._serialized_end=1530
  _globals['_VIEW']._serialized_start=1532
  _globals['_VIEW']._serialized_end=1591
  _globals['_MODELDEFINITION']._serialized_start=191
  _globals['_MODELDEFINITION']._serialized_end=703
  _globals['_LISTMODELDEFINITIONSREQUEST']._serialized_start=706
  _globals['_LISTMODELDEFINITIONSREQUEST']._serialized_end=910
  _globals['_LISTMODELDEFINITIONSRESPONSE']._serialized_start=913
  _globals['_LISTMODELDEFINITIONSRESPONSE']._serialized_end=1097
  _globals['_GETMODELDEFINITIONREQUEST']._serialized_start=1100
  _globals['_GETMODELDEFINITIONREQUEST']._serialized_end=1252
  _globals['_GETMODELDEFINITIONRESPONSE']._serialized_start=1254
  _globals['_GETMODELDEFINITIONRESPONSE']._serialized_end=1368
# @@protoc_insertion_point(module_scope)
