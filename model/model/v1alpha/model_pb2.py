# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model/model/v1alpha/model.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from common.healthcheck.v1alpha import healthcheck_pb2 as common_dot_healthcheck_dot_v1alpha_dot_healthcheck__pb2
from model.model.v1alpha import model_definition_pb2 as model_dot_model_dot_v1alpha_dot_model__definition__pb2
from model.model.v1alpha import task_classification_pb2 as model_dot_model_dot_v1alpha_dot_task__classification__pb2
from model.model.v1alpha import task_detection_pb2 as model_dot_model_dot_v1alpha_dot_task__detection__pb2
from model.model.v1alpha import task_keypoint_pb2 as model_dot_model_dot_v1alpha_dot_task__keypoint__pb2
from model.model.v1alpha import task_ocr_pb2 as model_dot_model_dot_v1alpha_dot_task__ocr__pb2
from model.model.v1alpha import task_instance_segmentation_pb2 as model_dot_model_dot_v1alpha_dot_task__instance__segmentation__pb2
from model.model.v1alpha import task_semantic_segmentation_pb2 as model_dot_model_dot_v1alpha_dot_task__semantic__segmentation__pb2
from model.model.v1alpha import task_text_to_image_pb2 as model_dot_model_dot_v1alpha_dot_task__text__to__image__pb2
from model.model.v1alpha import task_text_generation_pb2 as model_dot_model_dot_v1alpha_dot_task__text__generation__pb2
from model.model.v1alpha import task_unspecified_pb2 as model_dot_model_dot_v1alpha_dot_task__unspecified__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fmodel/model/v1alpha/model.proto\x12\x13model.model.v1alpha\x1a\x1cgoogle/protobuf/struct.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/longrunning/operations.proto\x1a,common/healthcheck/v1alpha/healthcheck.proto\x1a*model/model/v1alpha/model_definition.proto\x1a-model/model/v1alpha/task_classification.proto\x1a(model/model/v1alpha/task_detection.proto\x1a\'model/model/v1alpha/task_keypoint.proto\x1a\"model/model/v1alpha/task_ocr.proto\x1a\x34model/model/v1alpha/task_instance_segmentation.proto\x1a\x34model/model/v1alpha/task_semantic_segmentation.proto\x1a,model/model/v1alpha/task_text_to_image.proto\x1a.model/model/v1alpha/task_text_generation.proto\x1a*model/model/v1alpha/task_unspecified.proto\"\x97\x01\n\x0fLivenessRequest\x12k\n\x14health_check_request\x18\x01 \x01(\x0b\x32..common.healthcheck.v1alpha.HealthCheckRequestB\x04\xe2\x41\x01\x01H\x00R\x12healthCheckRequest\x88\x01\x01\x42\x17\n\x15_health_check_request\"w\n\x10LivenessResponse\x12\x63\n\x15health_check_response\x18\x01 \x01(\x0b\x32/.common.healthcheck.v1alpha.HealthCheckResponseR\x13healthCheckResponse\"\x98\x01\n\x10ReadinessRequest\x12k\n\x14health_check_request\x18\x01 \x01(\x0b\x32..common.healthcheck.v1alpha.HealthCheckRequestB\x04\xe2\x41\x01\x01H\x00R\x12healthCheckRequest\x88\x01\x01\x42\x17\n\x15_health_check_request\"x\n\x11ReadinessResponse\x12\x63\n\x15health_check_response\x18\x01 \x01(\x0b\x32/.common.healthcheck.v1alpha.HealthCheckResponseR\x13healthCheckResponse\"\xa9\t\n\x05Model\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\x16\n\x03uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x03uid\x12\x14\n\x02id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x05R\x02id\x12+\n\x0b\x64\x65scription\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01H\x01R\x0b\x64\x65scription\x88\x01\x01\x12T\n\x10model_definition\x18\x05 \x01(\tB)\xe2\x41\x01\x05\xfa\x41\"\n api.instill.tech/ModelDefinitionR\x0fmodelDefinition\x12\x43\n\rconfiguration\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructB\x04\xe2\x41\x01\x05R\rconfiguration\x12\x39\n\x04task\x18\x07 \x01(\x0e\x32\x1f.model.model.v1alpha.Model.TaskB\x04\xe2\x41\x01\x03R\x04task\x12<\n\x05state\x18\x08 \x01(\x0e\x32 .model.model.v1alpha.Model.StateB\x04\xe2\x41\x01\x03R\x05state\x12K\n\nvisibility\x18\t \x01(\x0e\x32%.model.model.v1alpha.Model.VisibilityB\x04\xe2\x41\x01\x03R\nvisibility\x12\x34\n\x04user\x18\n \x01(\tB\x1e\xe2\x41\x01\x03\xfa\x41\x17\n\x15\x61pi.instill.tech/UserH\x00R\x04user\x12:\n\x03org\x18\x0b \x01(\tB&\xe2\x41\x01\x03\xfa\x41\x1f\n\x1d\x61pi.instill.tech/OrganizationH\x00R\x03org\x12\x41\n\x0b\x63reate_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\"W\n\nVisibility\x12\x1a\n\x16VISIBILITY_UNSPECIFIED\x10\x00\x12\x16\n\x12VISIBILITY_PRIVATE\x10\x01\x12\x15\n\x11VISIBILITY_PUBLIC\x10\x02\"\xdc\x01\n\x04Task\x12\x14\n\x10TASK_UNSPECIFIED\x10\x00\x12\x17\n\x13TASK_CLASSIFICATION\x10\x01\x12\x12\n\x0eTASK_DETECTION\x10\x02\x12\x11\n\rTASK_KEYPOINT\x10\x03\x12\x0c\n\x08TASK_OCR\x10\x04\x12\x1e\n\x1aTASK_INSTANCE_SEGMENTATION\x10\x05\x12\x1e\n\x1aTASK_SEMANTIC_SEGMENTATION\x10\x06\x12\x16\n\x12TASK_TEXT_TO_IMAGE\x10\x07\x12\x18\n\x14TASK_TEXT_GENERATION\x10\x08\"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x11\n\rSTATE_OFFLINE\x10\x01\x12\x10\n\x0cSTATE_ONLINE\x10\x02\x12\x0f\n\x0bSTATE_ERROR\x10\x03:+\xea\x41(\n\x16\x61pi.instill.tech/Model\x12\x0emodels/{model}B\x07\n\x05ownerB\x0e\n\x0c_description\"\xd3\x01\n\tModelCard\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\x18\n\x04size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x03R\x04size\x12\x18\n\x04type\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x04type\x12\x1e\n\x07\x63ontent\x18\x04 \x01(\x0c\x42\x04\xe2\x41\x01\x03R\x07\x63ontent\x12 \n\x08\x65ncoding\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\x08\x65ncoding:6\xea\x41\x33\n\x1a\x61pi.instill.tech/ModelCard\x12\x15models/{model}/readme\"\xc5\x01\n\x11ListModelsRequest\x12&\n\tpage_size\x18\x01 \x01(\x03\x42\x04\xe2\x41\x01\x01H\x00R\x08pageSize\x88\x01\x01\x12(\n\npage_token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01H\x01R\tpageToken\x88\x01\x01\x12\x38\n\x04view\x18\x03 \x01(\x0e\x32\x19.model.model.v1alpha.ViewB\x04\xe2\x41\x01\x01H\x02R\x04view\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\x07\n\x05_view\"\x8f\x01\n\x12ListModelsResponse\x12\x32\n\x06models\x18\x01 \x03(\x0b\x32\x1a.model.model.v1alpha.ModelR\x06models\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12\x1d\n\ntotal_size\x18\x03 \x01(\x03R\ttotalSize\"L\n\x12\x43reateModelRequest\x12\x36\n\x05model\x18\x01 \x01(\x0b\x32\x1a.model.model.v1alpha.ModelB\x04\xe2\x41\x01\x02R\x05model\"X\n\x13\x43reateModelResponse\x12\x41\n\toperation\x18\x01 \x01(\x0b\x32\x1d.google.longrunning.OperationB\x04\xe2\x41\x01\x03R\toperation\"|\n\"CreateModelBinaryFileUploadRequest\x12\x36\n\x05model\x18\x01 \x01(\x0b\x32\x1a.model.model.v1alpha.ModelB\x04\xe2\x41\x01\x02R\x05model\x12\x1e\n\x07\x63ontent\x18\x02 \x01(\x0c\x42\x04\xe2\x41\x01\x02R\x07\x63ontent\"h\n#CreateModelBinaryFileUploadResponse\x12\x41\n\toperation\x18\x01 \x01(\x0b\x32\x1d.google.longrunning.OperationB\x04\xe2\x41\x01\x03R\toperation\"\x9c\x01\n\x0fGetModelRequest\x12\x46\n\x04name\x18\x01 \x01(\tB2\x92\x41\x10\xca>\r\xfa\x02\nmodel.name\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\x12\x38\n\x04view\x18\x02 \x01(\x0e\x32\x19.model.model.v1alpha.ViewB\x04\xe2\x41\x01\x01H\x00R\x04view\x88\x01\x01\x42\x07\n\x05_view\"D\n\x10GetModelResponse\x12\x30\n\x05model\x18\x01 \x01(\x0b\x32\x1a.model.model.v1alpha.ModelR\x05model\"\x8f\x01\n\x12UpdateModelRequest\x12\x36\n\x05model\x18\x01 \x01(\x0b\x32\x1a.model.model.v1alpha.ModelB\x04\xe2\x41\x01\x02R\x05model\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\"G\n\x13UpdateModelResponse\x12\x30\n\x05model\x18\x01 \x01(\x0b\x32\x1a.model.model.v1alpha.ModelR\x05model\"\\\n\x12\x44\x65leteModelRequest\x12\x46\n\x04name\x18\x01 \x01(\tB2\x92\x41\x10\xca>\r\xfa\x02\nmodel.name\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\"\x15\n\x13\x44\x65leteModelResponse\"{\n\x12LookUpModelRequest\x12\"\n\tpermalink\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\tpermalink\x12\x38\n\x04view\x18\x02 \x01(\x0e\x32\x19.model.model.v1alpha.ViewB\x04\xe2\x41\x01\x01H\x00R\x04view\x88\x01\x01\x42\x07\n\x05_view\"G\n\x13LookUpModelResponse\x12\x30\n\x05model\x18\x01 \x01(\x0b\x32\x1a.model.model.v1alpha.ModelR\x05model\"q\n\x12RenameModelRequest\x12\x33\n\x04name\x18\x01 \x01(\tB\x1f\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\x12&\n\x0cnew_model_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\nnewModelId\"G\n\x13RenameModelResponse\x12\x30\n\x05model\x18\x01 \x01(\x0b\x32\x1a.model.model.v1alpha.ModelR\x05model\"J\n\x13PublishModelRequest\x12\x33\n\x04name\x18\x01 \x01(\tB\x1f\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\"H\n\x14PublishModelResponse\x12\x30\n\x05model\x18\x01 \x01(\x0b\x32\x1a.model.model.v1alpha.ModelR\x05model\"L\n\x15UnpublishModelRequest\x12\x33\n\x04name\x18\x01 \x01(\tB\x1f\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\"J\n\x16UnpublishModelResponse\x12\x30\n\x05model\x18\x01 \x01(\x0b\x32\x1a.model.model.v1alpha.ModelR\x05model\"I\n\x12\x44\x65ployModelRequest\x12\x33\n\x04name\x18\x01 \x01(\tB\x1f\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\"R\n\x13\x44\x65ployModelResponse\x12;\n\toperation\x18\x01 \x01(\x0b\x32\x1d.google.longrunning.OperationR\toperation\"K\n\x14UndeployModelRequest\x12\x33\n\x04name\x18\x01 \x01(\tB\x1f\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\"T\n\x15UndeployModelResponse\x12;\n\toperation\x18\x01 \x01(\x0b\x32\x1d.google.longrunning.OperationR\toperation\"h\n\x13GetModelCardRequest\x12Q\n\x04name\x18\x01 \x01(\tB=\x92\x41\x17\xca>\x14\xfa\x02\x11model.name/readme\xe2\x41\x01\x02\xfa\x41\x1c\n\x1a\x61pi.instill.tech/ModelCardR\x04name\"N\n\x14GetModelCardResponse\x12\x36\n\x06readme\x18\x01 \x01(\x0b\x32\x1e.model.model.v1alpha.ModelCardR\x06readme\"a\n\x11WatchModelRequest\x12L\n\x04name\x18\x01 \x01(\tB8\x92\x41\x16\xca>\x13\xfa\x02\x10model.name/watch\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\"h\n\x12WatchModelResponse\x12\x36\n\x05state\x18\x01 \x01(\x0e\x32 .model.model.v1alpha.Model.StateR\x05state\x12\x1a\n\x08progress\x18\x02 \x01(\x05R\x08progress\"\xdd\x05\n\tTaskInput\x12R\n\x0e\x63lassification\x18\x01 \x01(\x0b\x32(.model.model.v1alpha.ClassificationInputH\x00R\x0e\x63lassification\x12\x43\n\tdetection\x18\x02 \x01(\x0b\x32#.model.model.v1alpha.DetectionInputH\x00R\tdetection\x12@\n\x08keypoint\x18\x03 \x01(\x0b\x32\".model.model.v1alpha.KeypointInputH\x00R\x08keypoint\x12\x31\n\x03ocr\x18\x04 \x01(\x0b\x32\x1d.model.model.v1alpha.OcrInputH\x00R\x03ocr\x12\x65\n\x15instance_segmentation\x18\x05 \x01(\x0b\x32..model.model.v1alpha.InstanceSegmentationInputH\x00R\x14instanceSegmentation\x12\x65\n\x15semantic_segmentation\x18\x06 \x01(\x0b\x32..model.model.v1alpha.SemanticSegmentationInputH\x00R\x14semanticSegmentation\x12K\n\rtext_to_image\x18\x07 \x01(\x0b\x32%.model.model.v1alpha.TextToImageInputH\x00R\x0btextToImage\x12S\n\x0ftext_generation\x18\x08 \x01(\x0b\x32(.model.model.v1alpha.TextGenerationInputH\x00R\x0etextGeneration\x12I\n\x0bunspecified\x18\t \x01(\x0b\x32%.model.model.v1alpha.UnspecifiedInputH\x00R\x0bunspecifiedB\x07\n\x05input\"\x87\x06\n\x0fTaskInputStream\x12X\n\x0e\x63lassification\x18\x01 \x01(\x0b\x32..model.model.v1alpha.ClassificationInputStreamH\x00R\x0e\x63lassification\x12I\n\tdetection\x18\x02 \x01(\x0b\x32).model.model.v1alpha.DetectionInputStreamH\x00R\tdetection\x12\x46\n\x08keypoint\x18\x03 \x01(\x0b\x32(.model.model.v1alpha.KeypointInputStreamH\x00R\x08keypoint\x12\x37\n\x03ocr\x18\x04 \x01(\x0b\x32#.model.model.v1alpha.OcrInputStreamH\x00R\x03ocr\x12k\n\x15instance_segmentation\x18\x05 \x01(\x0b\x32\x34.model.model.v1alpha.InstanceSegmentationInputStreamH\x00R\x14instanceSegmentation\x12k\n\x15semantic_segmentation\x18\x06 \x01(\x0b\x32\x34.model.model.v1alpha.SemanticSegmentationInputStreamH\x00R\x14semanticSegmentation\x12K\n\rtext_to_image\x18\x07 \x01(\x0b\x32%.model.model.v1alpha.TextToImageInputH\x00R\x0btextToImage\x12S\n\x0ftext_generation\x18\x08 \x01(\x0b\x32(.model.model.v1alpha.TextGenerationInputH\x00R\x0etextGeneration\x12I\n\x0bunspecified\x18\t \x01(\x0b\x32%.model.model.v1alpha.UnspecifiedInputH\x00R\x0bunspecifiedB\x07\n\x05input\"\x9e\x06\n\nTaskOutput\x12Y\n\x0e\x63lassification\x18\x01 \x01(\x0b\x32).model.model.v1alpha.ClassificationOutputB\x04\xe2\x41\x01\x03H\x00R\x0e\x63lassification\x12J\n\tdetection\x18\x02 \x01(\x0b\x32$.model.model.v1alpha.DetectionOutputB\x04\xe2\x41\x01\x03H\x00R\tdetection\x12G\n\x08keypoint\x18\x03 \x01(\x0b\x32#.model.model.v1alpha.KeypointOutputB\x04\xe2\x41\x01\x03H\x00R\x08keypoint\x12\x38\n\x03ocr\x18\x04 \x01(\x0b\x32\x1e.model.model.v1alpha.OcrOutputB\x04\xe2\x41\x01\x03H\x00R\x03ocr\x12l\n\x15instance_segmentation\x18\x05 \x01(\x0b\x32/.model.model.v1alpha.InstanceSegmentationOutputB\x04\xe2\x41\x01\x03H\x00R\x14instanceSegmentation\x12l\n\x15semantic_segmentation\x18\x06 \x01(\x0b\x32/.model.model.v1alpha.SemanticSegmentationOutputB\x04\xe2\x41\x01\x03H\x00R\x14semanticSegmentation\x12R\n\rtext_to_image\x18\x07 \x01(\x0b\x32&.model.model.v1alpha.TextToImageOutputB\x04\xe2\x41\x01\x03H\x00R\x0btextToImage\x12Z\n\x0ftext_generation\x18\x08 \x01(\x0b\x32).model.model.v1alpha.TextGenerationOutputB\x04\xe2\x41\x01\x03H\x00R\x0etextGeneration\x12P\n\x0bunspecified\x18\t \x01(\x0b\x32&.model.model.v1alpha.UnspecifiedOutputB\x04\xe2\x41\x01\x03H\x00R\x0bunspecifiedB\x08\n\x06output\"\x91\x01\n\x13TriggerModelRequest\x12\x33\n\x04name\x18\x01 \x01(\tB\x1f\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\x12\x45\n\x0btask_inputs\x18\x02 \x03(\x0b\x32\x1e.model.model.v1alpha.TaskInputB\x04\xe2\x41\x01\x02R\ntaskInputs\"\x8f\x01\n\x14TriggerModelResponse\x12\x33\n\x04task\x18\x01 \x01(\x0e\x32\x1f.model.model.v1alpha.Model.TaskR\x04task\x12\x42\n\x0ctask_outputs\x18\x02 \x03(\x0b\x32\x1f.model.model.v1alpha.TaskOutputR\x0btaskOutputs\"\xa5\x01\n#TriggerModelBinaryFileUploadRequest\x12\x33\n\x04name\x18\x01 \x01(\tB\x1f\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\x12I\n\ntask_input\x18\x02 \x01(\x0b\x32$.model.model.v1alpha.TaskInputStreamB\x04\xe2\x41\x01\x02R\ttaskInput\"\xab\x01\n$TriggerModelBinaryFileUploadResponse\x12\x39\n\x04task\x18\x01 \x01(\x0e\x32\x1f.model.model.v1alpha.Model.TaskB\x04\xe2\x41\x01\x02R\x04task\x12H\n\x0ctask_outputs\x18\x02 \x03(\x0b\x32\x1f.model.model.v1alpha.TaskOutputB\x04\xe2\x41\x01\x02R\x0btaskOutputs\"\x8e\x01\n\x10TestModelRequest\x12\x33\n\x04name\x18\x01 \x01(\tB\x1f\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\x12\x45\n\x0btask_inputs\x18\x02 \x03(\x0b\x32\x1e.model.model.v1alpha.TaskInputB\x04\xe2\x41\x01\x02R\ntaskInputs\"\x98\x01\n\x11TestModelResponse\x12\x39\n\x04task\x18\x01 \x01(\x0e\x32\x1f.model.model.v1alpha.Model.TaskB\x04\xe2\x41\x01\x02R\x04task\x12H\n\x0ctask_outputs\x18\x02 \x03(\x0b\x32\x1f.model.model.v1alpha.TaskOutputB\x04\xe2\x41\x01\x02R\x0btaskOutputs\"\xa2\x01\n TestModelBinaryFileUploadRequest\x12\x33\n\x04name\x18\x01 \x01(\tB\x1f\xe2\x41\x01\x02\xfa\x41\x18\n\x16\x61pi.instill.tech/ModelR\x04name\x12I\n\ntask_input\x18\x02 \x01(\x0b\x32$.model.model.v1alpha.TaskInputStreamB\x04\xe2\x41\x01\x02R\ttaskInput\"\xa8\x01\n!TestModelBinaryFileUploadResponse\x12\x39\n\x04task\x18\x01 \x01(\x0e\x32\x1f.model.model.v1alpha.Model.TaskB\x04\xe2\x41\x01\x02R\x04task\x12H\n\x0ctask_outputs\x18\x02 \x03(\x0b\x32\x1f.model.model.v1alpha.TaskOutputB\x04\xe2\x41\x01\x02R\x0btaskOutputs\"w\n\x18GetModelOperationRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12\x38\n\x04view\x18\x02 \x01(\x0e\x32\x19.model.model.v1alpha.ViewB\x04\xe2\x41\x01\x01H\x00R\x04view\x88\x01\x01\x42\x07\n\x05_view\"X\n\x19GetModelOperationResponse\x12;\n\toperation\x18\x01 \x01(\x0b\x32\x1d.google.longrunning.OperationR\toperation\"\xca\x01\n\x16ListModelsAdminRequest\x12&\n\tpage_size\x18\x01 \x01(\x03\x42\x04\xe2\x41\x01\x01H\x00R\x08pageSize\x88\x01\x01\x12(\n\npage_token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01H\x01R\tpageToken\x88\x01\x01\x12\x38\n\x04view\x18\x03 \x01(\x0e\x32\x19.model.model.v1alpha.ViewB\x04\xe2\x41\x01\x01H\x02R\x04view\x88\x01\x01\x42\x0c\n\n_page_sizeB\r\n\x0b_page_tokenB\x07\n\x05_view\"\x94\x01\n\x17ListModelsAdminResponse\x12\x32\n\x06models\x18\x01 \x03(\x0b\x32\x1a.model.model.v1alpha.ModelR\x06models\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12\x1d\n\ntotal_size\x18\x03 \x01(\x03R\ttotalSize\"\x80\x01\n\x17LookUpModelAdminRequest\x12\"\n\tpermalink\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\tpermalink\x12\x38\n\x04view\x18\x02 \x01(\x0e\x32\x19.model.model.v1alpha.ViewB\x04\xe2\x41\x01\x01H\x00R\x04view\x88\x01\x01\x42\x07\n\x05_view\"L\n\x18LookUpModelAdminResponse\x12\x30\n\x05model\x18\x01 \x01(\x0b\x32\x1a.model.model.v1alpha.ModelR\x05model\"B\n\x11\x43heckModelRequest\x12-\n\x0fmodel_permalink\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0emodelPermalink\"L\n\x12\x43heckModelResponse\x12\x36\n\x05state\x18\x01 \x01(\x0e\x32 .model.model.v1alpha.Model.StateR\x05stateB\xd7\x01\n\x17\x63om.model.model.v1alphaB\nModelProtoP\x01ZBgithub.com/instill-ai/protogen-go/model/model/v1alpha;modelv1alpha\xa2\x02\x03MMX\xaa\x02\x13Model.Model.V1alpha\xca\x02\x13Model\\Model\\V1alpha\xe2\x02\x1fModel\\Model\\V1alpha\\GPBMetadata\xea\x02\x15Model::Model::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model.model.v1alpha.model_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.model.model.v1alphaB\nModelProtoP\001ZBgithub.com/instill-ai/protogen-go/model/model/v1alpha;modelv1alpha\242\002\003MMX\252\002\023Model.Model.V1alpha\312\002\023Model\\Model\\V1alpha\342\002\037Model\\Model\\V1alpha\\GPBMetadata\352\002\025Model::Model::V1alpha'
  _LIVENESSREQUEST.fields_by_name['health_check_request']._options = None
  _LIVENESSREQUEST.fields_by_name['health_check_request']._serialized_options = b'\342A\001\001'
  _READINESSREQUEST.fields_by_name['health_check_request']._options = None
  _READINESSREQUEST.fields_by_name['health_check_request']._serialized_options = b'\342A\001\001'
  _MODEL.fields_by_name['name']._options = None
  _MODEL.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _MODEL.fields_by_name['uid']._options = None
  _MODEL.fields_by_name['uid']._serialized_options = b'\342A\001\003'
  _MODEL.fields_by_name['id']._options = None
  _MODEL.fields_by_name['id']._serialized_options = b'\342A\001\005'
  _MODEL.fields_by_name['description']._options = None
  _MODEL.fields_by_name['description']._serialized_options = b'\342A\001\001'
  _MODEL.fields_by_name['model_definition']._options = None
  _MODEL.fields_by_name['model_definition']._serialized_options = b'\342A\001\005\372A\"\n api.instill.tech/ModelDefinition'
  _MODEL.fields_by_name['configuration']._options = None
  _MODEL.fields_by_name['configuration']._serialized_options = b'\342A\001\005'
  _MODEL.fields_by_name['task']._options = None
  _MODEL.fields_by_name['task']._serialized_options = b'\342A\001\003'
  _MODEL.fields_by_name['state']._options = None
  _MODEL.fields_by_name['state']._serialized_options = b'\342A\001\003'
  _MODEL.fields_by_name['visibility']._options = None
  _MODEL.fields_by_name['visibility']._serialized_options = b'\342A\001\003'
  _MODEL.fields_by_name['user']._options = None
  _MODEL.fields_by_name['user']._serialized_options = b'\342A\001\003\372A\027\n\025api.instill.tech/User'
  _MODEL.fields_by_name['org']._options = None
  _MODEL.fields_by_name['org']._serialized_options = b'\342A\001\003\372A\037\n\035api.instill.tech/Organization'
  _MODEL.fields_by_name['create_time']._options = None
  _MODEL.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _MODEL.fields_by_name['update_time']._options = None
  _MODEL.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _MODEL._options = None
  _MODEL._serialized_options = b'\352A(\n\026api.instill.tech/Model\022\016models/{model}'
  _MODELCARD.fields_by_name['name']._options = None
  _MODELCARD.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _MODELCARD.fields_by_name['size']._options = None
  _MODELCARD.fields_by_name['size']._serialized_options = b'\342A\001\003'
  _MODELCARD.fields_by_name['type']._options = None
  _MODELCARD.fields_by_name['type']._serialized_options = b'\342A\001\003'
  _MODELCARD.fields_by_name['content']._options = None
  _MODELCARD.fields_by_name['content']._serialized_options = b'\342A\001\003'
  _MODELCARD.fields_by_name['encoding']._options = None
  _MODELCARD.fields_by_name['encoding']._serialized_options = b'\342A\001\003'
  _MODELCARD._options = None
  _MODELCARD._serialized_options = b'\352A3\n\032api.instill.tech/ModelCard\022\025models/{model}/readme'
  _LISTMODELSREQUEST.fields_by_name['page_size']._options = None
  _LISTMODELSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTMODELSREQUEST.fields_by_name['page_token']._options = None
  _LISTMODELSREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTMODELSREQUEST.fields_by_name['view']._options = None
  _LISTMODELSREQUEST.fields_by_name['view']._serialized_options = b'\342A\001\001'
  _CREATEMODELREQUEST.fields_by_name['model']._options = None
  _CREATEMODELREQUEST.fields_by_name['model']._serialized_options = b'\342A\001\002'
  _CREATEMODELRESPONSE.fields_by_name['operation']._options = None
  _CREATEMODELRESPONSE.fields_by_name['operation']._serialized_options = b'\342A\001\003'
  _CREATEMODELBINARYFILEUPLOADREQUEST.fields_by_name['model']._options = None
  _CREATEMODELBINARYFILEUPLOADREQUEST.fields_by_name['model']._serialized_options = b'\342A\001\002'
  _CREATEMODELBINARYFILEUPLOADREQUEST.fields_by_name['content']._options = None
  _CREATEMODELBINARYFILEUPLOADREQUEST.fields_by_name['content']._serialized_options = b'\342A\001\002'
  _CREATEMODELBINARYFILEUPLOADRESPONSE.fields_by_name['operation']._options = None
  _CREATEMODELBINARYFILEUPLOADRESPONSE.fields_by_name['operation']._serialized_options = b'\342A\001\003'
  _GETMODELREQUEST.fields_by_name['name']._options = None
  _GETMODELREQUEST.fields_by_name['name']._serialized_options = b'\222A\020\312>\r\372\002\nmodel.name\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _GETMODELREQUEST.fields_by_name['view']._options = None
  _GETMODELREQUEST.fields_by_name['view']._serialized_options = b'\342A\001\001'
  _UPDATEMODELREQUEST.fields_by_name['model']._options = None
  _UPDATEMODELREQUEST.fields_by_name['model']._serialized_options = b'\342A\001\002'
  _UPDATEMODELREQUEST.fields_by_name['update_mask']._options = None
  _UPDATEMODELREQUEST.fields_by_name['update_mask']._serialized_options = b'\342A\001\002'
  _DELETEMODELREQUEST.fields_by_name['name']._options = None
  _DELETEMODELREQUEST.fields_by_name['name']._serialized_options = b'\222A\020\312>\r\372\002\nmodel.name\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _LOOKUPMODELREQUEST.fields_by_name['permalink']._options = None
  _LOOKUPMODELREQUEST.fields_by_name['permalink']._serialized_options = b'\342A\001\002'
  _LOOKUPMODELREQUEST.fields_by_name['view']._options = None
  _LOOKUPMODELREQUEST.fields_by_name['view']._serialized_options = b'\342A\001\001'
  _RENAMEMODELREQUEST.fields_by_name['name']._options = None
  _RENAMEMODELREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _RENAMEMODELREQUEST.fields_by_name['new_model_id']._options = None
  _RENAMEMODELREQUEST.fields_by_name['new_model_id']._serialized_options = b'\342A\001\002'
  _PUBLISHMODELREQUEST.fields_by_name['name']._options = None
  _PUBLISHMODELREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _UNPUBLISHMODELREQUEST.fields_by_name['name']._options = None
  _UNPUBLISHMODELREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _DEPLOYMODELREQUEST.fields_by_name['name']._options = None
  _DEPLOYMODELREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _UNDEPLOYMODELREQUEST.fields_by_name['name']._options = None
  _UNDEPLOYMODELREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _GETMODELCARDREQUEST.fields_by_name['name']._options = None
  _GETMODELCARDREQUEST.fields_by_name['name']._serialized_options = b'\222A\027\312>\024\372\002\021model.name/readme\342A\001\002\372A\034\n\032api.instill.tech/ModelCard'
  _WATCHMODELREQUEST.fields_by_name['name']._options = None
  _WATCHMODELREQUEST.fields_by_name['name']._serialized_options = b'\222A\026\312>\023\372\002\020model.name/watch\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _TASKOUTPUT.fields_by_name['classification']._options = None
  _TASKOUTPUT.fields_by_name['classification']._serialized_options = b'\342A\001\003'
  _TASKOUTPUT.fields_by_name['detection']._options = None
  _TASKOUTPUT.fields_by_name['detection']._serialized_options = b'\342A\001\003'
  _TASKOUTPUT.fields_by_name['keypoint']._options = None
  _TASKOUTPUT.fields_by_name['keypoint']._serialized_options = b'\342A\001\003'
  _TASKOUTPUT.fields_by_name['ocr']._options = None
  _TASKOUTPUT.fields_by_name['ocr']._serialized_options = b'\342A\001\003'
  _TASKOUTPUT.fields_by_name['instance_segmentation']._options = None
  _TASKOUTPUT.fields_by_name['instance_segmentation']._serialized_options = b'\342A\001\003'
  _TASKOUTPUT.fields_by_name['semantic_segmentation']._options = None
  _TASKOUTPUT.fields_by_name['semantic_segmentation']._serialized_options = b'\342A\001\003'
  _TASKOUTPUT.fields_by_name['text_to_image']._options = None
  _TASKOUTPUT.fields_by_name['text_to_image']._serialized_options = b'\342A\001\003'
  _TASKOUTPUT.fields_by_name['text_generation']._options = None
  _TASKOUTPUT.fields_by_name['text_generation']._serialized_options = b'\342A\001\003'
  _TASKOUTPUT.fields_by_name['unspecified']._options = None
  _TASKOUTPUT.fields_by_name['unspecified']._serialized_options = b'\342A\001\003'
  _TRIGGERMODELREQUEST.fields_by_name['name']._options = None
  _TRIGGERMODELREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _TRIGGERMODELREQUEST.fields_by_name['task_inputs']._options = None
  _TRIGGERMODELREQUEST.fields_by_name['task_inputs']._serialized_options = b'\342A\001\002'
  _TRIGGERMODELBINARYFILEUPLOADREQUEST.fields_by_name['name']._options = None
  _TRIGGERMODELBINARYFILEUPLOADREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _TRIGGERMODELBINARYFILEUPLOADREQUEST.fields_by_name['task_input']._options = None
  _TRIGGERMODELBINARYFILEUPLOADREQUEST.fields_by_name['task_input']._serialized_options = b'\342A\001\002'
  _TRIGGERMODELBINARYFILEUPLOADRESPONSE.fields_by_name['task']._options = None
  _TRIGGERMODELBINARYFILEUPLOADRESPONSE.fields_by_name['task']._serialized_options = b'\342A\001\002'
  _TRIGGERMODELBINARYFILEUPLOADRESPONSE.fields_by_name['task_outputs']._options = None
  _TRIGGERMODELBINARYFILEUPLOADRESPONSE.fields_by_name['task_outputs']._serialized_options = b'\342A\001\002'
  _TESTMODELREQUEST.fields_by_name['name']._options = None
  _TESTMODELREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _TESTMODELREQUEST.fields_by_name['task_inputs']._options = None
  _TESTMODELREQUEST.fields_by_name['task_inputs']._serialized_options = b'\342A\001\002'
  _TESTMODELRESPONSE.fields_by_name['task']._options = None
  _TESTMODELRESPONSE.fields_by_name['task']._serialized_options = b'\342A\001\002'
  _TESTMODELRESPONSE.fields_by_name['task_outputs']._options = None
  _TESTMODELRESPONSE.fields_by_name['task_outputs']._serialized_options = b'\342A\001\002'
  _TESTMODELBINARYFILEUPLOADREQUEST.fields_by_name['name']._options = None
  _TESTMODELBINARYFILEUPLOADREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002\372A\030\n\026api.instill.tech/Model'
  _TESTMODELBINARYFILEUPLOADREQUEST.fields_by_name['task_input']._options = None
  _TESTMODELBINARYFILEUPLOADREQUEST.fields_by_name['task_input']._serialized_options = b'\342A\001\002'
  _TESTMODELBINARYFILEUPLOADRESPONSE.fields_by_name['task']._options = None
  _TESTMODELBINARYFILEUPLOADRESPONSE.fields_by_name['task']._serialized_options = b'\342A\001\002'
  _TESTMODELBINARYFILEUPLOADRESPONSE.fields_by_name['task_outputs']._options = None
  _TESTMODELBINARYFILEUPLOADRESPONSE.fields_by_name['task_outputs']._serialized_options = b'\342A\001\002'
  _GETMODELOPERATIONREQUEST.fields_by_name['name']._options = None
  _GETMODELOPERATIONREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _GETMODELOPERATIONREQUEST.fields_by_name['view']._options = None
  _GETMODELOPERATIONREQUEST.fields_by_name['view']._serialized_options = b'\342A\001\001'
  _LISTMODELSADMINREQUEST.fields_by_name['page_size']._options = None
  _LISTMODELSADMINREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTMODELSADMINREQUEST.fields_by_name['page_token']._options = None
  _LISTMODELSADMINREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTMODELSADMINREQUEST.fields_by_name['view']._options = None
  _LISTMODELSADMINREQUEST.fields_by_name['view']._serialized_options = b'\342A\001\001'
  _LOOKUPMODELADMINREQUEST.fields_by_name['permalink']._options = None
  _LOOKUPMODELADMINREQUEST.fields_by_name['permalink']._serialized_options = b'\342A\001\002'
  _LOOKUPMODELADMINREQUEST.fields_by_name['view']._options = None
  _LOOKUPMODELADMINREQUEST.fields_by_name['view']._serialized_options = b'\342A\001\001'
  _CHECKMODELREQUEST.fields_by_name['model_permalink']._options = None
  _CHECKMODELREQUEST.fields_by_name['model_permalink']._serialized_options = b'\342A\001\002'
  _globals['_LIVENESSREQUEST']._serialized_start=801
  _globals['_LIVENESSREQUEST']._serialized_end=952
  _globals['_LIVENESSRESPONSE']._serialized_start=954
  _globals['_LIVENESSRESPONSE']._serialized_end=1073
  _globals['_READINESSREQUEST']._serialized_start=1076
  _globals['_READINESSREQUEST']._serialized_end=1228
  _globals['_READINESSRESPONSE']._serialized_start=1230
  _globals['_READINESSRESPONSE']._serialized_end=1350
  _globals['_MODEL']._serialized_start=1353
  _globals['_MODEL']._serialized_end=2546
  _globals['_MODEL_VISIBILITY']._serialized_start=2080
  _globals['_MODEL_VISIBILITY']._serialized_end=2167
  _globals['_MODEL_TASK']._serialized_start=2170
  _globals['_MODEL_TASK']._serialized_end=2390
  _globals['_MODEL_STATE']._serialized_start=2392
  _globals['_MODEL_STATE']._serialized_end=2476
  _globals['_MODELCARD']._serialized_start=2549
  _globals['_MODELCARD']._serialized_end=2760
  _globals['_LISTMODELSREQUEST']._serialized_start=2763
  _globals['_LISTMODELSREQUEST']._serialized_end=2960
  _globals['_LISTMODELSRESPONSE']._serialized_start=2963
  _globals['_LISTMODELSRESPONSE']._serialized_end=3106
  _globals['_CREATEMODELREQUEST']._serialized_start=3108
  _globals['_CREATEMODELREQUEST']._serialized_end=3184
  _globals['_CREATEMODELRESPONSE']._serialized_start=3186
  _globals['_CREATEMODELRESPONSE']._serialized_end=3274
  _globals['_CREATEMODELBINARYFILEUPLOADREQUEST']._serialized_start=3276
  _globals['_CREATEMODELBINARYFILEUPLOADREQUEST']._serialized_end=3400
  _globals['_CREATEMODELBINARYFILEUPLOADRESPONSE']._serialized_start=3402
  _globals['_CREATEMODELBINARYFILEUPLOADRESPONSE']._serialized_end=3506
  _globals['_GETMODELREQUEST']._serialized_start=3509
  _globals['_GETMODELREQUEST']._serialized_end=3665
  _globals['_GETMODELRESPONSE']._serialized_start=3667
  _globals['_GETMODELRESPONSE']._serialized_end=3735
  _globals['_UPDATEMODELREQUEST']._serialized_start=3738
  _globals['_UPDATEMODELREQUEST']._serialized_end=3881
  _globals['_UPDATEMODELRESPONSE']._serialized_start=3883
  _globals['_UPDATEMODELRESPONSE']._serialized_end=3954
  _globals['_DELETEMODELREQUEST']._serialized_start=3956
  _globals['_DELETEMODELREQUEST']._serialized_end=4048
  _globals['_DELETEMODELRESPONSE']._serialized_start=4050
  _globals['_DELETEMODELRESPONSE']._serialized_end=4071
  _globals['_LOOKUPMODELREQUEST']._serialized_start=4073
  _globals['_LOOKUPMODELREQUEST']._serialized_end=4196
  _globals['_LOOKUPMODELRESPONSE']._serialized_start=4198
  _globals['_LOOKUPMODELRESPONSE']._serialized_end=4269
  _globals['_RENAMEMODELREQUEST']._serialized_start=4271
  _globals['_RENAMEMODELREQUEST']._serialized_end=4384
  _globals['_RENAMEMODELRESPONSE']._serialized_start=4386
  _globals['_RENAMEMODELRESPONSE']._serialized_end=4457
  _globals['_PUBLISHMODELREQUEST']._serialized_start=4459
  _globals['_PUBLISHMODELREQUEST']._serialized_end=4533
  _globals['_PUBLISHMODELRESPONSE']._serialized_start=4535
  _globals['_PUBLISHMODELRESPONSE']._serialized_end=4607
  _globals['_UNPUBLISHMODELREQUEST']._serialized_start=4609
  _globals['_UNPUBLISHMODELREQUEST']._serialized_end=4685
  _globals['_UNPUBLISHMODELRESPONSE']._serialized_start=4687
  _globals['_UNPUBLISHMODELRESPONSE']._serialized_end=4761
  _globals['_DEPLOYMODELREQUEST']._serialized_start=4763
  _globals['_DEPLOYMODELREQUEST']._serialized_end=4836
  _globals['_DEPLOYMODELRESPONSE']._serialized_start=4838
  _globals['_DEPLOYMODELRESPONSE']._serialized_end=4920
  _globals['_UNDEPLOYMODELREQUEST']._serialized_start=4922
  _globals['_UNDEPLOYMODELREQUEST']._serialized_end=4997
  _globals['_UNDEPLOYMODELRESPONSE']._serialized_start=4999
  _globals['_UNDEPLOYMODELRESPONSE']._serialized_end=5083
  _globals['_GETMODELCARDREQUEST']._serialized_start=5085
  _globals['_GETMODELCARDREQUEST']._serialized_end=5189
  _globals['_GETMODELCARDRESPONSE']._serialized_start=5191
  _globals['_GETMODELCARDRESPONSE']._serialized_end=5269
  _globals['_WATCHMODELREQUEST']._serialized_start=5271
  _globals['_WATCHMODELREQUEST']._serialized_end=5368
  _globals['_WATCHMODELRESPONSE']._serialized_start=5370
  _globals['_WATCHMODELRESPONSE']._serialized_end=5474
  _globals['_TASKINPUT']._serialized_start=5477
  _globals['_TASKINPUT']._serialized_end=6210
  _globals['_TASKINPUTSTREAM']._serialized_start=6213
  _globals['_TASKINPUTSTREAM']._serialized_end=6988
  _globals['_TASKOUTPUT']._serialized_start=6991
  _globals['_TASKOUTPUT']._serialized_end=7789
  _globals['_TRIGGERMODELREQUEST']._serialized_start=7792
  _globals['_TRIGGERMODELREQUEST']._serialized_end=7937
  _globals['_TRIGGERMODELRESPONSE']._serialized_start=7940
  _globals['_TRIGGERMODELRESPONSE']._serialized_end=8083
  _globals['_TRIGGERMODELBINARYFILEUPLOADREQUEST']._serialized_start=8086
  _globals['_TRIGGERMODELBINARYFILEUPLOADREQUEST']._serialized_end=8251
  _globals['_TRIGGERMODELBINARYFILEUPLOADRESPONSE']._serialized_start=8254
  _globals['_TRIGGERMODELBINARYFILEUPLOADRESPONSE']._serialized_end=8425
  _globals['_TESTMODELREQUEST']._serialized_start=8428
  _globals['_TESTMODELREQUEST']._serialized_end=8570
  _globals['_TESTMODELRESPONSE']._serialized_start=8573
  _globals['_TESTMODELRESPONSE']._serialized_end=8725
  _globals['_TESTMODELBINARYFILEUPLOADREQUEST']._serialized_start=8728
  _globals['_TESTMODELBINARYFILEUPLOADREQUEST']._serialized_end=8890
  _globals['_TESTMODELBINARYFILEUPLOADRESPONSE']._serialized_start=8893
  _globals['_TESTMODELBINARYFILEUPLOADRESPONSE']._serialized_end=9061
  _globals['_GETMODELOPERATIONREQUEST']._serialized_start=9063
  _globals['_GETMODELOPERATIONREQUEST']._serialized_end=9182
  _globals['_GETMODELOPERATIONRESPONSE']._serialized_start=9184
  _globals['_GETMODELOPERATIONRESPONSE']._serialized_end=9272
  _globals['_LISTMODELSADMINREQUEST']._serialized_start=9275
  _globals['_LISTMODELSADMINREQUEST']._serialized_end=9477
  _globals['_LISTMODELSADMINRESPONSE']._serialized_start=9480
  _globals['_LISTMODELSADMINRESPONSE']._serialized_end=9628
  _globals['_LOOKUPMODELADMINREQUEST']._serialized_start=9631
  _globals['_LOOKUPMODELADMINREQUEST']._serialized_end=9759
  _globals['_LOOKUPMODELADMINRESPONSE']._serialized_start=9761
  _globals['_LOOKUPMODELADMINRESPONSE']._serialized_end=9837
  _globals['_CHECKMODELREQUEST']._serialized_start=9839
  _globals['_CHECKMODELREQUEST']._serialized_end=9905
  _globals['_CHECKMODELRESPONSE']._serialized_start=9907
  _globals['_CHECKMODELRESPONSE']._serialized_end=9983
# @@protoc_insertion_point(module_scope)