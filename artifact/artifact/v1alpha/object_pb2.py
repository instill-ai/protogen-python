# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: artifact/artifact/v1alpha/object.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&artifact/artifact/v1alpha/object.proto\x12\x19\x61rtifact.artifact.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf9\x03\n\x06Object\x12\x10\n\x03uid\x18\x01 \x01(\tR\x03uid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x12\n\x04size\x18\x03 \x01(\x03R\x04size\x12!\n\x0c\x63ontent_type\x18\x04 \x01(\tR\x0b\x63ontentType\x12#\n\rnamespace_uid\x18\x06 \x01(\tR\x0cnamespaceUid\x12\x18\n\x07\x63reator\x18\x07 \x01(\tR\x07\x63reator\x12\x1f\n\x0bis_uploaded\x18\x08 \x01(\x08R\nisUploaded\x12\x17\n\x04path\x18\t \x01(\tH\x00R\x04path\x88\x01\x01\x12,\n\x12object_expire_days\x18\n \x01(\x05R\x10objectExpireDays\x12M\n\x12last_modified_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01R\x10lastModifiedTime\x88\x01\x01\x12=\n\x0c\x63reated_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x63reatedTime\x12=\n\x0cupdated_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0bupdatedTimeB\x07\n\x05_pathB\x15\n\x13_last_modified_time\"\x98\x02\n\x19GetObjectUploadURLRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12$\n\x0bobject_name\x18\x02 \x01(\tB\x03\xe0\x41\x02R\nobjectName\x12+\n\x0furl_expire_days\x18\x03 \x01(\x05\x42\x03\xe0\x41\x01R\rurlExpireDays\x12M\n\x12last_modified_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x01R\x10lastModifiedTime\x12\x31\n\x12object_expire_days\x18\x05 \x01(\x05\x42\x03\xe0\x41\x01R\x10objectExpireDays\"\xb6\x01\n\x1aGetObjectUploadURLResponse\x12\x1d\n\nupload_url\x18\x01 \x01(\tR\tuploadUrl\x12>\n\rurl_expire_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0burlExpireAt\x12\x39\n\x06object\x18\x03 \x01(\x0b\x32!.artifact.artifact.v1alpha.ObjectR\x06object\"\x96\x01\n\x1bGetObjectDownloadURLRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12\"\n\nobject_uid\x18\x02 \x01(\tB\x03\xe0\x41\x02R\tobjectUid\x12+\n\x0furl_expire_days\x18\x03 \x01(\x05\x42\x03\xe0\x41\x01R\rurlExpireDays\"\xbc\x01\n\x1cGetObjectDownloadURLResponse\x12!\n\x0c\x64ownload_url\x18\x01 \x01(\tR\x0b\x64ownloadUrl\x12>\n\rurl_expire_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0burlExpireAt\x12\x39\n\x06object\x18\x03 \x01(\x0b\x32!.artifact.artifact.v1alpha.ObjectR\x06objectB\xff\x01\n\x1d\x63om.artifact.artifact.v1alphaB\x0bObjectProtoP\x01ZKgithub.com/instill-ai/protogen-go/artifact/artifact/v1alpha;artifactv1alpha\xa2\x02\x03\x41\x41X\xaa\x02\x19\x41rtifact.Artifact.V1alpha\xca\x02\x19\x41rtifact\\Artifact\\V1alpha\xe2\x02%Artifact\\Artifact\\V1alpha\\GPBMetadata\xea\x02\x1b\x41rtifact::Artifact::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'artifact.artifact.v1alpha.object_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.artifact.artifact.v1alphaB\013ObjectProtoP\001ZKgithub.com/instill-ai/protogen-go/artifact/artifact/v1alpha;artifactv1alpha\242\002\003AAX\252\002\031Artifact.Artifact.V1alpha\312\002\031Artifact\\Artifact\\V1alpha\342\002%Artifact\\Artifact\\V1alpha\\GPBMetadata\352\002\033Artifact::Artifact::V1alpha'
  _GETOBJECTUPLOADURLREQUEST.fields_by_name['namespace_id']._options = None
  _GETOBJECTUPLOADURLREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _GETOBJECTUPLOADURLREQUEST.fields_by_name['object_name']._options = None
  _GETOBJECTUPLOADURLREQUEST.fields_by_name['object_name']._serialized_options = b'\340A\002'
  _GETOBJECTUPLOADURLREQUEST.fields_by_name['url_expire_days']._options = None
  _GETOBJECTUPLOADURLREQUEST.fields_by_name['url_expire_days']._serialized_options = b'\340A\001'
  _GETOBJECTUPLOADURLREQUEST.fields_by_name['last_modified_time']._options = None
  _GETOBJECTUPLOADURLREQUEST.fields_by_name['last_modified_time']._serialized_options = b'\340A\001'
  _GETOBJECTUPLOADURLREQUEST.fields_by_name['object_expire_days']._options = None
  _GETOBJECTUPLOADURLREQUEST.fields_by_name['object_expire_days']._serialized_options = b'\340A\001'
  _GETOBJECTDOWNLOADURLREQUEST.fields_by_name['namespace_id']._options = None
  _GETOBJECTDOWNLOADURLREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _GETOBJECTDOWNLOADURLREQUEST.fields_by_name['object_uid']._options = None
  _GETOBJECTDOWNLOADURLREQUEST.fields_by_name['object_uid']._serialized_options = b'\340A\002'
  _GETOBJECTDOWNLOADURLREQUEST.fields_by_name['url_expire_days']._options = None
  _GETOBJECTDOWNLOADURLREQUEST.fields_by_name['url_expire_days']._serialized_options = b'\340A\001'
  _globals['_OBJECT']._serialized_start=136
  _globals['_OBJECT']._serialized_end=641
  _globals['_GETOBJECTUPLOADURLREQUEST']._serialized_start=644
  _globals['_GETOBJECTUPLOADURLREQUEST']._serialized_end=924
  _globals['_GETOBJECTUPLOADURLRESPONSE']._serialized_start=927
  _globals['_GETOBJECTUPLOADURLRESPONSE']._serialized_end=1109
  _globals['_GETOBJECTDOWNLOADURLREQUEST']._serialized_start=1112
  _globals['_GETOBJECTDOWNLOADURLREQUEST']._serialized_end=1262
  _globals['_GETOBJECTDOWNLOADURLRESPONSE']._serialized_start=1265
  _globals['_GETOBJECTDOWNLOADURLRESPONSE']._serialized_end=1453
# @@protoc_insertion_point(module_scope)