# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vdp/connector/v1alpha/spec.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from vdp.connector.v1alpha import auth_pb2 as vdp_dot_connector_dot_v1alpha_dot_auth__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n vdp/connector/v1alpha/spec.proto\x12\x15vdp.connector.v1alpha\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a vdp/connector/v1alpha/auth.proto\"\x81\x04\n\x04Spec\x12\x30\n\x11\x64ocumentation_url\x18\x04 \x01(\tB\x03\xe0\x41\x03R\x10\x64ocumentationUrl\x12W\n\x18\x63onnection_specification\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructB\x03\xe0\x41\x02R\x17\x63onnectionSpecification\x12\x36\n\x14supports_incremental\x18\x06 \x01(\x08\x42\x03\xe0\x41\x03R\x13supportsIncremental\x12:\n\x16supports_normalization\x18\x07 \x01(\x08\x42\x03\xe0\x41\x03R\x15supportsNormalization\x12&\n\x0csupports_dbt\x18\x08 \x01(\x08\x42\x03\xe0\x41\x03R\x0bsupportsDbt\x12\x82\x01\n supported_destination_sync_modes\x18\t \x03(\x0e\x32\x34.vdp.connector.v1alpha.SupportedDestinationSyncModesB\x03\xe0\x41\x03R\x1dsupportedDestinationSyncModes\x12M\n\radvanced_auth\x18\n \x01(\x0b\x32#.vdp.connector.v1alpha.AdvancedAuthB\x03\xe0\x41\x03R\x0c\x61\x64vancedAuth*\x87\x01\n\x12SupportedSyncModes\x12$\n SUPPORTED_SYNC_MODES_UNSPECIFIED\x10\x00\x12%\n!SUPPORTED_SYNC_MODES_FULL_REFRESH\x10\x01\x12$\n SUPPORTED_SYNC_MODES_INCREMENTAL\x10\x02*\xe1\x01\n\x1dSupportedDestinationSyncModes\x12\x30\n,SUPPORTED_DESTINATION_SYNC_MODES_UNSPECIFIED\x10\x00\x12+\n\'SUPPORTED_DESTINATION_SYNC_MODES_APPEND\x10\x01\x12.\n*SUPPORTED_DESTINATION_SYNC_MODES_OVERWRITE\x10\x02\x12\x31\n-SUPPORTED_DESTINATION_SYNC_MODES_APPEND_DEDUP\x10\x03\x42\xe6\x01\n\x19\x63om.vdp.connector.v1alphaB\tSpecProtoP\x01ZHgithub.com/instill-ai/protogen-go/vdp/connector/v1alpha;connectorv1alpha\xa2\x02\x03VCX\xaa\x02\x15Vdp.Connector.V1alpha\xca\x02\x15Vdp\\Connector\\V1alpha\xe2\x02!Vdp\\Connector\\V1alpha\\GPBMetadata\xea\x02\x17Vdp::Connector::V1alphab\x06proto3')

_SUPPORTEDSYNCMODES = DESCRIPTOR.enum_types_by_name['SupportedSyncModes']
SupportedSyncModes = enum_type_wrapper.EnumTypeWrapper(_SUPPORTEDSYNCMODES)
_SUPPORTEDDESTINATIONSYNCMODES = DESCRIPTOR.enum_types_by_name['SupportedDestinationSyncModes']
SupportedDestinationSyncModes = enum_type_wrapper.EnumTypeWrapper(_SUPPORTEDDESTINATIONSYNCMODES)
SUPPORTED_SYNC_MODES_UNSPECIFIED = 0
SUPPORTED_SYNC_MODES_FULL_REFRESH = 1
SUPPORTED_SYNC_MODES_INCREMENTAL = 2
SUPPORTED_DESTINATION_SYNC_MODES_UNSPECIFIED = 0
SUPPORTED_DESTINATION_SYNC_MODES_APPEND = 1
SUPPORTED_DESTINATION_SYNC_MODES_OVERWRITE = 2
SUPPORTED_DESTINATION_SYNC_MODES_APPEND_DEDUP = 3


_SPEC = DESCRIPTOR.message_types_by_name['Spec']
Spec = _reflection.GeneratedProtocolMessageType('Spec', (_message.Message,), {
  'DESCRIPTOR' : _SPEC,
  '__module__' : 'vdp.connector.v1alpha.spec_pb2'
  # @@protoc_insertion_point(class_scope:vdp.connector.v1alpha.Spec)
  })
_sym_db.RegisterMessage(Spec)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.vdp.connector.v1alphaB\tSpecProtoP\001ZHgithub.com/instill-ai/protogen-go/vdp/connector/v1alpha;connectorv1alpha\242\002\003VCX\252\002\025Vdp.Connector.V1alpha\312\002\025Vdp\\Connector\\V1alpha\342\002!Vdp\\Connector\\V1alpha\\GPBMetadata\352\002\027Vdp::Connector::V1alpha'
  _SPEC.fields_by_name['documentation_url']._options = None
  _SPEC.fields_by_name['documentation_url']._serialized_options = b'\340A\003'
  _SPEC.fields_by_name['connection_specification']._options = None
  _SPEC.fields_by_name['connection_specification']._serialized_options = b'\340A\002'
  _SPEC.fields_by_name['supports_incremental']._options = None
  _SPEC.fields_by_name['supports_incremental']._serialized_options = b'\340A\003'
  _SPEC.fields_by_name['supports_normalization']._options = None
  _SPEC.fields_by_name['supports_normalization']._serialized_options = b'\340A\003'
  _SPEC.fields_by_name['supports_dbt']._options = None
  _SPEC.fields_by_name['supports_dbt']._serialized_options = b'\340A\003'
  _SPEC.fields_by_name['supported_destination_sync_modes']._options = None
  _SPEC.fields_by_name['supported_destination_sync_modes']._serialized_options = b'\340A\003'
  _SPEC.fields_by_name['advanced_auth']._options = None
  _SPEC.fields_by_name['advanced_auth']._serialized_options = b'\340A\003'
  _SUPPORTEDSYNCMODES._serialized_start=673
  _SUPPORTEDSYNCMODES._serialized_end=808
  _SUPPORTEDDESTINATIONSYNCMODES._serialized_start=811
  _SUPPORTEDDESTINATIONSYNCMODES._serialized_end=1036
  _SPEC._serialized_start=157
  _SPEC._serialized_end=670
# @@protoc_insertion_point(module_scope)
