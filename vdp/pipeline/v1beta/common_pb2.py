# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vdp/pipeline/v1beta/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n vdp/pipeline/v1beta/common.proto\x12\x13vdp.pipeline.v1beta\"\xc7\x03\n\nPermission\x12@\n\x05users\x18\x01 \x03(\x0b\x32*.vdp.pipeline.v1beta.Permission.UsersEntryR\x05users\x12H\n\nshare_code\x18\x02 \x01(\x0b\x32).vdp.pipeline.v1beta.Permission.ShareCodeR\tshareCode\x1aO\n\x04User\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12-\n\x04role\x18\x04 \x01(\x0e\x32\x19.vdp.pipeline.v1beta.RoleR\x04role\x1a|\n\tShareCode\x12\x12\n\x04user\x18\x01 \x01(\tR\x04user\x12\x12\n\x04\x63ode\x18\x02 \x01(\tR\x04\x63ode\x12\x18\n\x07\x65nabled\x18\x03 \x01(\x08R\x07\x65nabled\x12-\n\x04role\x18\x04 \x01(\x0e\x32\x19.vdp.pipeline.v1beta.RoleR\x04role\x1a^\n\nUsersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12:\n\x05value\x18\x02 \x01(\x0b\x32$.vdp.pipeline.v1beta.Permission.UserR\x05value:\x02\x38\x01*@\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bROLE_VIEWER\x10\x01\x12\x11\n\rROLE_EXECUTOR\x10\x02\x42\xda\x01\n\x17\x63om.vdp.pipeline.v1betaB\x0b\x43ommonProtoP\x01ZDgithub.com/instill-ai/protogen-go/vdp/pipeline/v1beta;pipelinev1beta\xa2\x02\x03VPX\xaa\x02\x13Vdp.Pipeline.V1beta\xca\x02\x13Vdp\\Pipeline\\V1beta\xe2\x02\x1fVdp\\Pipeline\\V1beta\\GPBMetadata\xea\x02\x15Vdp::Pipeline::V1betab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vdp.pipeline.v1beta.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.vdp.pipeline.v1betaB\013CommonProtoP\001ZDgithub.com/instill-ai/protogen-go/vdp/pipeline/v1beta;pipelinev1beta\242\002\003VPX\252\002\023Vdp.Pipeline.V1beta\312\002\023Vdp\\Pipeline\\V1beta\342\002\037Vdp\\Pipeline\\V1beta\\GPBMetadata\352\002\025Vdp::Pipeline::V1beta'
  _PERMISSION_USERSENTRY._options = None
  _PERMISSION_USERSENTRY._serialized_options = b'8\001'
  _globals['_ROLE']._serialized_start=515
  _globals['_ROLE']._serialized_end=579
  _globals['_PERMISSION']._serialized_start=58
  _globals['_PERMISSION']._serialized_end=513
  _globals['_PERMISSION_USER']._serialized_start=212
  _globals['_PERMISSION_USER']._serialized_end=291
  _globals['_PERMISSION_SHARECODE']._serialized_start=293
  _globals['_PERMISSION_SHARECODE']._serialized_end=417
  _globals['_PERMISSION_USERSENTRY']._serialized_start=419
  _globals['_PERMISSION_USERSENTRY']._serialized_end=513
# @@protoc_insertion_point(module_scope)