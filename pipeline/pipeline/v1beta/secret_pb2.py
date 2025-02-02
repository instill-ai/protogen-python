# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pipeline/pipeline/v1beta/secret.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%pipeline/pipeline/v1beta/secret.proto\x12\x18pipeline.pipeline.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x9a\x03\n\x06Secret\x12\x17\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x04name\x12\x15\n\x03uid\x18\x02 \x01(\tB\x03\xe0\x41\x03R\x03uid\x12\x13\n\x02id\x18\x03 \x01(\tB\x03\xe0\x41\x05R\x02id\x12@\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\ncreateTime\x12@\n\x0bupdate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\nupdateTime\x12\x1e\n\x05value\x18\x06 \x01(\tB\x03\xe0\x41\x04H\x00R\x05value\x88\x01\x01\x12%\n\x0b\x64\x65scription\x18\x07 \x01(\tB\x03\xe0\x41\x01R\x0b\x64\x65scription:v\xea\x41s\n\x17\x61pi.instill.tech/Secret\x12#users/{user.id}/secrets/{secret.id}\x12\x33organizations/{organization.id}/secrets/{secret.id}B\x08\n\x06_value\"\x80\x01\n\x1c\x43reateNamespaceSecretRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12\x38\n\x06secret\x18\x02 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\"^\n\x1d\x43reateNamespaceSecretResponse\x12=\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretB\x03\xe0\x41\x03R\x06secret\"\xb2\x01\n\x1bListNamespaceSecretsRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12%\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01H\x00R\x08pageSize\x88\x01\x01\x12\'\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01H\x01R\tpageToken\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_token\"\xb0\x01\n\x1cListNamespaceSecretsResponse\x12?\n\x07secrets\x18\x01 \x03(\x0b\x32 .pipeline.pipeline.v1beta.SecretB\x03\xe0\x41\x03R\x07secrets\x12+\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0\x41\x03R\rnextPageToken\x12\"\n\ntotal_size\x18\x03 \x01(\x05\x42\x03\xe0\x41\x03R\ttotalSize\"e\n\x19GetNamespaceSecretRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12 \n\tsecret_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x08secretId\"V\n\x1aGetNamespaceSecretResponse\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\"\xe4\x01\n\x1cUpdateNamespaceSecretRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12 \n\tsecret_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x08secretId\x12\x38\n\x06secret\x18\x03 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\x12@\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x02R\nupdateMask\"Y\n\x1dUpdateNamespaceSecretResponse\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\"h\n\x1c\x44\x65leteNamespaceSecretRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12 \n\tsecret_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x08secretId\"\x1f\n\x1d\x44\x65leteNamespaceSecretResponse\"\x9e\x01\n\x17\x43reateUserSecretRequest\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\x12I\n\x06parent\x18\x02 \x01(\tB1\x92\x41\x0f\xca>\x0c\xfa\x02\tuser_name\xe0\x41\x02\xfa\x41\x19\x12\x17\x61pi.instill.tech/SecretR\x06parent\"T\n\x18\x43reateUserSecretResponse\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\"\xd0\x01\n\x16ListUserSecretsRequest\x12%\n\tpage_size\x18\x01 \x01(\x05\x42\x03\xe0\x41\x01H\x00R\x08pageSize\x88\x01\x01\x12\'\n\npage_token\x18\x02 \x01(\tB\x03\xe0\x41\x01H\x01R\tpageToken\x88\x01\x01\x12I\n\x06parent\x18\x03 \x01(\tB1\x92\x41\x0f\xca>\x0c\xfa\x02\tuser_name\xe0\x41\x02\xfa\x41\x19\x12\x17\x61pi.instill.tech/SecretR\x06parentB\x0c\n\n_page_sizeB\r\n\x0b_page_token\"\x9c\x01\n\x17ListUserSecretsResponse\x12:\n\x07secrets\x18\x01 \x03(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x07secrets\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12\x1d\n\ntotal_size\x18\x03 \x01(\x05R\ttotalSize\"d\n\x14GetUserSecretRequest\x12L\n\x04name\x18\x01 \x01(\tB8\x92\x41\x16\xca>\x13\xfa\x02\x10user_secret_name\xe0\x41\x02\xfa\x41\x19\n\x17\x61pi.instill.tech/SecretR\x04name\"Q\n\x15GetUserSecretResponse\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\"\x9a\x01\n\x17UpdateUserSecretRequest\x12=\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretB\x03\xe0\x41\x02R\x06secret\x12@\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x02R\nupdateMask\"T\n\x18UpdateUserSecretResponse\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\"g\n\x17\x44\x65leteUserSecretRequest\x12L\n\x04name\x18\x01 \x01(\tB8\x92\x41\x16\xca>\x13\xfa\x02\x10user_secret_name\xe0\x41\x02\xfa\x41\x19\n\x17\x61pi.instill.tech/SecretR\x04name\"\x1a\n\x18\x44\x65leteUserSecretResponse\"\xae\x01\n\x1f\x43reateOrganizationSecretRequest\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\x12Q\n\x06parent\x18\x02 \x01(\tB9\x92\x41\x17\xca>\x14\xfa\x02\x11organization_name\xe0\x41\x02\xfa\x41\x19\x12\x17\x61pi.instill.tech/SecretR\x06parent\"\\\n CreateOrganizationSecretResponse\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\"\xe0\x01\n\x1eListOrganizationSecretsRequest\x12%\n\tpage_size\x18\x01 \x01(\x05\x42\x03\xe0\x41\x01H\x00R\x08pageSize\x88\x01\x01\x12\'\n\npage_token\x18\x02 \x01(\tB\x03\xe0\x41\x01H\x01R\tpageToken\x88\x01\x01\x12Q\n\x06parent\x18\x03 \x01(\tB9\x92\x41\x17\xca>\x14\xfa\x02\x11organization_name\xe0\x41\x02\xfa\x41\x19\x12\x17\x61pi.instill.tech/SecretR\x06parentB\x0c\n\n_page_sizeB\r\n\x0b_page_token\"\xa4\x01\n\x1fListOrganizationSecretsResponse\x12:\n\x07secrets\x18\x01 \x03(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x07secrets\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12\x1d\n\ntotal_size\x18\x03 \x01(\x05R\ttotalSize\"t\n\x1cGetOrganizationSecretRequest\x12T\n\x04name\x18\x01 \x01(\tB@\x92\x41\x1e\xca>\x1b\xfa\x02\x18organization_secret_name\xe0\x41\x02\xfa\x41\x19\n\x17\x61pi.instill.tech/SecretR\x04name\"Y\n\x1dGetOrganizationSecretResponse\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\"\xa2\x01\n\x1fUpdateOrganizationSecretRequest\x12=\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretB\x03\xe0\x41\x02R\x06secret\x12@\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x02R\nupdateMask\"\\\n UpdateOrganizationSecretResponse\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .pipeline.pipeline.v1beta.SecretR\x06secret\"w\n\x1f\x44\x65leteOrganizationSecretRequest\x12T\n\x04name\x18\x01 \x01(\tB@\x92\x41\x1e\xca>\x1b\xfa\x02\x18organization_secret_name\xe0\x41\x02\xfa\x41\x19\n\x17\x61pi.instill.tech/SecretR\x04name\"\"\n DeleteOrganizationSecretResponseB\xf8\x01\n\x1c\x63om.pipeline.pipeline.v1betaB\x0bSecretProtoP\x01ZIgithub.com/instill-ai/protogen-go/pipeline/pipeline/v1beta;pipelinev1beta\xa2\x02\x03PPX\xaa\x02\x18Pipeline.Pipeline.V1beta\xca\x02\x18Pipeline\\Pipeline\\V1beta\xe2\x02$Pipeline\\Pipeline\\V1beta\\GPBMetadata\xea\x02\x1aPipeline::Pipeline::V1betab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pipeline.pipeline.v1beta.secret_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.pipeline.pipeline.v1betaB\013SecretProtoP\001ZIgithub.com/instill-ai/protogen-go/pipeline/pipeline/v1beta;pipelinev1beta\242\002\003PPX\252\002\030Pipeline.Pipeline.V1beta\312\002\030Pipeline\\Pipeline\\V1beta\342\002$Pipeline\\Pipeline\\V1beta\\GPBMetadata\352\002\032Pipeline::Pipeline::V1beta'
  _SECRET.fields_by_name['name']._options = None
  _SECRET.fields_by_name['name']._serialized_options = b'\340A\003'
  _SECRET.fields_by_name['uid']._options = None
  _SECRET.fields_by_name['uid']._serialized_options = b'\340A\003'
  _SECRET.fields_by_name['id']._options = None
  _SECRET.fields_by_name['id']._serialized_options = b'\340A\005'
  _SECRET.fields_by_name['create_time']._options = None
  _SECRET.fields_by_name['create_time']._serialized_options = b'\340A\003'
  _SECRET.fields_by_name['update_time']._options = None
  _SECRET.fields_by_name['update_time']._serialized_options = b'\340A\003'
  _SECRET.fields_by_name['value']._options = None
  _SECRET.fields_by_name['value']._serialized_options = b'\340A\004'
  _SECRET.fields_by_name['description']._options = None
  _SECRET.fields_by_name['description']._serialized_options = b'\340A\001'
  _SECRET._options = None
  _SECRET._serialized_options = b'\352As\n\027api.instill.tech/Secret\022#users/{user.id}/secrets/{secret.id}\0223organizations/{organization.id}/secrets/{secret.id}'
  _CREATENAMESPACESECRETREQUEST.fields_by_name['namespace_id']._options = None
  _CREATENAMESPACESECRETREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _CREATENAMESPACESECRETRESPONSE.fields_by_name['secret']._options = None
  _CREATENAMESPACESECRETRESPONSE.fields_by_name['secret']._serialized_options = b'\340A\003'
  _LISTNAMESPACESECRETSREQUEST.fields_by_name['namespace_id']._options = None
  _LISTNAMESPACESECRETSREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _LISTNAMESPACESECRETSREQUEST.fields_by_name['page_size']._options = None
  _LISTNAMESPACESECRETSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTNAMESPACESECRETSREQUEST.fields_by_name['page_token']._options = None
  _LISTNAMESPACESECRETSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _LISTNAMESPACESECRETSRESPONSE.fields_by_name['secrets']._options = None
  _LISTNAMESPACESECRETSRESPONSE.fields_by_name['secrets']._serialized_options = b'\340A\003'
  _LISTNAMESPACESECRETSRESPONSE.fields_by_name['next_page_token']._options = None
  _LISTNAMESPACESECRETSRESPONSE.fields_by_name['next_page_token']._serialized_options = b'\340A\003'
  _LISTNAMESPACESECRETSRESPONSE.fields_by_name['total_size']._options = None
  _LISTNAMESPACESECRETSRESPONSE.fields_by_name['total_size']._serialized_options = b'\340A\003'
  _GETNAMESPACESECRETREQUEST.fields_by_name['namespace_id']._options = None
  _GETNAMESPACESECRETREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _GETNAMESPACESECRETREQUEST.fields_by_name['secret_id']._options = None
  _GETNAMESPACESECRETREQUEST.fields_by_name['secret_id']._serialized_options = b'\340A\002'
  _UPDATENAMESPACESECRETREQUEST.fields_by_name['namespace_id']._options = None
  _UPDATENAMESPACESECRETREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _UPDATENAMESPACESECRETREQUEST.fields_by_name['secret_id']._options = None
  _UPDATENAMESPACESECRETREQUEST.fields_by_name['secret_id']._serialized_options = b'\340A\002'
  _UPDATENAMESPACESECRETREQUEST.fields_by_name['update_mask']._options = None
  _UPDATENAMESPACESECRETREQUEST.fields_by_name['update_mask']._serialized_options = b'\340A\002'
  _DELETENAMESPACESECRETREQUEST.fields_by_name['namespace_id']._options = None
  _DELETENAMESPACESECRETREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _DELETENAMESPACESECRETREQUEST.fields_by_name['secret_id']._options = None
  _DELETENAMESPACESECRETREQUEST.fields_by_name['secret_id']._serialized_options = b'\340A\002'
  _CREATEUSERSECRETREQUEST.fields_by_name['parent']._options = None
  _CREATEUSERSECRETREQUEST.fields_by_name['parent']._serialized_options = b'\222A\017\312>\014\372\002\tuser_name\340A\002\372A\031\022\027api.instill.tech/Secret'
  _LISTUSERSECRETSREQUEST.fields_by_name['page_size']._options = None
  _LISTUSERSECRETSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTUSERSECRETSREQUEST.fields_by_name['page_token']._options = None
  _LISTUSERSECRETSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _LISTUSERSECRETSREQUEST.fields_by_name['parent']._options = None
  _LISTUSERSECRETSREQUEST.fields_by_name['parent']._serialized_options = b'\222A\017\312>\014\372\002\tuser_name\340A\002\372A\031\022\027api.instill.tech/Secret'
  _GETUSERSECRETREQUEST.fields_by_name['name']._options = None
  _GETUSERSECRETREQUEST.fields_by_name['name']._serialized_options = b'\222A\026\312>\023\372\002\020user_secret_name\340A\002\372A\031\n\027api.instill.tech/Secret'
  _UPDATEUSERSECRETREQUEST.fields_by_name['secret']._options = None
  _UPDATEUSERSECRETREQUEST.fields_by_name['secret']._serialized_options = b'\340A\002'
  _UPDATEUSERSECRETREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEUSERSECRETREQUEST.fields_by_name['update_mask']._serialized_options = b'\340A\002'
  _DELETEUSERSECRETREQUEST.fields_by_name['name']._options = None
  _DELETEUSERSECRETREQUEST.fields_by_name['name']._serialized_options = b'\222A\026\312>\023\372\002\020user_secret_name\340A\002\372A\031\n\027api.instill.tech/Secret'
  _CREATEORGANIZATIONSECRETREQUEST.fields_by_name['parent']._options = None
  _CREATEORGANIZATIONSECRETREQUEST.fields_by_name['parent']._serialized_options = b'\222A\027\312>\024\372\002\021organization_name\340A\002\372A\031\022\027api.instill.tech/Secret'
  _LISTORGANIZATIONSECRETSREQUEST.fields_by_name['page_size']._options = None
  _LISTORGANIZATIONSECRETSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTORGANIZATIONSECRETSREQUEST.fields_by_name['page_token']._options = None
  _LISTORGANIZATIONSECRETSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _LISTORGANIZATIONSECRETSREQUEST.fields_by_name['parent']._options = None
  _LISTORGANIZATIONSECRETSREQUEST.fields_by_name['parent']._serialized_options = b'\222A\027\312>\024\372\002\021organization_name\340A\002\372A\031\022\027api.instill.tech/Secret'
  _GETORGANIZATIONSECRETREQUEST.fields_by_name['name']._options = None
  _GETORGANIZATIONSECRETREQUEST.fields_by_name['name']._serialized_options = b'\222A\036\312>\033\372\002\030organization_secret_name\340A\002\372A\031\n\027api.instill.tech/Secret'
  _UPDATEORGANIZATIONSECRETREQUEST.fields_by_name['secret']._options = None
  _UPDATEORGANIZATIONSECRETREQUEST.fields_by_name['secret']._serialized_options = b'\340A\002'
  _UPDATEORGANIZATIONSECRETREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEORGANIZATIONSECRETREQUEST.fields_by_name['update_mask']._serialized_options = b'\340A\002'
  _DELETEORGANIZATIONSECRETREQUEST.fields_by_name['name']._options = None
  _DELETEORGANIZATIONSECRETREQUEST.fields_by_name['name']._serialized_options = b'\222A\036\312>\033\372\002\030organization_secret_name\340A\002\372A\031\n\027api.instill.tech/Secret'
  _globals['_SECRET']._serialized_start=243
  _globals['_SECRET']._serialized_end=653
  _globals['_CREATENAMESPACESECRETREQUEST']._serialized_start=656
  _globals['_CREATENAMESPACESECRETREQUEST']._serialized_end=784
  _globals['_CREATENAMESPACESECRETRESPONSE']._serialized_start=786
  _globals['_CREATENAMESPACESECRETRESPONSE']._serialized_end=880
  _globals['_LISTNAMESPACESECRETSREQUEST']._serialized_start=883
  _globals['_LISTNAMESPACESECRETSREQUEST']._serialized_end=1061
  _globals['_LISTNAMESPACESECRETSRESPONSE']._serialized_start=1064
  _globals['_LISTNAMESPACESECRETSRESPONSE']._serialized_end=1240
  _globals['_GETNAMESPACESECRETREQUEST']._serialized_start=1242
  _globals['_GETNAMESPACESECRETREQUEST']._serialized_end=1343
  _globals['_GETNAMESPACESECRETRESPONSE']._serialized_start=1345
  _globals['_GETNAMESPACESECRETRESPONSE']._serialized_end=1431
  _globals['_UPDATENAMESPACESECRETREQUEST']._serialized_start=1434
  _globals['_UPDATENAMESPACESECRETREQUEST']._serialized_end=1662
  _globals['_UPDATENAMESPACESECRETRESPONSE']._serialized_start=1664
  _globals['_UPDATENAMESPACESECRETRESPONSE']._serialized_end=1753
  _globals['_DELETENAMESPACESECRETREQUEST']._serialized_start=1755
  _globals['_DELETENAMESPACESECRETREQUEST']._serialized_end=1859
  _globals['_DELETENAMESPACESECRETRESPONSE']._serialized_start=1861
  _globals['_DELETENAMESPACESECRETRESPONSE']._serialized_end=1892
  _globals['_CREATEUSERSECRETREQUEST']._serialized_start=1895
  _globals['_CREATEUSERSECRETREQUEST']._serialized_end=2053
  _globals['_CREATEUSERSECRETRESPONSE']._serialized_start=2055
  _globals['_CREATEUSERSECRETRESPONSE']._serialized_end=2139
  _globals['_LISTUSERSECRETSREQUEST']._serialized_start=2142
  _globals['_LISTUSERSECRETSREQUEST']._serialized_end=2350
  _globals['_LISTUSERSECRETSRESPONSE']._serialized_start=2353
  _globals['_LISTUSERSECRETSRESPONSE']._serialized_end=2509
  _globals['_GETUSERSECRETREQUEST']._serialized_start=2511
  _globals['_GETUSERSECRETREQUEST']._serialized_end=2611
  _globals['_GETUSERSECRETRESPONSE']._serialized_start=2613
  _globals['_GETUSERSECRETRESPONSE']._serialized_end=2694
  _globals['_UPDATEUSERSECRETREQUEST']._serialized_start=2697
  _globals['_UPDATEUSERSECRETREQUEST']._serialized_end=2851
  _globals['_UPDATEUSERSECRETRESPONSE']._serialized_start=2853
  _globals['_UPDATEUSERSECRETRESPONSE']._serialized_end=2937
  _globals['_DELETEUSERSECRETREQUEST']._serialized_start=2939
  _globals['_DELETEUSERSECRETREQUEST']._serialized_end=3042
  _globals['_DELETEUSERSECRETRESPONSE']._serialized_start=3044
  _globals['_DELETEUSERSECRETRESPONSE']._serialized_end=3070
  _globals['_CREATEORGANIZATIONSECRETREQUEST']._serialized_start=3073
  _globals['_CREATEORGANIZATIONSECRETREQUEST']._serialized_end=3247
  _globals['_CREATEORGANIZATIONSECRETRESPONSE']._serialized_start=3249
  _globals['_CREATEORGANIZATIONSECRETRESPONSE']._serialized_end=3341
  _globals['_LISTORGANIZATIONSECRETSREQUEST']._serialized_start=3344
  _globals['_LISTORGANIZATIONSECRETSREQUEST']._serialized_end=3568
  _globals['_LISTORGANIZATIONSECRETSRESPONSE']._serialized_start=3571
  _globals['_LISTORGANIZATIONSECRETSRESPONSE']._serialized_end=3735
  _globals['_GETORGANIZATIONSECRETREQUEST']._serialized_start=3737
  _globals['_GETORGANIZATIONSECRETREQUEST']._serialized_end=3853
  _globals['_GETORGANIZATIONSECRETRESPONSE']._serialized_start=3855
  _globals['_GETORGANIZATIONSECRETRESPONSE']._serialized_end=3944
  _globals['_UPDATEORGANIZATIONSECRETREQUEST']._serialized_start=3947
  _globals['_UPDATEORGANIZATIONSECRETREQUEST']._serialized_end=4109
  _globals['_UPDATEORGANIZATIONSECRETRESPONSE']._serialized_start=4111
  _globals['_UPDATEORGANIZATIONSECRETRESPONSE']._serialized_end=4203
  _globals['_DELETEORGANIZATIONSECRETREQUEST']._serialized_start=4205
  _globals['_DELETEORGANIZATIONSECRETREQUEST']._serialized_end=4324
  _globals['_DELETEORGANIZATIONSECRETRESPONSE']._serialized_start=4326
  _globals['_DELETEORGANIZATIONSECRETRESPONSE']._serialized_end=4360
# @@protoc_insertion_point(module_scope)
