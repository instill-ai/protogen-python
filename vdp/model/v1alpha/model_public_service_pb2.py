# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vdp/model/v1alpha/model_public_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from vdp.model.v1alpha import healthcheck_pb2 as vdp_dot_model_dot_v1alpha_dot_healthcheck__pb2
from vdp.model.v1alpha import model_definition_pb2 as vdp_dot_model_dot_v1alpha_dot_model__definition__pb2
from vdp.model.v1alpha import model_pb2 as vdp_dot_model_dot_v1alpha_dot_model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,vdp/model/v1alpha/model_public_service.proto\x12\x11vdp.model.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a#vdp/model/v1alpha/healthcheck.proto\x1a(vdp/model/v1alpha/model_definition.proto\x1a\x1dvdp/model/v1alpha/model.proto2\xb7\"\n\x12ModelPublicService\x12\x89\x01\n\x08Liveness\x12\".vdp.model.v1alpha.LivenessRequest\x1a#.vdp.model.v1alpha.LivenessResponse\"4\x82\xd3\xe4\x93\x02.Z\x17\x12\x15/v1alpha/health/model\x12\x13/v1alpha/__liveness\x12\x8c\x01\n\tReadiness\x12#.vdp.model.v1alpha.ReadinessRequest\x1a$.vdp.model.v1alpha.ReadinessResponse\"4\x82\xd3\xe4\x93\x02.Z\x16\x12\x14/v1alpha/ready/model\x12\x14/v1alpha/__readiness\x12\x98\x01\n\x13ListModelDefinition\x12-.vdp.model.v1alpha.ListModelDefinitionRequest\x1a..vdp.model.v1alpha.ListModelDefinitionResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1alpha/model-definitions\x12\xa5\x01\n\x12GetModelDefinition\x12,.vdp.model.v1alpha.GetModelDefinitionRequest\x1a-.vdp.model.v1alpha.GetModelDefinitionResponse\"2\xda\x41\x04name\x82\xd3\xe4\x93\x02%\x12#/v1alpha/{name=model-definitions/*}\x12o\n\tListModel\x12#.vdp.model.v1alpha.ListModelRequest\x1a$.vdp.model.v1alpha.ListModelResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1alpha/models\x12\x84\x01\n\x0b\x43reateModel\x12%.vdp.model.v1alpha.CreateModelRequest\x1a&.vdp.model.v1alpha.CreateModelResponse\"&\xda\x41\x05model\x82\xd3\xe4\x93\x02\x18:\x05model\"\x0f/v1alpha/models\x12\xae\x01\n\x1b\x43reateModelBinaryFileUpload\x12\x35.vdp.model.v1alpha.CreateModelBinaryFileUploadRequest\x1a\x36.vdp.model.v1alpha.CreateModelBinaryFileUploadResponse\"\x1e\xda\x41\x1bid,model_definition,content(\x01\x12|\n\x08GetModel\x12\".vdp.model.v1alpha.GetModelRequest\x1a#.vdp.model.v1alpha.GetModelResponse\"\'\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1alpha/{name=models/*}\x12\x9f\x01\n\x0bUpdateModel\x12%.vdp.model.v1alpha.UpdateModelRequest\x1a&.vdp.model.v1alpha.UpdateModelResponse\"A\xda\x41\x11model,update_mask\x82\xd3\xe4\x93\x02\':\x05model2\x1e/v1alpha/{model.name=models/*}\x12\x85\x01\n\x0b\x44\x65leteModel\x12%.vdp.model.v1alpha.DeleteModelRequest\x1a&.vdp.model.v1alpha.DeleteModelResponse\"\'\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1a*\x18/v1alpha/{name=models/*}\x12\x96\x01\n\x0bLookUpModel\x12%.vdp.model.v1alpha.LookUpModelRequest\x1a&.vdp.model.v1alpha.LookUpModelResponse\"8\xda\x41\tpermalink\x82\xd3\xe4\x93\x02&\x12$/v1alpha/{permalink=models/*}/lookUp\x12\x9c\x01\n\x0bRenameModel\x12%.vdp.model.v1alpha.RenameModelRequest\x1a&.vdp.model.v1alpha.RenameModelResponse\">\xda\x41\x11name,new_model_id\x82\xd3\xe4\x93\x02$:\x01*\"\x1f/v1alpha/{name=models/*}/rename\x12\x93\x01\n\x0cPublishModel\x12&.vdp.model.v1alpha.PublishModelRequest\x1a\'.vdp.model.v1alpha.PublishModelResponse\"2\xda\x41\x04name\x82\xd3\xe4\x93\x02%:\x01*\" /v1alpha/{name=models/*}/publish\x12\x9b\x01\n\x0eUnpublishModel\x12(.vdp.model.v1alpha.UnpublishModelRequest\x1a).vdp.model.v1alpha.UnpublishModelResponse\"4\xda\x41\x04name\x82\xd3\xe4\x93\x02\':\x01*\"\"/v1alpha/{name=models/*}/unpublish\x12\xa5\x01\n\x11ListModelInstance\x12+.vdp.model.v1alpha.ListModelInstanceRequest\x1a,.vdp.model.v1alpha.ListModelInstanceResponse\"5\xda\x41\x06parent\x82\xd3\xe4\x93\x02&\x12$/v1alpha/{parent=models/*}/instances\x12\xa0\x01\n\x10GetModelInstance\x12*.vdp.model.v1alpha.GetModelInstanceRequest\x1a+.vdp.model.v1alpha.GetModelInstanceResponse\"3\xda\x41\x04name\x82\xd3\xe4\x93\x02&\x12$/v1alpha/{name=models/*/instances/*}\x12\xba\x01\n\x13LookUpModelInstance\x12-.vdp.model.v1alpha.LookUpModelInstanceRequest\x1a..vdp.model.v1alpha.LookUpModelInstanceResponse\"D\xda\x41\tpermalink\x82\xd3\xe4\x93\x02\x32\x12\x30/v1alpha/{permalink=models/*/instances/*}/lookUp\x12\xb3\x01\n\x13\x44\x65ployModelInstance\x12-.vdp.model.v1alpha.DeployModelInstanceRequest\x1a..vdp.model.v1alpha.DeployModelInstanceResponse\"=\xda\x41\x04name\x82\xd3\xe4\x93\x02\x30:\x01*\"+/v1alpha/{name=models/*/instances/*}/deploy\x12\xbb\x01\n\x15UndeployModelInstance\x12/.vdp.model.v1alpha.UndeployModelInstanceRequest\x1a\x30.vdp.model.v1alpha.UndeployModelInstanceResponse\"?\xda\x41\x04name\x82\xd3\xe4\x93\x02\x32:\x01*\"-/v1alpha/{name=models/*/instances/*}/undeploy\x12\xb3\x01\n\x14GetModelInstanceCard\x12..vdp.model.v1alpha.GetModelInstanceCardRequest\x1a/.vdp.model.v1alpha.GetModelInstanceCardResponse\":\xda\x41\x04name\x82\xd3\xe4\x93\x02-\x12+/v1alpha/{name=models/*/instances/*/readme}\x12\xbe\x01\n\x14TriggerModelInstance\x12..vdp.model.v1alpha.TriggerModelInstanceRequest\x1a/.vdp.model.v1alpha.TriggerModelInstanceResponse\"E\xda\x41\x0bname,inputs\x82\xd3\xe4\x93\x02\x31:\x01*\",/v1alpha/{name=models/*/instances/*}/trigger\x12\xb7\x01\n$TriggerModelInstanceBinaryFileUpload\x12>.vdp.model.v1alpha.TriggerModelInstanceBinaryFileUploadRequest\x1a?.vdp.model.v1alpha.TriggerModelInstanceBinaryFileUploadResponse\"\x0c\xda\x41\tname,file(\x01\x12\xb2\x01\n\x11TestModelInstance\x12+.vdp.model.v1alpha.TestModelInstanceRequest\x1a,.vdp.model.v1alpha.TestModelInstanceResponse\"B\xda\x41\x0bname,inputs\x82\xd3\xe4\x93\x02.:\x01*\")/v1alpha/{name=models/*/instances/*}/test\x12\xae\x01\n!TestModelInstanceBinaryFileUpload\x12;.vdp.model.v1alpha.TestModelInstanceBinaryFileUploadRequest\x1a<.vdp.model.v1alpha.TestModelInstanceBinaryFileUploadResponse\"\x0c\xda\x41\tname,file(\x01\x12\x9b\x01\n\x11GetModelOperation\x12+.vdp.model.v1alpha.GetModelOperationRequest\x1a,.vdp.model.v1alpha.GetModelOperationResponse\"+\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1alpha/{name=operations/*}\x12\x8e\x01\n\x12ListModelOperation\x12,.vdp.model.v1alpha.ListModelOperationRequest\x1a-.vdp.model.v1alpha.ListModelOperationResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/v1alpha/operations\x12\xae\x01\n\x14\x43\x61ncelModelOperation\x12..vdp.model.v1alpha.CancelModelOperationRequest\x1a/.vdp.model.v1alpha.CancelModelOperationResponse\"5\xda\x41\x04name\x82\xd3\xe4\x93\x02(:\x01*\"#/v1alpha/{name=operations/*}/cancel\x1a\x13\xca\x41\x10\x61pi.instill.techB\xd8\x01\n\x15\x63om.vdp.model.v1alphaB\x17ModelPublicServiceProtoP\x01Z@github.com/instill-ai/protogen-go/vdp/model/v1alpha;modelv1alpha\xa2\x02\x03VMX\xaa\x02\x11Vdp.Model.V1alpha\xca\x02\x11Vdp\\Model\\V1alpha\xe2\x02\x1dVdp\\Model\\V1alpha\\GPBMetadata\xea\x02\x13Vdp::Model::V1alphab\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vdp.model.v1alpha.model_public_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.vdp.model.v1alphaB\027ModelPublicServiceProtoP\001Z@github.com/instill-ai/protogen-go/vdp/model/v1alpha;modelv1alpha\242\002\003VMX\252\002\021Vdp.Model.V1alpha\312\002\021Vdp\\Model\\V1alpha\342\002\035Vdp\\Model\\V1alpha\\GPBMetadata\352\002\023Vdp::Model::V1alpha'
  _MODELPUBLICSERVICE._options = None
  _MODELPUBLICSERVICE._serialized_options = b'\312A\020api.instill.tech'
  _MODELPUBLICSERVICE.methods_by_name['Liveness']._options = None
  _MODELPUBLICSERVICE.methods_by_name['Liveness']._serialized_options = b'\202\323\344\223\002.Z\027\022\025/v1alpha/health/model\022\023/v1alpha/__liveness'
  _MODELPUBLICSERVICE.methods_by_name['Readiness']._options = None
  _MODELPUBLICSERVICE.methods_by_name['Readiness']._serialized_options = b'\202\323\344\223\002.Z\026\022\024/v1alpha/ready/model\022\024/v1alpha/__readiness'
  _MODELPUBLICSERVICE.methods_by_name['ListModelDefinition']._options = None
  _MODELPUBLICSERVICE.methods_by_name['ListModelDefinition']._serialized_options = b'\202\323\344\223\002\034\022\032/v1alpha/model-definitions'
  _MODELPUBLICSERVICE.methods_by_name['GetModelDefinition']._options = None
  _MODELPUBLICSERVICE.methods_by_name['GetModelDefinition']._serialized_options = b'\332A\004name\202\323\344\223\002%\022#/v1alpha/{name=model-definitions/*}'
  _MODELPUBLICSERVICE.methods_by_name['ListModel']._options = None
  _MODELPUBLICSERVICE.methods_by_name['ListModel']._serialized_options = b'\202\323\344\223\002\021\022\017/v1alpha/models'
  _MODELPUBLICSERVICE.methods_by_name['CreateModel']._options = None
  _MODELPUBLICSERVICE.methods_by_name['CreateModel']._serialized_options = b'\332A\005model\202\323\344\223\002\030:\005model\"\017/v1alpha/models'
  _MODELPUBLICSERVICE.methods_by_name['CreateModelBinaryFileUpload']._options = None
  _MODELPUBLICSERVICE.methods_by_name['CreateModelBinaryFileUpload']._serialized_options = b'\332A\033id,model_definition,content'
  _MODELPUBLICSERVICE.methods_by_name['GetModel']._options = None
  _MODELPUBLICSERVICE.methods_by_name['GetModel']._serialized_options = b'\332A\004name\202\323\344\223\002\032\022\030/v1alpha/{name=models/*}'
  _MODELPUBLICSERVICE.methods_by_name['UpdateModel']._options = None
  _MODELPUBLICSERVICE.methods_by_name['UpdateModel']._serialized_options = b'\332A\021model,update_mask\202\323\344\223\002\':\005model2\036/v1alpha/{model.name=models/*}'
  _MODELPUBLICSERVICE.methods_by_name['DeleteModel']._options = None
  _MODELPUBLICSERVICE.methods_by_name['DeleteModel']._serialized_options = b'\332A\004name\202\323\344\223\002\032*\030/v1alpha/{name=models/*}'
  _MODELPUBLICSERVICE.methods_by_name['LookUpModel']._options = None
  _MODELPUBLICSERVICE.methods_by_name['LookUpModel']._serialized_options = b'\332A\tpermalink\202\323\344\223\002&\022$/v1alpha/{permalink=models/*}/lookUp'
  _MODELPUBLICSERVICE.methods_by_name['RenameModel']._options = None
  _MODELPUBLICSERVICE.methods_by_name['RenameModel']._serialized_options = b'\332A\021name,new_model_id\202\323\344\223\002$:\001*\"\037/v1alpha/{name=models/*}/rename'
  _MODELPUBLICSERVICE.methods_by_name['PublishModel']._options = None
  _MODELPUBLICSERVICE.methods_by_name['PublishModel']._serialized_options = b'\332A\004name\202\323\344\223\002%:\001*\" /v1alpha/{name=models/*}/publish'
  _MODELPUBLICSERVICE.methods_by_name['UnpublishModel']._options = None
  _MODELPUBLICSERVICE.methods_by_name['UnpublishModel']._serialized_options = b'\332A\004name\202\323\344\223\002\':\001*\"\"/v1alpha/{name=models/*}/unpublish'
  _MODELPUBLICSERVICE.methods_by_name['ListModelInstance']._options = None
  _MODELPUBLICSERVICE.methods_by_name['ListModelInstance']._serialized_options = b'\332A\006parent\202\323\344\223\002&\022$/v1alpha/{parent=models/*}/instances'
  _MODELPUBLICSERVICE.methods_by_name['GetModelInstance']._options = None
  _MODELPUBLICSERVICE.methods_by_name['GetModelInstance']._serialized_options = b'\332A\004name\202\323\344\223\002&\022$/v1alpha/{name=models/*/instances/*}'
  _MODELPUBLICSERVICE.methods_by_name['LookUpModelInstance']._options = None
  _MODELPUBLICSERVICE.methods_by_name['LookUpModelInstance']._serialized_options = b'\332A\tpermalink\202\323\344\223\0022\0220/v1alpha/{permalink=models/*/instances/*}/lookUp'
  _MODELPUBLICSERVICE.methods_by_name['DeployModelInstance']._options = None
  _MODELPUBLICSERVICE.methods_by_name['DeployModelInstance']._serialized_options = b'\332A\004name\202\323\344\223\0020:\001*\"+/v1alpha/{name=models/*/instances/*}/deploy'
  _MODELPUBLICSERVICE.methods_by_name['UndeployModelInstance']._options = None
  _MODELPUBLICSERVICE.methods_by_name['UndeployModelInstance']._serialized_options = b'\332A\004name\202\323\344\223\0022:\001*\"-/v1alpha/{name=models/*/instances/*}/undeploy'
  _MODELPUBLICSERVICE.methods_by_name['GetModelInstanceCard']._options = None
  _MODELPUBLICSERVICE.methods_by_name['GetModelInstanceCard']._serialized_options = b'\332A\004name\202\323\344\223\002-\022+/v1alpha/{name=models/*/instances/*/readme}'
  _MODELPUBLICSERVICE.methods_by_name['TriggerModelInstance']._options = None
  _MODELPUBLICSERVICE.methods_by_name['TriggerModelInstance']._serialized_options = b'\332A\013name,inputs\202\323\344\223\0021:\001*\",/v1alpha/{name=models/*/instances/*}/trigger'
  _MODELPUBLICSERVICE.methods_by_name['TriggerModelInstanceBinaryFileUpload']._options = None
  _MODELPUBLICSERVICE.methods_by_name['TriggerModelInstanceBinaryFileUpload']._serialized_options = b'\332A\tname,file'
  _MODELPUBLICSERVICE.methods_by_name['TestModelInstance']._options = None
  _MODELPUBLICSERVICE.methods_by_name['TestModelInstance']._serialized_options = b'\332A\013name,inputs\202\323\344\223\002.:\001*\")/v1alpha/{name=models/*/instances/*}/test'
  _MODELPUBLICSERVICE.methods_by_name['TestModelInstanceBinaryFileUpload']._options = None
  _MODELPUBLICSERVICE.methods_by_name['TestModelInstanceBinaryFileUpload']._serialized_options = b'\332A\tname,file'
  _MODELPUBLICSERVICE.methods_by_name['GetModelOperation']._options = None
  _MODELPUBLICSERVICE.methods_by_name['GetModelOperation']._serialized_options = b'\332A\004name\202\323\344\223\002\036\022\034/v1alpha/{name=operations/*}'
  _MODELPUBLICSERVICE.methods_by_name['ListModelOperation']._options = None
  _MODELPUBLICSERVICE.methods_by_name['ListModelOperation']._serialized_options = b'\202\323\344\223\002\025\022\023/v1alpha/operations'
  _MODELPUBLICSERVICE.methods_by_name['CancelModelOperation']._options = None
  _MODELPUBLICSERVICE.methods_by_name['CancelModelOperation']._serialized_options = b'\332A\004name\202\323\344\223\002(:\001*\"#/v1alpha/{name=operations/*}/cancel'
  _MODELPUBLICSERVICE._serialized_start=233
  _MODELPUBLICSERVICE._serialized_end=4640
# @@protoc_insertion_point(module_scope)