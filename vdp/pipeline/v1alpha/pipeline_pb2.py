# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vdp/pipeline/v1alpha/pipeline.proto
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
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#vdp/pipeline/v1alpha/pipeline.proto\x12\x14vdp.pipeline.v1alpha\x1a\x1cgoogle/protobuf/struct.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/api/field_behavior.proto\"\xdb\x01\n\x06Recipe\x12:\n\x06source\x18\x01 \x01(\tB\"\xe0\x41\x05\xfa\x41\x1c\n\x1a\x61pi.instill.tech/ConnectorR\x06source\x12\x44\n\x0b\x64\x65stination\x18\x02 \x01(\tB\"\xe0\x41\x05\xfa\x41\x1c\n\x1a\x61pi.instill.tech/ConnectorR\x0b\x64\x65stination\x12O\n\x0fmodel_instances\x18\x03 \x03(\tB&\xe0\x41\x05\xfa\x41 \n\x1e\x61pi.instill.tech/ModelInstanceR\x0emodelInstances\"\x8c\x06\n\x08Pipeline\x12\x17\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x04name\x12\x15\n\x03uid\x18\x02 \x01(\tB\x03\xe0\x41\x03R\x03uid\x12\x13\n\x02id\x18\x03 \x01(\tB\x03\xe0\x41\x05R\x02id\x12*\n\x0b\x64\x65scription\x18\x04 \x01(\tB\x03\xe0\x41\x01H\x01R\x0b\x64\x65scription\x88\x01\x01\x12\x39\n\x06recipe\x18\x05 \x01(\x0b\x32\x1c.vdp.pipeline.v1alpha.RecipeB\x03\xe0\x41\x05R\x06recipe\x12<\n\x04mode\x18\x06 \x01(\x0e\x32#.vdp.pipeline.v1alpha.Pipeline.ModeB\x03\xe0\x41\x03R\x04mode\x12?\n\x05state\x18\x07 \x01(\x0e\x32$.vdp.pipeline.v1alpha.Pipeline.StateB\x03\xe0\x41\x03R\x05state\x12\x33\n\x04user\x18\x08 \x01(\tB\x1d\xe0\x41\x03\xfa\x41\x17\n\x15\x61pi.instill.tech/UserH\x00R\x04user\x12\x39\n\x03org\x18\t \x01(\tB%\xe0\x41\x03\xfa\x41\x1f\n\x1d\x61pi.instill.tech/OrganizationH\x00R\x03org\x12@\n\x0b\x63reate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\ncreateTime\x12@\n\x0bupdate_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\nupdateTime\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\r\n\tMODE_SYNC\x10\x01\x12\x0e\n\nMODE_ASYNC\x10\x02\"U\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x12\n\x0eSTATE_INACTIVE\x10\x01\x12\x10\n\x0cSTATE_ACTIVE\x10\x02\x12\x0f\n\x0bSTATE_ERROR\x10\x03:4\xea\x41\x31\n\x19\x61pi.instill.tech/Pipeline\x12\x14pipelines/{pipeline}B\x07\n\x05ownerB\x0e\n\x0c_description\"X\n\x15\x43reatePipelineRequest\x12?\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.vdp.pipeline.v1alpha.PipelineB\x03\xe0\x41\x02R\x08pipeline\"T\n\x16\x43reatePipelineResponse\x12:\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.vdp.pipeline.v1alpha.PipelineR\x08pipeline\"\xf2\x01\n\x13ListPipelineRequest\x12%\n\tpage_size\x18\x01 \x01(\x03\x42\x03\xe0\x41\x01H\x00R\x08pageSize\x88\x01\x01\x12\'\n\npage_token\x18\x02 \x01(\tB\x03\xe0\x41\x01H\x01R\tpageToken\x88\x01\x01\x12\x38\n\x04view\x18\x03 \x01(\x0e\x32\x1a.vdp.pipeline.v1alpha.ViewB\x03\xe0\x41\x01H\x02R\x04view\x88\x01\x01\x12 \n\x06\x66ilter\x18\x04 \x01(\tB\x03\xe0\x41\x01H\x03R\x06\x66ilter\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\x07\n\x05_viewB\t\n\x07_filter\"\x9b\x01\n\x14ListPipelineResponse\x12<\n\tpipelines\x18\x01 \x03(\x0b\x32\x1e.vdp.pipeline.v1alpha.PipelineR\tpipelines\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12\x1d\n\ntotal_size\x18\x03 \x01(\x03R\ttotalSize\"\xa4\x01\n\x12GetPipelineRequest\x12K\n\x04name\x18\x01 \x01(\tB7\xe0\x41\x02\xfa\x41\x1b\n\x19\x61pi.instill.tech/Pipeline\x92\x41\x13\xca>\x10\xfa\x02\rpipeline.nameR\x04name\x12\x38\n\x04view\x18\x02 \x01(\x0e\x32\x1a.vdp.pipeline.v1alpha.ViewB\x03\xe0\x41\x01H\x00R\x04view\x88\x01\x01\x42\x07\n\x05_view\"Q\n\x13GetPipelineResponse\x12:\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.vdp.pipeline.v1alpha.PipelineR\x08pipeline\"\x9a\x01\n\x15UpdatePipelineRequest\x12?\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.vdp.pipeline.v1alpha.PipelineB\x03\xe0\x41\x02R\x08pipeline\x12@\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x02R\nupdateMask\"T\n\x16UpdatePipelineResponse\x12:\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.vdp.pipeline.v1alpha.PipelineR\x08pipeline\"d\n\x15\x44\x65letePipelineRequest\x12K\n\x04name\x18\x01 \x01(\tB7\xe0\x41\x02\xfa\x41\x1b\n\x19\x61pi.instill.tech/Pipeline\x92\x41\x13\xca>\x10\xfa\x02\rpipeline.nameR\x04name\"\x18\n\x16\x44\x65letePipelineResponse\"}\n\x15LookUpPipelineRequest\x12!\n\tpermalink\x18\x01 \x01(\tB\x03\xe0\x41\x02R\tpermalink\x12\x38\n\x04view\x18\x02 \x01(\x0e\x32\x1a.vdp.pipeline.v1alpha.ViewB\x03\xe0\x41\x01H\x00R\x04view\x88\x01\x01\x42\x07\n\x05_view\"T\n\x16LookUpPipelineResponse\x12:\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.vdp.pipeline.v1alpha.PipelineR\x08pipeline\"P\n\x17\x41\x63tivatePipelineRequest\x12\x35\n\x04name\x18\x01 \x01(\tB!\xe0\x41\x02\xfa\x41\x1b\n\x19\x61pi.instill.tech/PipelineR\x04name\"V\n\x18\x41\x63tivatePipelineResponse\x12:\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.vdp.pipeline.v1alpha.PipelineR\x08pipeline\"R\n\x19\x44\x65\x61\x63tivatePipelineRequest\x12\x35\n\x04name\x18\x01 \x01(\tB!\xe0\x41\x02\xfa\x41\x1b\n\x19\x61pi.instill.tech/PipelineR\x04name\"X\n\x1a\x44\x65\x61\x63tivatePipelineResponse\x12:\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.vdp.pipeline.v1alpha.PipelineR\x08pipeline\"{\n\x15RenamePipelineRequest\x12\x35\n\x04name\x18\x01 \x01(\tB!\xe0\x41\x02\xfa\x41\x1b\n\x19\x61pi.instill.tech/PipelineR\x04name\x12+\n\x0fnew_pipeline_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\rnewPipelineId\"T\n\x16RenamePipelineResponse\x12:\n\x08pipeline\x18\x01 \x01(\x0b\x32\x1e.vdp.pipeline.v1alpha.PipelineR\x08pipeline\"S\n\x05Input\x12\x1d\n\timage_url\x18\x01 \x01(\tH\x00R\x08imageUrl\x12#\n\x0cimage_base64\x18\x02 \x01(\tH\x00R\x0bimageBase64B\x06\n\x04type\"\x89\x01\n\x16TriggerPipelineRequest\x12\x35\n\x04name\x18\x01 \x01(\tB!\xe0\x41\x02\xfa\x41\x1b\n\x19\x61pi.instill.tech/PipelineR\x04name\x12\x38\n\x06inputs\x18\x02 \x03(\x0b\x32\x1b.vdp.pipeline.v1alpha.InputB\x03\xe0\x41\x02R\x06inputs\"J\n\x17TriggerPipelineResponse\x12/\n\x06output\x18\x01 \x01(\x0b\x32\x17.google.protobuf.StructR\x06output\"\xa2\x01\n&TriggerPipelineBinaryFileUploadRequest\x12\x35\n\x04name\x18\x01 \x01(\tB!\xe0\x41\x02\xfa\x41\x1b\n\x19\x61pi.instill.tech/PipelineR\x04name\x12&\n\x0c\x66ile_lengths\x18\x02 \x03(\x04\x42\x03\xe0\x41\x02R\x0b\x66ileLengths\x12\x19\n\x05\x62ytes\x18\x03 \x01(\x0c\x42\x03\xe0\x41\x02R\x05\x62ytes\"Z\n\'TriggerPipelineBinaryFileUploadResponse\x12/\n\x06output\x18\x01 \x01(\x0b\x32\x17.google.protobuf.StructR\x06output*;\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\x0e\n\nVIEW_BASIC\x10\x01\x12\r\n\tVIEW_FULL\x10\x02\x42\xe3\x01\n\x18\x63om.vdp.pipeline.v1alphaB\rPipelineProtoP\x01ZFgithub.com/instill-ai/protogen-go/vdp/pipeline/v1alpha;pipelinev1alpha\xa2\x02\x03VPX\xaa\x02\x14Vdp.Pipeline.V1alpha\xca\x02\x14Vdp\\Pipeline\\V1alpha\xe2\x02 Vdp\\Pipeline\\V1alpha\\GPBMetadata\xea\x02\x16Vdp::Pipeline::V1alphab\x06proto3')

_VIEW = DESCRIPTOR.enum_types_by_name['View']
View = enum_type_wrapper.EnumTypeWrapper(_VIEW)
VIEW_UNSPECIFIED = 0
VIEW_BASIC = 1
VIEW_FULL = 2


_RECIPE = DESCRIPTOR.message_types_by_name['Recipe']
_PIPELINE = DESCRIPTOR.message_types_by_name['Pipeline']
_CREATEPIPELINEREQUEST = DESCRIPTOR.message_types_by_name['CreatePipelineRequest']
_CREATEPIPELINERESPONSE = DESCRIPTOR.message_types_by_name['CreatePipelineResponse']
_LISTPIPELINEREQUEST = DESCRIPTOR.message_types_by_name['ListPipelineRequest']
_LISTPIPELINERESPONSE = DESCRIPTOR.message_types_by_name['ListPipelineResponse']
_GETPIPELINEREQUEST = DESCRIPTOR.message_types_by_name['GetPipelineRequest']
_GETPIPELINERESPONSE = DESCRIPTOR.message_types_by_name['GetPipelineResponse']
_UPDATEPIPELINEREQUEST = DESCRIPTOR.message_types_by_name['UpdatePipelineRequest']
_UPDATEPIPELINERESPONSE = DESCRIPTOR.message_types_by_name['UpdatePipelineResponse']
_DELETEPIPELINEREQUEST = DESCRIPTOR.message_types_by_name['DeletePipelineRequest']
_DELETEPIPELINERESPONSE = DESCRIPTOR.message_types_by_name['DeletePipelineResponse']
_LOOKUPPIPELINEREQUEST = DESCRIPTOR.message_types_by_name['LookUpPipelineRequest']
_LOOKUPPIPELINERESPONSE = DESCRIPTOR.message_types_by_name['LookUpPipelineResponse']
_ACTIVATEPIPELINEREQUEST = DESCRIPTOR.message_types_by_name['ActivatePipelineRequest']
_ACTIVATEPIPELINERESPONSE = DESCRIPTOR.message_types_by_name['ActivatePipelineResponse']
_DEACTIVATEPIPELINEREQUEST = DESCRIPTOR.message_types_by_name['DeactivatePipelineRequest']
_DEACTIVATEPIPELINERESPONSE = DESCRIPTOR.message_types_by_name['DeactivatePipelineResponse']
_RENAMEPIPELINEREQUEST = DESCRIPTOR.message_types_by_name['RenamePipelineRequest']
_RENAMEPIPELINERESPONSE = DESCRIPTOR.message_types_by_name['RenamePipelineResponse']
_INPUT = DESCRIPTOR.message_types_by_name['Input']
_TRIGGERPIPELINEREQUEST = DESCRIPTOR.message_types_by_name['TriggerPipelineRequest']
_TRIGGERPIPELINERESPONSE = DESCRIPTOR.message_types_by_name['TriggerPipelineResponse']
_TRIGGERPIPELINEBINARYFILEUPLOADREQUEST = DESCRIPTOR.message_types_by_name['TriggerPipelineBinaryFileUploadRequest']
_TRIGGERPIPELINEBINARYFILEUPLOADRESPONSE = DESCRIPTOR.message_types_by_name['TriggerPipelineBinaryFileUploadResponse']
_PIPELINE_MODE = _PIPELINE.enum_types_by_name['Mode']
_PIPELINE_STATE = _PIPELINE.enum_types_by_name['State']
Recipe = _reflection.GeneratedProtocolMessageType('Recipe', (_message.Message,), {
  'DESCRIPTOR' : _RECIPE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.Recipe)
  })
_sym_db.RegisterMessage(Recipe)

Pipeline = _reflection.GeneratedProtocolMessageType('Pipeline', (_message.Message,), {
  'DESCRIPTOR' : _PIPELINE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.Pipeline)
  })
_sym_db.RegisterMessage(Pipeline)

CreatePipelineRequest = _reflection.GeneratedProtocolMessageType('CreatePipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPIPELINEREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.CreatePipelineRequest)
  })
_sym_db.RegisterMessage(CreatePipelineRequest)

CreatePipelineResponse = _reflection.GeneratedProtocolMessageType('CreatePipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPIPELINERESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.CreatePipelineResponse)
  })
_sym_db.RegisterMessage(CreatePipelineResponse)

ListPipelineRequest = _reflection.GeneratedProtocolMessageType('ListPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPIPELINEREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.ListPipelineRequest)
  })
_sym_db.RegisterMessage(ListPipelineRequest)

ListPipelineResponse = _reflection.GeneratedProtocolMessageType('ListPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPIPELINERESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.ListPipelineResponse)
  })
_sym_db.RegisterMessage(ListPipelineResponse)

GetPipelineRequest = _reflection.GeneratedProtocolMessageType('GetPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPIPELINEREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.GetPipelineRequest)
  })
_sym_db.RegisterMessage(GetPipelineRequest)

GetPipelineResponse = _reflection.GeneratedProtocolMessageType('GetPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPIPELINERESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.GetPipelineResponse)
  })
_sym_db.RegisterMessage(GetPipelineResponse)

UpdatePipelineRequest = _reflection.GeneratedProtocolMessageType('UpdatePipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPIPELINEREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.UpdatePipelineRequest)
  })
_sym_db.RegisterMessage(UpdatePipelineRequest)

UpdatePipelineResponse = _reflection.GeneratedProtocolMessageType('UpdatePipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPIPELINERESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.UpdatePipelineResponse)
  })
_sym_db.RegisterMessage(UpdatePipelineResponse)

DeletePipelineRequest = _reflection.GeneratedProtocolMessageType('DeletePipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPIPELINEREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.DeletePipelineRequest)
  })
_sym_db.RegisterMessage(DeletePipelineRequest)

DeletePipelineResponse = _reflection.GeneratedProtocolMessageType('DeletePipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPIPELINERESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.DeletePipelineResponse)
  })
_sym_db.RegisterMessage(DeletePipelineResponse)

LookUpPipelineRequest = _reflection.GeneratedProtocolMessageType('LookUpPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOOKUPPIPELINEREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.LookUpPipelineRequest)
  })
_sym_db.RegisterMessage(LookUpPipelineRequest)

LookUpPipelineResponse = _reflection.GeneratedProtocolMessageType('LookUpPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOOKUPPIPELINERESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.LookUpPipelineResponse)
  })
_sym_db.RegisterMessage(LookUpPipelineResponse)

ActivatePipelineRequest = _reflection.GeneratedProtocolMessageType('ActivatePipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATEPIPELINEREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.ActivatePipelineRequest)
  })
_sym_db.RegisterMessage(ActivatePipelineRequest)

ActivatePipelineResponse = _reflection.GeneratedProtocolMessageType('ActivatePipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATEPIPELINERESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.ActivatePipelineResponse)
  })
_sym_db.RegisterMessage(ActivatePipelineResponse)

DeactivatePipelineRequest = _reflection.GeneratedProtocolMessageType('DeactivatePipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEACTIVATEPIPELINEREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.DeactivatePipelineRequest)
  })
_sym_db.RegisterMessage(DeactivatePipelineRequest)

DeactivatePipelineResponse = _reflection.GeneratedProtocolMessageType('DeactivatePipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEACTIVATEPIPELINERESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.DeactivatePipelineResponse)
  })
_sym_db.RegisterMessage(DeactivatePipelineResponse)

RenamePipelineRequest = _reflection.GeneratedProtocolMessageType('RenamePipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _RENAMEPIPELINEREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.RenamePipelineRequest)
  })
_sym_db.RegisterMessage(RenamePipelineRequest)

RenamePipelineResponse = _reflection.GeneratedProtocolMessageType('RenamePipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _RENAMEPIPELINERESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.RenamePipelineResponse)
  })
_sym_db.RegisterMessage(RenamePipelineResponse)

Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.Input)
  })
_sym_db.RegisterMessage(Input)

TriggerPipelineRequest = _reflection.GeneratedProtocolMessageType('TriggerPipelineRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERPIPELINEREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.TriggerPipelineRequest)
  })
_sym_db.RegisterMessage(TriggerPipelineRequest)

TriggerPipelineResponse = _reflection.GeneratedProtocolMessageType('TriggerPipelineResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERPIPELINERESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.TriggerPipelineResponse)
  })
_sym_db.RegisterMessage(TriggerPipelineResponse)

TriggerPipelineBinaryFileUploadRequest = _reflection.GeneratedProtocolMessageType('TriggerPipelineBinaryFileUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERPIPELINEBINARYFILEUPLOADREQUEST,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.TriggerPipelineBinaryFileUploadRequest)
  })
_sym_db.RegisterMessage(TriggerPipelineBinaryFileUploadRequest)

TriggerPipelineBinaryFileUploadResponse = _reflection.GeneratedProtocolMessageType('TriggerPipelineBinaryFileUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGERPIPELINEBINARYFILEUPLOADRESPONSE,
  '__module__' : 'vdp.pipeline.v1alpha.pipeline_pb2'
  # @@protoc_insertion_point(class_scope:vdp.pipeline.v1alpha.TriggerPipelineBinaryFileUploadResponse)
  })
_sym_db.RegisterMessage(TriggerPipelineBinaryFileUploadResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.vdp.pipeline.v1alphaB\rPipelineProtoP\001ZFgithub.com/instill-ai/protogen-go/vdp/pipeline/v1alpha;pipelinev1alpha\242\002\003VPX\252\002\024Vdp.Pipeline.V1alpha\312\002\024Vdp\\Pipeline\\V1alpha\342\002 Vdp\\Pipeline\\V1alpha\\GPBMetadata\352\002\026Vdp::Pipeline::V1alpha'
  _RECIPE.fields_by_name['source']._options = None
  _RECIPE.fields_by_name['source']._serialized_options = b'\340A\005\372A\034\n\032api.instill.tech/Connector'
  _RECIPE.fields_by_name['destination']._options = None
  _RECIPE.fields_by_name['destination']._serialized_options = b'\340A\005\372A\034\n\032api.instill.tech/Connector'
  _RECIPE.fields_by_name['model_instances']._options = None
  _RECIPE.fields_by_name['model_instances']._serialized_options = b'\340A\005\372A \n\036api.instill.tech/ModelInstance'
  _PIPELINE.fields_by_name['name']._options = None
  _PIPELINE.fields_by_name['name']._serialized_options = b'\340A\003'
  _PIPELINE.fields_by_name['uid']._options = None
  _PIPELINE.fields_by_name['uid']._serialized_options = b'\340A\003'
  _PIPELINE.fields_by_name['id']._options = None
  _PIPELINE.fields_by_name['id']._serialized_options = b'\340A\005'
  _PIPELINE.fields_by_name['description']._options = None
  _PIPELINE.fields_by_name['description']._serialized_options = b'\340A\001'
  _PIPELINE.fields_by_name['recipe']._options = None
  _PIPELINE.fields_by_name['recipe']._serialized_options = b'\340A\005'
  _PIPELINE.fields_by_name['mode']._options = None
  _PIPELINE.fields_by_name['mode']._serialized_options = b'\340A\003'
  _PIPELINE.fields_by_name['state']._options = None
  _PIPELINE.fields_by_name['state']._serialized_options = b'\340A\003'
  _PIPELINE.fields_by_name['user']._options = None
  _PIPELINE.fields_by_name['user']._serialized_options = b'\340A\003\372A\027\n\025api.instill.tech/User'
  _PIPELINE.fields_by_name['org']._options = None
  _PIPELINE.fields_by_name['org']._serialized_options = b'\340A\003\372A\037\n\035api.instill.tech/Organization'
  _PIPELINE.fields_by_name['create_time']._options = None
  _PIPELINE.fields_by_name['create_time']._serialized_options = b'\340A\003'
  _PIPELINE.fields_by_name['update_time']._options = None
  _PIPELINE.fields_by_name['update_time']._serialized_options = b'\340A\003'
  _PIPELINE._options = None
  _PIPELINE._serialized_options = b'\352A1\n\031api.instill.tech/Pipeline\022\024pipelines/{pipeline}'
  _CREATEPIPELINEREQUEST.fields_by_name['pipeline']._options = None
  _CREATEPIPELINEREQUEST.fields_by_name['pipeline']._serialized_options = b'\340A\002'
  _LISTPIPELINEREQUEST.fields_by_name['page_size']._options = None
  _LISTPIPELINEREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTPIPELINEREQUEST.fields_by_name['page_token']._options = None
  _LISTPIPELINEREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _LISTPIPELINEREQUEST.fields_by_name['view']._options = None
  _LISTPIPELINEREQUEST.fields_by_name['view']._serialized_options = b'\340A\001'
  _LISTPIPELINEREQUEST.fields_by_name['filter']._options = None
  _LISTPIPELINEREQUEST.fields_by_name['filter']._serialized_options = b'\340A\001'
  _GETPIPELINEREQUEST.fields_by_name['name']._options = None
  _GETPIPELINEREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\033\n\031api.instill.tech/Pipeline\222A\023\312>\020\372\002\rpipeline.name'
  _GETPIPELINEREQUEST.fields_by_name['view']._options = None
  _GETPIPELINEREQUEST.fields_by_name['view']._serialized_options = b'\340A\001'
  _UPDATEPIPELINEREQUEST.fields_by_name['pipeline']._options = None
  _UPDATEPIPELINEREQUEST.fields_by_name['pipeline']._serialized_options = b'\340A\002'
  _UPDATEPIPELINEREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEPIPELINEREQUEST.fields_by_name['update_mask']._serialized_options = b'\340A\002'
  _DELETEPIPELINEREQUEST.fields_by_name['name']._options = None
  _DELETEPIPELINEREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\033\n\031api.instill.tech/Pipeline\222A\023\312>\020\372\002\rpipeline.name'
  _LOOKUPPIPELINEREQUEST.fields_by_name['permalink']._options = None
  _LOOKUPPIPELINEREQUEST.fields_by_name['permalink']._serialized_options = b'\340A\002'
  _LOOKUPPIPELINEREQUEST.fields_by_name['view']._options = None
  _LOOKUPPIPELINEREQUEST.fields_by_name['view']._serialized_options = b'\340A\001'
  _ACTIVATEPIPELINEREQUEST.fields_by_name['name']._options = None
  _ACTIVATEPIPELINEREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\033\n\031api.instill.tech/Pipeline'
  _DEACTIVATEPIPELINEREQUEST.fields_by_name['name']._options = None
  _DEACTIVATEPIPELINEREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\033\n\031api.instill.tech/Pipeline'
  _RENAMEPIPELINEREQUEST.fields_by_name['name']._options = None
  _RENAMEPIPELINEREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\033\n\031api.instill.tech/Pipeline'
  _RENAMEPIPELINEREQUEST.fields_by_name['new_pipeline_id']._options = None
  _RENAMEPIPELINEREQUEST.fields_by_name['new_pipeline_id']._serialized_options = b'\340A\002'
  _TRIGGERPIPELINEREQUEST.fields_by_name['name']._options = None
  _TRIGGERPIPELINEREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\033\n\031api.instill.tech/Pipeline'
  _TRIGGERPIPELINEREQUEST.fields_by_name['inputs']._options = None
  _TRIGGERPIPELINEREQUEST.fields_by_name['inputs']._serialized_options = b'\340A\002'
  _TRIGGERPIPELINEBINARYFILEUPLOADREQUEST.fields_by_name['name']._options = None
  _TRIGGERPIPELINEBINARYFILEUPLOADREQUEST.fields_by_name['name']._serialized_options = b'\340A\002\372A\033\n\031api.instill.tech/Pipeline'
  _TRIGGERPIPELINEBINARYFILEUPLOADREQUEST.fields_by_name['file_lengths']._options = None
  _TRIGGERPIPELINEBINARYFILEUPLOADREQUEST.fields_by_name['file_lengths']._serialized_options = b'\340A\002'
  _TRIGGERPIPELINEBINARYFILEUPLOADREQUEST.fields_by_name['bytes']._options = None
  _TRIGGERPIPELINEBINARYFILEUPLOADREQUEST.fields_by_name['bytes']._serialized_options = b'\340A\002'
  _VIEW._serialized_start=3797
  _VIEW._serialized_end=3856
  _RECIPE._serialized_start=267
  _RECIPE._serialized_end=486
  _PIPELINE._serialized_start=489
  _PIPELINE._serialized_end=1269
  _PIPELINE_MODE._serialized_start=1044
  _PIPELINE_MODE._serialized_end=1103
  _PIPELINE_STATE._serialized_start=1105
  _PIPELINE_STATE._serialized_end=1190
  _CREATEPIPELINEREQUEST._serialized_start=1271
  _CREATEPIPELINEREQUEST._serialized_end=1359
  _CREATEPIPELINERESPONSE._serialized_start=1361
  _CREATEPIPELINERESPONSE._serialized_end=1445
  _LISTPIPELINEREQUEST._serialized_start=1448
  _LISTPIPELINEREQUEST._serialized_end=1690
  _LISTPIPELINERESPONSE._serialized_start=1693
  _LISTPIPELINERESPONSE._serialized_end=1848
  _GETPIPELINEREQUEST._serialized_start=1851
  _GETPIPELINEREQUEST._serialized_end=2015
  _GETPIPELINERESPONSE._serialized_start=2017
  _GETPIPELINERESPONSE._serialized_end=2098
  _UPDATEPIPELINEREQUEST._serialized_start=2101
  _UPDATEPIPELINEREQUEST._serialized_end=2255
  _UPDATEPIPELINERESPONSE._serialized_start=2257
  _UPDATEPIPELINERESPONSE._serialized_end=2341
  _DELETEPIPELINEREQUEST._serialized_start=2343
  _DELETEPIPELINEREQUEST._serialized_end=2443
  _DELETEPIPELINERESPONSE._serialized_start=2445
  _DELETEPIPELINERESPONSE._serialized_end=2469
  _LOOKUPPIPELINEREQUEST._serialized_start=2471
  _LOOKUPPIPELINEREQUEST._serialized_end=2596
  _LOOKUPPIPELINERESPONSE._serialized_start=2598
  _LOOKUPPIPELINERESPONSE._serialized_end=2682
  _ACTIVATEPIPELINEREQUEST._serialized_start=2684
  _ACTIVATEPIPELINEREQUEST._serialized_end=2764
  _ACTIVATEPIPELINERESPONSE._serialized_start=2766
  _ACTIVATEPIPELINERESPONSE._serialized_end=2852
  _DEACTIVATEPIPELINEREQUEST._serialized_start=2854
  _DEACTIVATEPIPELINEREQUEST._serialized_end=2936
  _DEACTIVATEPIPELINERESPONSE._serialized_start=2938
  _DEACTIVATEPIPELINERESPONSE._serialized_end=3026
  _RENAMEPIPELINEREQUEST._serialized_start=3028
  _RENAMEPIPELINEREQUEST._serialized_end=3151
  _RENAMEPIPELINERESPONSE._serialized_start=3153
  _RENAMEPIPELINERESPONSE._serialized_end=3237
  _INPUT._serialized_start=3239
  _INPUT._serialized_end=3322
  _TRIGGERPIPELINEREQUEST._serialized_start=3325
  _TRIGGERPIPELINEREQUEST._serialized_end=3462
  _TRIGGERPIPELINERESPONSE._serialized_start=3464
  _TRIGGERPIPELINERESPONSE._serialized_end=3538
  _TRIGGERPIPELINEBINARYFILEUPLOADREQUEST._serialized_start=3541
  _TRIGGERPIPELINEBINARYFILEUPLOADREQUEST._serialized_end=3703
  _TRIGGERPIPELINEBINARYFILEUPLOADRESPONSE._serialized_start=3705
  _TRIGGERPIPELINEBINARYFILEUPLOADRESPONSE._serialized_end=3795
# @@protoc_insertion_point(module_scope)