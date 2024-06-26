# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: artifact/artifact/v1alpha/artifact_public_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from artifact.artifact.v1alpha import artifact_pb2 as artifact_dot_artifact_dot_v1alpha_dot_artifact__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7artifact/artifact/v1alpha/artifact_public_service.proto\x12\x19\x61rtifact.artifact.v1alpha\x1a(artifact/artifact/v1alpha/artifact.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1bgoogle/api/visibility.proto\x1a.protoc-gen-openapiv2/options/annotations.proto2\x8d\x11\n\x15\x41rtifactPublicService\x12\xac\x01\n\x08Liveness\x12*.artifact.artifact.v1alpha.LivenessRequest\x1a+.artifact.artifact.v1alpha.LivenessResponse\"G\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x82\xd3\xe4\x93\x02\x31\x12\x13/v1alpha/__livenessZ\x1a\x12\x18/v1alpha/health/artifact\x12\xaf\x01\n\tReadiness\x12+.artifact.artifact.v1alpha.ReadinessRequest\x1a,.artifact.artifact.v1alpha.ReadinessResponse\"G\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL\x82\xd3\xe4\x93\x02\x31\x12\x14/v1alpha/__readinessZ\x19\x12\x17/v1alpha/ready/artifact\x12\xcd\x01\n\x13\x43reateKnowledgeBase\x12\x35.artifact.artifact.v1alpha.CreateKnowledgeBaseRequest\x1a\x36.artifact.artifact.v1alpha.CreateKnowledgeBaseResponse\"G\x92\x41\x0f\n\rKnowledgeBase\x82\xd3\xe4\x93\x02/\"*/v1alpha/owners/{owner_id}/knowledge-bases:\x01*\x12\xc7\x01\n\x12ListKnowledgeBases\x12\x34.artifact.artifact.v1alpha.ListKnowledgeBasesRequest\x1a\x35.artifact.artifact.v1alpha.ListKnowledgeBasesResponse\"D\x92\x41\x0f\n\rKnowledgeBase\x82\xd3\xe4\x93\x02,\x12*/v1alpha/owners/{owner_id}/knowledge-bases\x12\xd5\x01\n\x13UpdateKnowledgeBase\x12\x35.artifact.artifact.v1alpha.UpdateKnowledgeBaseRequest\x1a\x36.artifact.artifact.v1alpha.UpdateKnowledgeBaseResponse\"O\x92\x41\x0f\n\rKnowledgeBase\x82\xd3\xe4\x93\x02\x37\x1a\x32/v1alpha/owners/{owner_id}/knowledge-bases/{kb_id}:\x01*\x12\xd2\x01\n\x13\x44\x65leteKnowledgeBase\x12\x35.artifact.artifact.v1alpha.DeleteKnowledgeBaseRequest\x1a\x36.artifact.artifact.v1alpha.DeleteKnowledgeBaseResponse\"L\x92\x41\x0f\n\rKnowledgeBase\x82\xd3\xe4\x93\x02\x34*2/v1alpha/owners/{owner_id}/knowledge-bases/{kb_id}\x12\x80\x02\n\x17UploadKnowledgeBaseFile\x12\x39.artifact.artifact.v1alpha.UploadKnowledgeBaseFileRequest\x1a:.artifact.artifact.v1alpha.UploadKnowledgeBaseFileResponse\"n\x92\x41\x0f\n\rKnowledgeBase\xda\x41\x13owner_id,kb_id,file\x82\xd3\xe4\x93\x02@\"8/v1alpha/owners/{owner_id}/knowledge-bases/{kb_id}/files:\x04\x66ile\x12\xd5\x01\n\x17\x44\x65leteKnowledgeBaseFile\x12\x39.artifact.artifact.v1alpha.DeleteKnowledgeBaseFileRequest\x1a:.artifact.artifact.v1alpha.DeleteKnowledgeBaseFileResponse\"C\x92\x41\x0f\n\rKnowledgeBase\xda\x41\x08\x66ile_uid\x82\xd3\xe4\x93\x02 *\x1e/v1alpha/knowledge-bases/files\x12\xec\x01\n\x19ProcessKnowledgeBaseFiles\x12;.artifact.artifact.v1alpha.ProcessKnowledgeBaseFilesRequest\x1a<.artifact.artifact.v1alpha.ProcessKnowledgeBaseFilesResponse\"T\x92\x41\x0f\n\rKnowledgeBase\xda\x41\tfile_uids\x82\xd3\xe4\x93\x02\x30\"+/v1alpha/knowledge-bases/files/processAsync:\x01*\x12\xe1\x01\n\x16ListKnowledgeBaseFiles\x12\x38.artifact.artifact.v1alpha.ListKnowledgeBaseFilesRequest\x1a\x39.artifact.artifact.v1alpha.ListKnowledgeBaseFilesResponse\"R\x92\x41\x0f\n\rKnowledgeBase\x82\xd3\xe4\x93\x02:\x12\x38/v1alpha/owners/{owner_id}/knowledge-bases/{kb_id}/files\x1a\x1e\x92\x41\x1b\x12\x19Public Artifact endpointsB\x8e\x02\n\x1d\x63om.artifact.artifact.v1alphaB\x1a\x41rtifactPublicServiceProtoP\x01ZKgithub.com/instill-ai/protogen-go/artifact/artifact/v1alpha;artifactv1alpha\xa2\x02\x03\x41\x41X\xaa\x02\x19\x41rtifact.Artifact.V1alpha\xca\x02\x19\x41rtifact\\Artifact\\V1alpha\xe2\x02%Artifact\\Artifact\\V1alpha\\GPBMetadata\xea\x02\x1b\x41rtifact::Artifact::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'artifact.artifact.v1alpha.artifact_public_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.artifact.artifact.v1alphaB\032ArtifactPublicServiceProtoP\001ZKgithub.com/instill-ai/protogen-go/artifact/artifact/v1alpha;artifactv1alpha\242\002\003AAX\252\002\031Artifact.Artifact.V1alpha\312\002\031Artifact\\Artifact\\V1alpha\342\002%Artifact\\Artifact\\V1alpha\\GPBMetadata\352\002\033Artifact::Artifact::V1alpha'
  _ARTIFACTPUBLICSERVICE._options = None
  _ARTIFACTPUBLICSERVICE._serialized_options = b'\222A\033\022\031Public Artifact endpoints'
  _ARTIFACTPUBLICSERVICE.methods_by_name['Liveness']._options = None
  _ARTIFACTPUBLICSERVICE.methods_by_name['Liveness']._serialized_options = b'\372\322\344\223\002\n\022\010INTERNAL\202\323\344\223\0021\022\023/v1alpha/__livenessZ\032\022\030/v1alpha/health/artifact'
  _ARTIFACTPUBLICSERVICE.methods_by_name['Readiness']._options = None
  _ARTIFACTPUBLICSERVICE.methods_by_name['Readiness']._serialized_options = b'\372\322\344\223\002\n\022\010INTERNAL\202\323\344\223\0021\022\024/v1alpha/__readinessZ\031\022\027/v1alpha/ready/artifact'
  _ARTIFACTPUBLICSERVICE.methods_by_name['CreateKnowledgeBase']._options = None
  _ARTIFACTPUBLICSERVICE.methods_by_name['CreateKnowledgeBase']._serialized_options = b'\222A\017\n\rKnowledgeBase\202\323\344\223\002/\"*/v1alpha/owners/{owner_id}/knowledge-bases:\001*'
  _ARTIFACTPUBLICSERVICE.methods_by_name['ListKnowledgeBases']._options = None
  _ARTIFACTPUBLICSERVICE.methods_by_name['ListKnowledgeBases']._serialized_options = b'\222A\017\n\rKnowledgeBase\202\323\344\223\002,\022*/v1alpha/owners/{owner_id}/knowledge-bases'
  _ARTIFACTPUBLICSERVICE.methods_by_name['UpdateKnowledgeBase']._options = None
  _ARTIFACTPUBLICSERVICE.methods_by_name['UpdateKnowledgeBase']._serialized_options = b'\222A\017\n\rKnowledgeBase\202\323\344\223\0027\0322/v1alpha/owners/{owner_id}/knowledge-bases/{kb_id}:\001*'
  _ARTIFACTPUBLICSERVICE.methods_by_name['DeleteKnowledgeBase']._options = None
  _ARTIFACTPUBLICSERVICE.methods_by_name['DeleteKnowledgeBase']._serialized_options = b'\222A\017\n\rKnowledgeBase\202\323\344\223\0024*2/v1alpha/owners/{owner_id}/knowledge-bases/{kb_id}'
  _ARTIFACTPUBLICSERVICE.methods_by_name['UploadKnowledgeBaseFile']._options = None
  _ARTIFACTPUBLICSERVICE.methods_by_name['UploadKnowledgeBaseFile']._serialized_options = b'\222A\017\n\rKnowledgeBase\332A\023owner_id,kb_id,file\202\323\344\223\002@\"8/v1alpha/owners/{owner_id}/knowledge-bases/{kb_id}/files:\004file'
  _ARTIFACTPUBLICSERVICE.methods_by_name['DeleteKnowledgeBaseFile']._options = None
  _ARTIFACTPUBLICSERVICE.methods_by_name['DeleteKnowledgeBaseFile']._serialized_options = b'\222A\017\n\rKnowledgeBase\332A\010file_uid\202\323\344\223\002 *\036/v1alpha/knowledge-bases/files'
  _ARTIFACTPUBLICSERVICE.methods_by_name['ProcessKnowledgeBaseFiles']._options = None
  _ARTIFACTPUBLICSERVICE.methods_by_name['ProcessKnowledgeBaseFiles']._serialized_options = b'\222A\017\n\rKnowledgeBase\332A\tfile_uids\202\323\344\223\0020\"+/v1alpha/knowledge-bases/files/processAsync:\001*'
  _ARTIFACTPUBLICSERVICE.methods_by_name['ListKnowledgeBaseFiles']._options = None
  _ARTIFACTPUBLICSERVICE.methods_by_name['ListKnowledgeBaseFiles']._serialized_options = b'\222A\017\n\rKnowledgeBase\202\323\344\223\002:\0228/v1alpha/owners/{owner_id}/knowledge-bases/{kb_id}/files'
  _globals['_ARTIFACTPUBLICSERVICE']._serialized_start=261
  _globals['_ARTIFACTPUBLICSERVICE']._serialized_end=2450
# @@protoc_insertion_point(module_scope)
