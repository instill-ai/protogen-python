# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vdp/controller/v1beta/controller.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.healthcheck.v1beta import healthcheck_pb2 as common_dot_healthcheck_dot_v1beta_dot_healthcheck__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from vdp.pipeline.v1beta import connector_pb2 as vdp_dot_pipeline_dot_v1beta_dot_connector__pb2
from vdp.pipeline.v1beta import pipeline_pb2 as vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&vdp/controller/v1beta/controller.proto\x12\x15vdp.controller.v1beta\x1a+common/healthcheck/v1beta/healthcheck.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a#vdp/pipeline/v1beta/connector.proto\x1a\"vdp/pipeline/v1beta/pipeline.proto\"\x96\x01\n\x0fLivenessRequest\x12j\n\x14health_check_request\x18\x01 \x01(\x0b\x32-.common.healthcheck.v1beta.HealthCheckRequestB\x04\xe2\x41\x01\x01H\x00R\x12healthCheckRequest\x88\x01\x01\x42\x17\n\x15_health_check_request\"v\n\x10LivenessResponse\x12\x62\n\x15health_check_response\x18\x01 \x01(\x0b\x32..common.healthcheck.v1beta.HealthCheckResponseR\x13healthCheckResponse\"\x97\x01\n\x10ReadinessRequest\x12j\n\x14health_check_request\x18\x01 \x01(\x0b\x32-.common.healthcheck.v1beta.HealthCheckRequestB\x04\xe2\x41\x01\x01H\x00R\x12healthCheckRequest\x88\x01\x01\x42\x17\n\x15_health_check_request\"w\n\x11ReadinessResponse\x12\x62\n\x15health_check_response\x18\x01 \x01(\x0b\x32..common.healthcheck.v1beta.HealthCheckResponseR\x13healthCheckResponse\"\xbf\x03\n\x08Resource\x12\x33\n\x12resource_permalink\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x11resourcePermalink\x12\x43\n\x0epipeline_state\x18\x03 \x01(\x0e\x32\x1a.vdp.pipeline.v1beta.StateH\x00R\rpipelineState\x12O\n\x0f\x63onnector_state\x18\x04 \x01(\x0e\x32$.vdp.pipeline.v1beta.Connector.StateH\x00R\x0e\x63onnectorState\x12\x63\n\rbackend_state\x18\x05 \x01(\x0e\x32<.common.healthcheck.v1beta.HealthCheckResponse.ServingStatusH\x00R\x0c\x62\x61\x63kendState\x12%\n\x08progress\x18\x06 \x01(\x05\x42\x04\xe2\x41\x01\x01H\x01R\x08progress\x88\x01\x01:F\xea\x41\x43\n\x19\x61pi.instill.tech/Resource\x12&resources/{resource_uuid}/types/{type}B\x07\n\x05stateB\x0b\n\t_progress\"\x8b\x01\n\x12GetResourceRequest\x12u\n\x12resource_permalink\x18\x01 \x01(\tBF\x92\x41!\xca>\x1e\xfa\x02\x1bresource.resource_permalink\xe2\x41\x01\x02\xfa\x41\x1b\n\x19\x61pi.instill.tech/ResourceR\x11resourcePermalink\"R\n\x13GetResourceResponse\x12;\n\x08resource\x18\x01 \x01(\x0b\x32\x1f.vdp.controller.v1beta.ResourceR\x08resource\"\x96\x01\n\x15UpdateResourceRequest\x12\x41\n\x08resource\x18\x01 \x01(\x0b\x32\x1f.vdp.controller.v1beta.ResourceB\x04\xe2\x41\x01\x02R\x08resource\x12*\n\x0bworkflow_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01H\x00R\nworkflowId\x88\x01\x01\x42\x0e\n\x0c_workflow_id\"U\n\x16UpdateResourceResponse\x12;\n\x08resource\x18\x01 \x01(\x0b\x32\x1f.vdp.controller.v1beta.ResourceR\x08resource\"\x8e\x01\n\x15\x44\x65leteResourceRequest\x12u\n\x12resource_permalink\x18\x01 \x01(\tBF\x92\x41!\xca>\x1e\xfa\x02\x1bresource.resource_permalink\xe2\x41\x01\x02\xfa\x41\x1b\n\x19\x61pi.instill.tech/ResourceR\x11resourcePermalink\"\x18\n\x16\x44\x65leteResourceResponseB\xec\x01\n\x19\x63om.vdp.controller.v1betaB\x0f\x43ontrollerProtoP\x01ZHgithub.com/instill-ai/protogen-go/vdp/controller/v1beta;controllerv1beta\xa2\x02\x03VCX\xaa\x02\x15Vdp.Controller.V1beta\xca\x02\x15Vdp\\Controller\\V1beta\xe2\x02!Vdp\\Controller\\V1beta\\GPBMetadata\xea\x02\x17Vdp::Controller::V1betab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vdp.controller.v1beta.controller_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.vdp.controller.v1betaB\017ControllerProtoP\001ZHgithub.com/instill-ai/protogen-go/vdp/controller/v1beta;controllerv1beta\242\002\003VCX\252\002\025Vdp.Controller.V1beta\312\002\025Vdp\\Controller\\V1beta\342\002!Vdp\\Controller\\V1beta\\GPBMetadata\352\002\027Vdp::Controller::V1beta'
  _LIVENESSREQUEST.fields_by_name['health_check_request']._options = None
  _LIVENESSREQUEST.fields_by_name['health_check_request']._serialized_options = b'\342A\001\001'
  _READINESSREQUEST.fields_by_name['health_check_request']._options = None
  _READINESSREQUEST.fields_by_name['health_check_request']._serialized_options = b'\342A\001\001'
  _RESOURCE.fields_by_name['resource_permalink']._options = None
  _RESOURCE.fields_by_name['resource_permalink']._serialized_options = b'\342A\001\002'
  _RESOURCE.fields_by_name['progress']._options = None
  _RESOURCE.fields_by_name['progress']._serialized_options = b'\342A\001\001'
  _RESOURCE._options = None
  _RESOURCE._serialized_options = b'\352AC\n\031api.instill.tech/Resource\022&resources/{resource_uuid}/types/{type}'
  _GETRESOURCEREQUEST.fields_by_name['resource_permalink']._options = None
  _GETRESOURCEREQUEST.fields_by_name['resource_permalink']._serialized_options = b'\222A!\312>\036\372\002\033resource.resource_permalink\342A\001\002\372A\033\n\031api.instill.tech/Resource'
  _UPDATERESOURCEREQUEST.fields_by_name['resource']._options = None
  _UPDATERESOURCEREQUEST.fields_by_name['resource']._serialized_options = b'\342A\001\002'
  _UPDATERESOURCEREQUEST.fields_by_name['workflow_id']._options = None
  _UPDATERESOURCEREQUEST.fields_by_name['workflow_id']._serialized_options = b'\342A\001\001'
  _DELETERESOURCEREQUEST.fields_by_name['resource_permalink']._options = None
  _DELETERESOURCEREQUEST.fields_by_name['resource_permalink']._serialized_options = b'\222A!\312>\036\372\002\033resource.resource_permalink\342A\001\002\372A\033\n\031api.instill.tech/Resource'
  _globals['_LIVENESSREQUEST']._serialized_start=292
  _globals['_LIVENESSREQUEST']._serialized_end=442
  _globals['_LIVENESSRESPONSE']._serialized_start=444
  _globals['_LIVENESSRESPONSE']._serialized_end=562
  _globals['_READINESSREQUEST']._serialized_start=565
  _globals['_READINESSREQUEST']._serialized_end=716
  _globals['_READINESSRESPONSE']._serialized_start=718
  _globals['_READINESSRESPONSE']._serialized_end=837
  _globals['_RESOURCE']._serialized_start=840
  _globals['_RESOURCE']._serialized_end=1287
  _globals['_GETRESOURCEREQUEST']._serialized_start=1290
  _globals['_GETRESOURCEREQUEST']._serialized_end=1429
  _globals['_GETRESOURCERESPONSE']._serialized_start=1431
  _globals['_GETRESOURCERESPONSE']._serialized_end=1513
  _globals['_UPDATERESOURCEREQUEST']._serialized_start=1516
  _globals['_UPDATERESOURCEREQUEST']._serialized_end=1666
  _globals['_UPDATERESOURCERESPONSE']._serialized_start=1668
  _globals['_UPDATERESOURCERESPONSE']._serialized_end=1753
  _globals['_DELETERESOURCEREQUEST']._serialized_start=1756
  _globals['_DELETERESOURCEREQUEST']._serialized_end=1898
  _globals['_DELETERESOURCERESPONSE']._serialized_start=1900
  _globals['_DELETERESOURCERESPONSE']._serialized_end=1924
# @@protoc_insertion_point(module_scope)