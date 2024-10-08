# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vdp/pipeline/v1beta/integration.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from vdp.pipeline.v1beta import common_pb2 as vdp_dot_pipeline_dot_v1beta_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%vdp/pipeline/v1beta/integration.proto\x12\x13vdp.pipeline.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a vdp/pipeline/v1beta/common.proto\"\x80\x06\n\nConnection\x12\x15\n\x03uid\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x03uid\x12\x13\n\x02id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x02id\x12)\n\x0cnamespace_id\x18\x03 \x01(\tB\x06\xe0\x41\x02\xe0\x41\x05R\x0bnamespaceId\x12-\n\x0eintegration_id\x18\x04 \x01(\tB\x06\xe0\x41\x02\xe0\x41\x05R\rintegrationId\x12\x30\n\x11integration_title\x18\x05 \x01(\tB\x03\xe0\x41\x03R\x10integrationTitle\x12\x43\n\x06method\x18\x06 \x01(\x0e\x32&.vdp.pipeline.v1beta.Connection.MethodB\x03\xe0\x41\x02R\x06method\x12\x32\n\x05setup\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructB\x03\xe0\x41\x02R\x05setup\x12\x1b\n\x06scopes\x18\x0b \x03(\tB\x03\xe0\x41\x01R\x06scopes\x12$\n\x08identity\x18\r \x01(\tB\x03\xe0\x41\x01H\x00R\x08identity\x88\x01\x01\x12T\n\x15o_auth_access_details\x18\x0c \x01(\x0b\x32\x17.google.protobuf.StructB\x03\xe0\x41\x01H\x01R\x12oAuthAccessDetails\x88\x01\x01\x12\x32\n\x04view\x18\x08 \x01(\x0e\x32\x19.vdp.pipeline.v1beta.ViewB\x03\xe0\x41\x03R\x04view\x12@\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\ncreateTime\x12@\n\x0bupdate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\nupdateTime\"I\n\x06Method\x12\x16\n\x12METHOD_UNSPECIFIED\x10\x00\x12\x15\n\x11METHOD_DICTIONARY\x10\x01\x12\x10\n\x0cMETHOD_OAUTH\x10\x02\x42\x0b\n\t_identityB\x18\n\x16_o_auth_access_details\"\xe3\x01\n\x1fListNamespaceConnectionsRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12%\n\tpage_size\x18\x02 \x01(\x05\x42\x03\xe0\x41\x01H\x00R\x08pageSize\x88\x01\x01\x12\'\n\npage_token\x18\x03 \x01(\tB\x03\xe0\x41\x01H\x01R\tpageToken\x88\x01\x01\x12 \n\x06\x66ilter\x18\x04 \x01(\tB\x03\xe0\x41\x01H\x02R\x06\x66ilter\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\t\n\x07_filter\"\xbb\x01\n ListNamespaceConnectionsResponse\x12\x46\n\x0b\x63onnections\x18\x01 \x03(\x0b\x32\x1f.vdp.pipeline.v1beta.ConnectionB\x03\xe0\x41\x03R\x0b\x63onnections\x12+\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0\x41\x03R\rnextPageToken\x12\"\n\ntotal_size\x18\x03 \x01(\x05\x42\x03\xe0\x41\x03R\ttotalSize\"\xb3\x01\n\x1dGetNamespaceConnectionRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12(\n\rconnection_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x0c\x63onnectionId\x12\x37\n\x04view\x18\x03 \x01(\x0e\x32\x19.vdp.pipeline.v1beta.ViewB\x03\xe0\x41\x01H\x00R\x04view\x88\x01\x01\x42\x07\n\x05_view\"f\n\x1eGetNamespaceConnectionResponse\x12\x44\n\nconnection\x18\x01 \x01(\x0b\x32\x1f.vdp.pipeline.v1beta.ConnectionB\x03\xe0\x41\x03R\nconnection\"h\n CreateNamespaceConnectionRequest\x12\x44\n\nconnection\x18\x01 \x01(\x0b\x32\x1f.vdp.pipeline.v1beta.ConnectionB\x03\xe0\x41\x02R\nconnection\"i\n!CreateNamespaceConnectionResponse\x12\x44\n\nconnection\x18\x01 \x01(\x0b\x32\x1f.vdp.pipeline.v1beta.ConnectionB\x03\xe0\x41\x03R\nconnection\"\xd4\x01\n UpdateNamespaceConnectionRequest\x12(\n\rconnection_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0c\x63onnectionId\x12\x44\n\nconnection\x18\x02 \x01(\x0b\x32\x1f.vdp.pipeline.v1beta.ConnectionB\x03\xe0\x41\x02R\nconnection\x12@\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x02R\nupdateMask\"i\n!UpdateNamespaceConnectionResponse\x12\x44\n\nconnection\x18\x01 \x01(\x0b\x32\x1f.vdp.pipeline.v1beta.ConnectionB\x03\xe0\x41\x03R\nconnection\"t\n DeleteNamespaceConnectionRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12(\n\rconnection_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x0c\x63onnectionId\"#\n!DeleteNamespaceConnectionResponse\"r\n\x1eTestNamespaceConnectionRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12(\n\rconnection_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x0c\x63onnectionId\"!\n\x1fTestNamespaceConnectionResponse\"\xf6\x06\n\x0bIntegration\x12\x15\n\x03uid\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x03uid\x12\x13\n\x02id\x18\x02 \x01(\tB\x03\xe0\x41\x03R\x02id\x12\x19\n\x05title\x18\x03 \x01(\tB\x03\xe0\x41\x03R\x05title\x12%\n\x0b\x64\x65scription\x18\x04 \x01(\tB\x03\xe0\x41\x03R\x0b\x64\x65scription\x12\x1b\n\x06vendor\x18\x05 \x01(\tB\x03\xe0\x41\x03R\x06vendor\x12\x17\n\x04icon\x18\x06 \x01(\tB\x03\xe0\x41\x03R\x04icon\x12L\n\thelp_link\x18\x07 \x01(\x0b\x32%.vdp.pipeline.v1beta.Integration.LinkB\x03\xe0\x41\x03H\x00R\x08helpLink\x88\x01\x01\x12?\n\x0csetup_schema\x18\n \x01(\x0b\x32\x17.google.protobuf.StructB\x03\xe0\x41\x03R\x0bsetupSchema\x12Z\n\ro_auth_config\x18\x0b \x01(\x0b\x32,.vdp.pipeline.v1beta.Integration.OAuthConfigB\x03\xe0\x41\x03H\x01R\x0boAuthConfig\x88\x01\x01\x12\x32\n\x04view\x18\t \x01(\x0e\x32\x19.vdp.pipeline.v1beta.ViewB\x03\xe0\x41\x03R\x04view\x12M\n\x07schemas\x18\x08 \x03(\x0b\x32,.vdp.pipeline.v1beta.Integration.SetupSchemaB\x05\x18\x01\xe0\x41\x03R\x07schemas\x1a\x36\n\x04Link\x12\x17\n\x04text\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x04text\x12\x15\n\x03url\x18\x02 \x01(\tB\x03\xe0\x41\x03R\x03url\x1an\n\x0bOAuthConfig\x12\x1e\n\x08\x61uth_url\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x07\x61uthUrl\x12\"\n\naccess_url\x18\x02 \x01(\tB\x03\xe0\x41\x03R\taccessUrl\x12\x1b\n\x06scopes\x18\x0b \x03(\tB\x03\xe0\x41\x03R\x06scopes\x1a\x8c\x01\n\x0bSetupSchema\x12\x45\n\x06method\x18\x01 \x01(\x0e\x32&.vdp.pipeline.v1beta.Connection.MethodB\x05\x18\x01\xe0\x41\x03R\x06method\x12\x36\n\x06schema\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x05\x18\x01\xe0\x41\x03R\x06schemaB\x0c\n\n_help_linkB\x10\n\x0e_o_auth_config\"\x92\x02\n$ListPipelineIDsByConnectionIDRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12(\n\rconnection_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x0c\x63onnectionId\x12%\n\tpage_size\x18\x03 \x01(\x05\x42\x03\xe0\x41\x01H\x00R\x08pageSize\x88\x01\x01\x12\'\n\npage_token\x18\x04 \x01(\tB\x03\xe0\x41\x01H\x01R\tpageToken\x88\x01\x01\x12 \n\x06\x66ilter\x18\x05 \x01(\tB\x03\xe0\x41\x01H\x02R\x06\x66ilter\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\t\n\x07_filter\"\xa0\x01\n%ListPipelineIDsByConnectionIDResponse\x12&\n\x0cpipeline_ids\x18\x01 \x03(\tB\x03\xe0\x41\x03R\x0bpipelineIds\x12+\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0\x41\x03R\rnextPageToken\x12\"\n\ntotal_size\x18\x03 \x01(\x05\x42\x03\xe0\x41\x03R\ttotalSize\"\xb3\x01\n\x17ListIntegrationsRequest\x12%\n\tpage_size\x18\x01 \x01(\x05\x42\x03\xe0\x41\x01H\x00R\x08pageSize\x88\x01\x01\x12\'\n\npage_token\x18\x02 \x01(\tB\x03\xe0\x41\x01H\x01R\tpageToken\x88\x01\x01\x12 \n\x06\x66ilter\x18\x03 \x01(\tB\x03\xe0\x41\x01H\x02R\x06\x66ilter\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\t\n\x07_filter\"\xb6\x01\n\x18ListIntegrationsResponse\x12I\n\x0cintegrations\x18\x01 \x03(\x0b\x32 .vdp.pipeline.v1beta.IntegrationB\x03\xe0\x41\x03R\x0cintegrations\x12+\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0\x41\x03R\rnextPageToken\x12\"\n\ntotal_size\x18\x03 \x01(\x05\x42\x03\xe0\x41\x03R\ttotalSize\"\x85\x01\n\x15GetIntegrationRequest\x12*\n\x0eintegration_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\rintegrationId\x12\x37\n\x04view\x18\x02 \x01(\x0e\x32\x19.vdp.pipeline.v1beta.ViewB\x03\xe0\x41\x01H\x00R\x04view\x88\x01\x01\x42\x07\n\x05_view\"a\n\x16GetIntegrationResponse\x12G\n\x0bintegration\x18\x01 \x01(\x0b\x32 .vdp.pipeline.v1beta.IntegrationB\x03\xe0\x41\x03R\x0bintegrationB\xdf\x01\n\x17\x63om.vdp.pipeline.v1betaB\x10IntegrationProtoP\x01ZDgithub.com/instill-ai/protogen-go/vdp/pipeline/v1beta;pipelinev1beta\xa2\x02\x03VPX\xaa\x02\x13Vdp.Pipeline.V1beta\xca\x02\x13Vdp\\Pipeline\\V1beta\xe2\x02\x1fVdp\\Pipeline\\V1beta\\GPBMetadata\xea\x02\x15Vdp::Pipeline::V1betab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vdp.pipeline.v1beta.integration_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.vdp.pipeline.v1betaB\020IntegrationProtoP\001ZDgithub.com/instill-ai/protogen-go/vdp/pipeline/v1beta;pipelinev1beta\242\002\003VPX\252\002\023Vdp.Pipeline.V1beta\312\002\023Vdp\\Pipeline\\V1beta\342\002\037Vdp\\Pipeline\\V1beta\\GPBMetadata\352\002\025Vdp::Pipeline::V1beta'
  _CONNECTION.fields_by_name['uid']._options = None
  _CONNECTION.fields_by_name['uid']._serialized_options = b'\340A\003'
  _CONNECTION.fields_by_name['id']._options = None
  _CONNECTION.fields_by_name['id']._serialized_options = b'\340A\002'
  _CONNECTION.fields_by_name['namespace_id']._options = None
  _CONNECTION.fields_by_name['namespace_id']._serialized_options = b'\340A\002\340A\005'
  _CONNECTION.fields_by_name['integration_id']._options = None
  _CONNECTION.fields_by_name['integration_id']._serialized_options = b'\340A\002\340A\005'
  _CONNECTION.fields_by_name['integration_title']._options = None
  _CONNECTION.fields_by_name['integration_title']._serialized_options = b'\340A\003'
  _CONNECTION.fields_by_name['method']._options = None
  _CONNECTION.fields_by_name['method']._serialized_options = b'\340A\002'
  _CONNECTION.fields_by_name['setup']._options = None
  _CONNECTION.fields_by_name['setup']._serialized_options = b'\340A\002'
  _CONNECTION.fields_by_name['scopes']._options = None
  _CONNECTION.fields_by_name['scopes']._serialized_options = b'\340A\001'
  _CONNECTION.fields_by_name['identity']._options = None
  _CONNECTION.fields_by_name['identity']._serialized_options = b'\340A\001'
  _CONNECTION.fields_by_name['o_auth_access_details']._options = None
  _CONNECTION.fields_by_name['o_auth_access_details']._serialized_options = b'\340A\001'
  _CONNECTION.fields_by_name['view']._options = None
  _CONNECTION.fields_by_name['view']._serialized_options = b'\340A\003'
  _CONNECTION.fields_by_name['create_time']._options = None
  _CONNECTION.fields_by_name['create_time']._serialized_options = b'\340A\003'
  _CONNECTION.fields_by_name['update_time']._options = None
  _CONNECTION.fields_by_name['update_time']._serialized_options = b'\340A\003'
  _LISTNAMESPACECONNECTIONSREQUEST.fields_by_name['namespace_id']._options = None
  _LISTNAMESPACECONNECTIONSREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _LISTNAMESPACECONNECTIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTNAMESPACECONNECTIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTNAMESPACECONNECTIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTNAMESPACECONNECTIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _LISTNAMESPACECONNECTIONSREQUEST.fields_by_name['filter']._options = None
  _LISTNAMESPACECONNECTIONSREQUEST.fields_by_name['filter']._serialized_options = b'\340A\001'
  _LISTNAMESPACECONNECTIONSRESPONSE.fields_by_name['connections']._options = None
  _LISTNAMESPACECONNECTIONSRESPONSE.fields_by_name['connections']._serialized_options = b'\340A\003'
  _LISTNAMESPACECONNECTIONSRESPONSE.fields_by_name['next_page_token']._options = None
  _LISTNAMESPACECONNECTIONSRESPONSE.fields_by_name['next_page_token']._serialized_options = b'\340A\003'
  _LISTNAMESPACECONNECTIONSRESPONSE.fields_by_name['total_size']._options = None
  _LISTNAMESPACECONNECTIONSRESPONSE.fields_by_name['total_size']._serialized_options = b'\340A\003'
  _GETNAMESPACECONNECTIONREQUEST.fields_by_name['namespace_id']._options = None
  _GETNAMESPACECONNECTIONREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _GETNAMESPACECONNECTIONREQUEST.fields_by_name['connection_id']._options = None
  _GETNAMESPACECONNECTIONREQUEST.fields_by_name['connection_id']._serialized_options = b'\340A\002'
  _GETNAMESPACECONNECTIONREQUEST.fields_by_name['view']._options = None
  _GETNAMESPACECONNECTIONREQUEST.fields_by_name['view']._serialized_options = b'\340A\001'
  _GETNAMESPACECONNECTIONRESPONSE.fields_by_name['connection']._options = None
  _GETNAMESPACECONNECTIONRESPONSE.fields_by_name['connection']._serialized_options = b'\340A\003'
  _CREATENAMESPACECONNECTIONREQUEST.fields_by_name['connection']._options = None
  _CREATENAMESPACECONNECTIONREQUEST.fields_by_name['connection']._serialized_options = b'\340A\002'
  _CREATENAMESPACECONNECTIONRESPONSE.fields_by_name['connection']._options = None
  _CREATENAMESPACECONNECTIONRESPONSE.fields_by_name['connection']._serialized_options = b'\340A\003'
  _UPDATENAMESPACECONNECTIONREQUEST.fields_by_name['connection_id']._options = None
  _UPDATENAMESPACECONNECTIONREQUEST.fields_by_name['connection_id']._serialized_options = b'\340A\002'
  _UPDATENAMESPACECONNECTIONREQUEST.fields_by_name['connection']._options = None
  _UPDATENAMESPACECONNECTIONREQUEST.fields_by_name['connection']._serialized_options = b'\340A\002'
  _UPDATENAMESPACECONNECTIONREQUEST.fields_by_name['update_mask']._options = None
  _UPDATENAMESPACECONNECTIONREQUEST.fields_by_name['update_mask']._serialized_options = b'\340A\002'
  _UPDATENAMESPACECONNECTIONRESPONSE.fields_by_name['connection']._options = None
  _UPDATENAMESPACECONNECTIONRESPONSE.fields_by_name['connection']._serialized_options = b'\340A\003'
  _DELETENAMESPACECONNECTIONREQUEST.fields_by_name['namespace_id']._options = None
  _DELETENAMESPACECONNECTIONREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _DELETENAMESPACECONNECTIONREQUEST.fields_by_name['connection_id']._options = None
  _DELETENAMESPACECONNECTIONREQUEST.fields_by_name['connection_id']._serialized_options = b'\340A\002'
  _TESTNAMESPACECONNECTIONREQUEST.fields_by_name['namespace_id']._options = None
  _TESTNAMESPACECONNECTIONREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _TESTNAMESPACECONNECTIONREQUEST.fields_by_name['connection_id']._options = None
  _TESTNAMESPACECONNECTIONREQUEST.fields_by_name['connection_id']._serialized_options = b'\340A\002'
  _INTEGRATION_LINK.fields_by_name['text']._options = None
  _INTEGRATION_LINK.fields_by_name['text']._serialized_options = b'\340A\003'
  _INTEGRATION_LINK.fields_by_name['url']._options = None
  _INTEGRATION_LINK.fields_by_name['url']._serialized_options = b'\340A\003'
  _INTEGRATION_OAUTHCONFIG.fields_by_name['auth_url']._options = None
  _INTEGRATION_OAUTHCONFIG.fields_by_name['auth_url']._serialized_options = b'\340A\003'
  _INTEGRATION_OAUTHCONFIG.fields_by_name['access_url']._options = None
  _INTEGRATION_OAUTHCONFIG.fields_by_name['access_url']._serialized_options = b'\340A\003'
  _INTEGRATION_OAUTHCONFIG.fields_by_name['scopes']._options = None
  _INTEGRATION_OAUTHCONFIG.fields_by_name['scopes']._serialized_options = b'\340A\003'
  _INTEGRATION_SETUPSCHEMA.fields_by_name['method']._options = None
  _INTEGRATION_SETUPSCHEMA.fields_by_name['method']._serialized_options = b'\030\001\340A\003'
  _INTEGRATION_SETUPSCHEMA.fields_by_name['schema']._options = None
  _INTEGRATION_SETUPSCHEMA.fields_by_name['schema']._serialized_options = b'\030\001\340A\003'
  _INTEGRATION.fields_by_name['uid']._options = None
  _INTEGRATION.fields_by_name['uid']._serialized_options = b'\340A\003'
  _INTEGRATION.fields_by_name['id']._options = None
  _INTEGRATION.fields_by_name['id']._serialized_options = b'\340A\003'
  _INTEGRATION.fields_by_name['title']._options = None
  _INTEGRATION.fields_by_name['title']._serialized_options = b'\340A\003'
  _INTEGRATION.fields_by_name['description']._options = None
  _INTEGRATION.fields_by_name['description']._serialized_options = b'\340A\003'
  _INTEGRATION.fields_by_name['vendor']._options = None
  _INTEGRATION.fields_by_name['vendor']._serialized_options = b'\340A\003'
  _INTEGRATION.fields_by_name['icon']._options = None
  _INTEGRATION.fields_by_name['icon']._serialized_options = b'\340A\003'
  _INTEGRATION.fields_by_name['help_link']._options = None
  _INTEGRATION.fields_by_name['help_link']._serialized_options = b'\340A\003'
  _INTEGRATION.fields_by_name['setup_schema']._options = None
  _INTEGRATION.fields_by_name['setup_schema']._serialized_options = b'\340A\003'
  _INTEGRATION.fields_by_name['o_auth_config']._options = None
  _INTEGRATION.fields_by_name['o_auth_config']._serialized_options = b'\340A\003'
  _INTEGRATION.fields_by_name['view']._options = None
  _INTEGRATION.fields_by_name['view']._serialized_options = b'\340A\003'
  _INTEGRATION.fields_by_name['schemas']._options = None
  _INTEGRATION.fields_by_name['schemas']._serialized_options = b'\030\001\340A\003'
  _LISTPIPELINEIDSBYCONNECTIONIDREQUEST.fields_by_name['namespace_id']._options = None
  _LISTPIPELINEIDSBYCONNECTIONIDREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _LISTPIPELINEIDSBYCONNECTIONIDREQUEST.fields_by_name['connection_id']._options = None
  _LISTPIPELINEIDSBYCONNECTIONIDREQUEST.fields_by_name['connection_id']._serialized_options = b'\340A\002'
  _LISTPIPELINEIDSBYCONNECTIONIDREQUEST.fields_by_name['page_size']._options = None
  _LISTPIPELINEIDSBYCONNECTIONIDREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTPIPELINEIDSBYCONNECTIONIDREQUEST.fields_by_name['page_token']._options = None
  _LISTPIPELINEIDSBYCONNECTIONIDREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _LISTPIPELINEIDSBYCONNECTIONIDREQUEST.fields_by_name['filter']._options = None
  _LISTPIPELINEIDSBYCONNECTIONIDREQUEST.fields_by_name['filter']._serialized_options = b'\340A\001'
  _LISTPIPELINEIDSBYCONNECTIONIDRESPONSE.fields_by_name['pipeline_ids']._options = None
  _LISTPIPELINEIDSBYCONNECTIONIDRESPONSE.fields_by_name['pipeline_ids']._serialized_options = b'\340A\003'
  _LISTPIPELINEIDSBYCONNECTIONIDRESPONSE.fields_by_name['next_page_token']._options = None
  _LISTPIPELINEIDSBYCONNECTIONIDRESPONSE.fields_by_name['next_page_token']._serialized_options = b'\340A\003'
  _LISTPIPELINEIDSBYCONNECTIONIDRESPONSE.fields_by_name['total_size']._options = None
  _LISTPIPELINEIDSBYCONNECTIONIDRESPONSE.fields_by_name['total_size']._serialized_options = b'\340A\003'
  _LISTINTEGRATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTINTEGRATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTINTEGRATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTINTEGRATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _LISTINTEGRATIONSREQUEST.fields_by_name['filter']._options = None
  _LISTINTEGRATIONSREQUEST.fields_by_name['filter']._serialized_options = b'\340A\001'
  _LISTINTEGRATIONSRESPONSE.fields_by_name['integrations']._options = None
  _LISTINTEGRATIONSRESPONSE.fields_by_name['integrations']._serialized_options = b'\340A\003'
  _LISTINTEGRATIONSRESPONSE.fields_by_name['next_page_token']._options = None
  _LISTINTEGRATIONSRESPONSE.fields_by_name['next_page_token']._serialized_options = b'\340A\003'
  _LISTINTEGRATIONSRESPONSE.fields_by_name['total_size']._options = None
  _LISTINTEGRATIONSRESPONSE.fields_by_name['total_size']._serialized_options = b'\340A\003'
  _GETINTEGRATIONREQUEST.fields_by_name['integration_id']._options = None
  _GETINTEGRATIONREQUEST.fields_by_name['integration_id']._serialized_options = b'\340A\002'
  _GETINTEGRATIONREQUEST.fields_by_name['view']._options = None
  _GETINTEGRATIONREQUEST.fields_by_name['view']._serialized_options = b'\340A\001'
  _GETINTEGRATIONRESPONSE.fields_by_name['integration']._options = None
  _GETINTEGRATIONRESPONSE.fields_by_name['integration']._serialized_options = b'\340A\003'
  _globals['_CONNECTION']._serialized_start=227
  _globals['_CONNECTION']._serialized_end=995
  _globals['_CONNECTION_METHOD']._serialized_start=883
  _globals['_CONNECTION_METHOD']._serialized_end=956
  _globals['_LISTNAMESPACECONNECTIONSREQUEST']._serialized_start=998
  _globals['_LISTNAMESPACECONNECTIONSREQUEST']._serialized_end=1225
  _globals['_LISTNAMESPACECONNECTIONSRESPONSE']._serialized_start=1228
  _globals['_LISTNAMESPACECONNECTIONSRESPONSE']._serialized_end=1415
  _globals['_GETNAMESPACECONNECTIONREQUEST']._serialized_start=1418
  _globals['_GETNAMESPACECONNECTIONREQUEST']._serialized_end=1597
  _globals['_GETNAMESPACECONNECTIONRESPONSE']._serialized_start=1599
  _globals['_GETNAMESPACECONNECTIONRESPONSE']._serialized_end=1701
  _globals['_CREATENAMESPACECONNECTIONREQUEST']._serialized_start=1703
  _globals['_CREATENAMESPACECONNECTIONREQUEST']._serialized_end=1807
  _globals['_CREATENAMESPACECONNECTIONRESPONSE']._serialized_start=1809
  _globals['_CREATENAMESPACECONNECTIONRESPONSE']._serialized_end=1914
  _globals['_UPDATENAMESPACECONNECTIONREQUEST']._serialized_start=1917
  _globals['_UPDATENAMESPACECONNECTIONREQUEST']._serialized_end=2129
  _globals['_UPDATENAMESPACECONNECTIONRESPONSE']._serialized_start=2131
  _globals['_UPDATENAMESPACECONNECTIONRESPONSE']._serialized_end=2236
  _globals['_DELETENAMESPACECONNECTIONREQUEST']._serialized_start=2238
  _globals['_DELETENAMESPACECONNECTIONREQUEST']._serialized_end=2354
  _globals['_DELETENAMESPACECONNECTIONRESPONSE']._serialized_start=2356
  _globals['_DELETENAMESPACECONNECTIONRESPONSE']._serialized_end=2391
  _globals['_TESTNAMESPACECONNECTIONREQUEST']._serialized_start=2393
  _globals['_TESTNAMESPACECONNECTIONREQUEST']._serialized_end=2507
  _globals['_TESTNAMESPACECONNECTIONRESPONSE']._serialized_start=2509
  _globals['_TESTNAMESPACECONNECTIONRESPONSE']._serialized_end=2542
  _globals['_INTEGRATION']._serialized_start=2545
  _globals['_INTEGRATION']._serialized_end=3431
  _globals['_INTEGRATION_LINK']._serialized_start=3090
  _globals['_INTEGRATION_LINK']._serialized_end=3144
  _globals['_INTEGRATION_OAUTHCONFIG']._serialized_start=3146
  _globals['_INTEGRATION_OAUTHCONFIG']._serialized_end=3256
  _globals['_INTEGRATION_SETUPSCHEMA']._serialized_start=3259
  _globals['_INTEGRATION_SETUPSCHEMA']._serialized_end=3399
  _globals['_LISTPIPELINEIDSBYCONNECTIONIDREQUEST']._serialized_start=3434
  _globals['_LISTPIPELINEIDSBYCONNECTIONIDREQUEST']._serialized_end=3708
  _globals['_LISTPIPELINEIDSBYCONNECTIONIDRESPONSE']._serialized_start=3711
  _globals['_LISTPIPELINEIDSBYCONNECTIONIDRESPONSE']._serialized_end=3871
  _globals['_LISTINTEGRATIONSREQUEST']._serialized_start=3874
  _globals['_LISTINTEGRATIONSREQUEST']._serialized_end=4053
  _globals['_LISTINTEGRATIONSRESPONSE']._serialized_start=4056
  _globals['_LISTINTEGRATIONSRESPONSE']._serialized_end=4238
  _globals['_GETINTEGRATIONREQUEST']._serialized_start=4241
  _globals['_GETINTEGRATIONREQUEST']._serialized_end=4374
  _globals['_GETINTEGRATIONRESPONSE']._serialized_start=4376
  _globals['_GETINTEGRATIONRESPONSE']._serialized_end=4473
# @@protoc_insertion_point(module_scope)
