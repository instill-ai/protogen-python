# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: artifact/artifact/v1alpha/qa.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from artifact.artifact.v1alpha import chunk_pb2 as artifact_dot_artifact_dot_v1alpha_dot_chunk__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"artifact/artifact/v1alpha/qa.proto\x12\x19\x61rtifact.artifact.v1alpha\x1a%artifact/artifact/v1alpha/chunk.proto\"\x8d\x01\n\x18QuestionAnsweringRequest\x12!\n\x0cnamespace_id\x18\x01 \x01(\tR\x0bnamespaceId\x12\x1d\n\ncatalog_id\x18\x02 \x01(\tR\tcatalogId\x12\x1a\n\x08question\x18\x03 \x01(\tR\x08question\x12\x13\n\x05top_k\x18\x04 \x01(\x05R\x04topK\"\x86\x01\n\x19QuestionAnsweringResponse\x12\x16\n\x06\x61nswer\x18\x01 \x01(\tR\x06\x61nswer\x12Q\n\x0esimilar_chunks\x18\x02 \x03(\x0b\x32*.artifact.artifact.v1alpha.SimilarityChunkR\rsimilarChunksB\xfb\x01\n\x1d\x63om.artifact.artifact.v1alphaB\x07QaProtoP\x01ZKgithub.com/instill-ai/protogen-go/artifact/artifact/v1alpha;artifactv1alpha\xa2\x02\x03\x41\x41X\xaa\x02\x19\x41rtifact.Artifact.V1alpha\xca\x02\x19\x41rtifact\\Artifact\\V1alpha\xe2\x02%Artifact\\Artifact\\V1alpha\\GPBMetadata\xea\x02\x1b\x41rtifact::Artifact::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'artifact.artifact.v1alpha.qa_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.artifact.artifact.v1alphaB\007QaProtoP\001ZKgithub.com/instill-ai/protogen-go/artifact/artifact/v1alpha;artifactv1alpha\242\002\003AAX\252\002\031Artifact.Artifact.V1alpha\312\002\031Artifact\\Artifact\\V1alpha\342\002%Artifact\\Artifact\\V1alpha\\GPBMetadata\352\002\033Artifact::Artifact::V1alpha'
  _globals['_QUESTIONANSWERINGREQUEST']._serialized_start=105
  _globals['_QUESTIONANSWERINGREQUEST']._serialized_end=246
  _globals['_QUESTIONANSWERINGRESPONSE']._serialized_start=249
  _globals['_QUESTIONANSWERINGRESPONSE']._serialized_end=383
# @@protoc_insertion_point(module_scope)
