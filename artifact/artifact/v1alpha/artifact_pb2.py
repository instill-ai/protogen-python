# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: artifact/artifact/v1alpha/artifact.proto
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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(artifact/artifact/v1alpha/artifact.proto\x12\x19\x61rtifact.artifact.v1alpha\x1a+common/healthcheck/v1beta/healthcheck.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x96\x01\n\x0fLivenessRequest\x12j\n\x14health_check_request\x18\x01 \x01(\x0b\x32-.common.healthcheck.v1beta.HealthCheckRequestB\x04\xe2\x41\x01\x01H\x00R\x12healthCheckRequest\x88\x01\x01\x42\x17\n\x15_health_check_request\"v\n\x10LivenessResponse\x12\x62\n\x15health_check_response\x18\x01 \x01(\x0b\x32..common.healthcheck.v1beta.HealthCheckResponseR\x13healthCheckResponse\"\x97\x01\n\x10ReadinessRequest\x12j\n\x14health_check_request\x18\x01 \x01(\x0b\x32-.common.healthcheck.v1beta.HealthCheckRequestB\x04\xe2\x41\x01\x01H\x00R\x12healthCheckRequest\x88\x01\x01\x42\x17\n\x15_health_check_request\"w\n\x11ReadinessResponse\x12\x62\n\x15health_check_response\x18\x01 \x01(\x0b\x32..common.healthcheck.v1beta.HealthCheckResponseR\x13healthCheckResponse\"\xa1\x01\n\rRepositoryTag\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x05R\x04name\x12\x14\n\x02id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x05R\x02id\x12\x1c\n\x06\x64igest\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01R\x06\x64igest\x12\x42\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x05\xe2\x41\x02\x03\x01R\nupdateTime\"\xb7\x01\n\x19ListRepositoryTagsRequest\x12&\n\tpage_size\x18\x01 \x01(\x05\x42\x04\xe2\x41\x01\x01H\x00R\x08pageSize\x88\x01\x01\x12\x1d\n\x04page\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01H\x01R\x04page\x88\x01\x01\x12<\n\x06parent\x18\x03 \x01(\tB$\xe2\x41\x01\x02\xfa\x41\x1d\n\x1b\x61pi.instill.tech/RepositoryR\x06parentB\x0c\n\n_page_sizeB\x07\n\x05_page\"\xaa\x01\n\x1aListRepositoryTagsResponse\x12<\n\x04tags\x18\x01 \x03(\x0b\x32(.artifact.artifact.v1alpha.RepositoryTagR\x04tags\x12\x1d\n\ntotal_size\x18\x02 \x01(\x05R\ttotalSize\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x12\n\x04page\x18\x04 \x01(\x05R\x04page\"X\n\x1a\x43reateRepositoryTagRequest\x12:\n\x03tag\x18\x01 \x01(\x0b\x32(.artifact.artifact.v1alpha.RepositoryTagR\x03tag\"Y\n\x1b\x43reateRepositoryTagResponse\x12:\n\x03tag\x18\x01 \x01(\x0b\x32(.artifact.artifact.v1alpha.RepositoryTagR\x03tag\"6\n\x1a\x44\x65leteRepositoryTagRequest\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\"\x1d\n\x1b\x44\x65leteRepositoryTagResponse\"\x8d\x03\n\rKnowledgeBase\x12\x13\n\x05kb_id\x18\x01 \x01(\tR\x04kbId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1f\n\x0b\x63reate_time\x18\x05 \x01(\tR\ncreateTime\x12\x1f\n\x0bupdate_time\x18\x06 \x01(\tR\nupdateTime\x12\x1d\n\nowner_name\x18\x07 \x01(\tR\townerName\x12\x12\n\x04tags\x18\x08 \x03(\tR\x04tags\x12\x31\n\x14\x63onverting_pipelines\x18\t \x03(\tR\x13\x63onvertingPipelines\x12/\n\x13splitting_pipelines\x18\n \x03(\tR\x12splittingPipelines\x12/\n\x13\x65mbedding_pipelines\x18\x0b \x03(\tR\x12\x65mbeddingPipelines\x12\'\n\x0f\x64ownstream_apps\x18\x0c \x03(\tR\x0e\x64ownstreamApps\"\x81\x01\n\x1a\x43reateKnowledgeBaseRequest\x12\x19\n\x08owner_id\x18\x01 \x01(\tR\x07ownerId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04tags\x18\x04 \x03(\tR\x04tags\"n\n\x1b\x43reateKnowledgeBaseResponse\x12O\n\x0eknowledge_base\x18\x01 \x01(\x0b\x32(.artifact.artifact.v1alpha.KnowledgeBaseR\rknowledgeBase\"6\n\x19ListKnowledgeBasesRequest\x12\x19\n\x08owner_id\x18\x01 \x01(\tR\x07ownerId\"o\n\x1aListKnowledgeBasesResponse\x12Q\n\x0fknowledge_bases\x18\x01 \x03(\x0b\x32(.artifact.artifact.v1alpha.KnowledgeBaseR\x0eknowledgeBases\"\x82\x01\n\x1aUpdateKnowledgeBaseRequest\x12\x13\n\x05kb_id\x18\x01 \x01(\tR\x04kbId\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04tags\x18\x03 \x03(\tR\x04tags\x12\x19\n\x08owner_id\x18\x04 \x01(\tR\x07ownerId\"n\n\x1bUpdateKnowledgeBaseResponse\x12O\n\x0eknowledge_base\x18\x01 \x01(\x0b\x32(.artifact.artifact.v1alpha.KnowledgeBaseR\rknowledgeBase\"L\n\x1a\x44\x65leteKnowledgeBaseRequest\x12\x19\n\x08owner_id\x18\x01 \x01(\tR\x07ownerId\x12\x13\n\x05kb_id\x18\x02 \x01(\tR\x04kbId\"n\n\x1b\x44\x65leteKnowledgeBaseResponse\x12O\n\x0eknowledge_base\x18\x01 \x01(\x0b\x32(.artifact.artifact.v1alpha.KnowledgeBaseR\rknowledgeBase\"\x82\x05\n\x04\x46ile\x12\x1f\n\x08\x66ile_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x07\x66ileUid\x12\x18\n\x04name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x04name\x12=\n\x04type\x18\x03 \x01(\x0e\x32#.artifact.artifact.v1alpha.FileTypeB\x04\xe2\x41\x01\x02R\x04type\x12Y\n\x0eprocess_status\x18\x04 \x01(\x0e\x32,.artifact.artifact.v1alpha.FileProcessStatusB\x04\xe2\x41\x01\x03R\rprocessStatus\x12-\n\x0fprocess_outcome\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\x0eprocessOutcome\x12&\n\x0bretrievable\x18\x06 \x01(\x08\x42\x04\xe2\x41\x01\x03R\x0bretrievable\x12\x1e\n\x07\x63ontent\x18\x07 \x01(\tB\x04\xe2\x41\x01\x01R\x07\x63ontent\x12!\n\towner_uid\x18\x08 \x01(\tB\x04\xe2\x41\x01\x03R\x08ownerUid\x12%\n\x0b\x63reator_uid\x18\t \x01(\tB\x04\xe2\x41\x01\x03R\ncreatorUid\x12\x1b\n\x06kb_uid\x18\n \x01(\tB\x04\xe2\x41\x01\x03R\x05kbUid\x12\x41\n\x0b\x63reate_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12\x41\n\x0b\x64\x65lete_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ndeleteTime\"\x91\x01\n\x1eUploadKnowledgeBaseFileRequest\x12\x1f\n\x08owner_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x07ownerId\x12\x19\n\x05kb_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x04kbId\x12\x33\n\x04\x66ile\x18\x03 \x01(\x0b\x32\x1f.artifact.artifact.v1alpha.FileR\x04\x66ile\"V\n\x1fUploadKnowledgeBaseFileResponse\x12\x33\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x1f.artifact.artifact.v1alpha.FileR\x04\x66ile\"A\n\x1e\x44\x65leteKnowledgeBaseFileRequest\x12\x1f\n\x08\x66ile_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x07\x66ileUid\"<\n\x1f\x44\x65leteKnowledgeBaseFileResponse\x12\x19\n\x08\x66ile_uid\x18\x01 \x01(\tR\x07\x66ileUid\"E\n ProcessKnowledgeBaseFilesRequest\x12!\n\tfile_uids\x18\x01 \x03(\tB\x04\xe2\x41\x01\x02R\x08\x66ileUids\"Z\n!ProcessKnowledgeBaseFilesResponse\x12\x35\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x1f.artifact.artifact.v1alpha.FileR\x05\x66iles\"A\n\x1cListKnowledgeBaseFilesFilter\x12!\n\tfile_uids\x18\x02 \x03(\tB\x04\xe2\x41\x01\x01R\x08\x66ileUids\"\xee\x01\n\x1dListKnowledgeBaseFilesRequest\x12\x19\n\x08owner_id\x18\x01 \x01(\tR\x07ownerId\x12\x13\n\x05kb_id\x18\x02 \x01(\tR\x04kbId\x12!\n\tpage_size\x18\x03 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\x12U\n\x06\x66ilter\x18\x05 \x01(\x0b\x32\x37.artifact.artifact.v1alpha.ListKnowledgeBaseFilesFilterB\x04\xe2\x41\x01\x01R\x06\x66ilter\"\x8c\x02\n\x1eListKnowledgeBaseFilesResponse\x12\x35\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x1f.artifact.artifact.v1alpha.FileR\x05\x66iles\x12\x1d\n\ntotal_size\x18\x02 \x01(\x05R\ttotalSize\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12&\n\x0fnext_page_token\x18\x04 \x01(\tR\rnextPageToken\x12O\n\x06\x66ilter\x18\x05 \x01(\x0b\x32\x37.artifact.artifact.v1alpha.ListKnowledgeBaseFilesFilterR\x06\x66ilter*\x89\x02\n\x11\x46ileProcessStatus\x12#\n\x1f\x46ILE_PROCESS_STATUS_UNSPECIFIED\x10\x00\x12\"\n\x1e\x46ILE_PROCESS_STATUS_NOTSTARTED\x10\x01\x12\x1f\n\x1b\x46ILE_PROCESS_STATUS_WAITING\x10\x02\x12\"\n\x1e\x46ILE_PROCESS_STATUS_CONVERTING\x10\x03\x12 \n\x1c\x46ILE_PROCESS_STATUS_CHUNKING\x10\x04\x12!\n\x1d\x46ILE_PROCESS_STATUS_EMBEDDING\x10\x05\x12!\n\x1d\x46ILE_PROCESS_STATUS_COMPLETED\x10\x06*\x9e\x01\n\x08\x46ileType\x12\x19\n\x15\x46ILE_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x46ILE_TYPE_TEXT\x10\x01\x12\x11\n\rFILE_TYPE_PDF\x10\x02\x12\x16\n\x12\x46ILE_TYPE_MARKDOWN\x10\x03\x12\x11\n\rFILE_TYPE_PNG\x10\x04\x12\x12\n\x0e\x46ILE_TYPE_JPEG\x10\x05\x12\x11\n\rFILE_TYPE_JPG\x10\x06\x42\x81\x02\n\x1d\x63om.artifact.artifact.v1alphaB\rArtifactProtoP\x01ZKgithub.com/instill-ai/protogen-go/artifact/artifact/v1alpha;artifactv1alpha\xa2\x02\x03\x41\x41X\xaa\x02\x19\x41rtifact.Artifact.V1alpha\xca\x02\x19\x41rtifact\\Artifact\\V1alpha\xe2\x02%Artifact\\Artifact\\V1alpha\\GPBMetadata\xea\x02\x1b\x41rtifact::Artifact::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'artifact.artifact.v1alpha.artifact_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.artifact.artifact.v1alphaB\rArtifactProtoP\001ZKgithub.com/instill-ai/protogen-go/artifact/artifact/v1alpha;artifactv1alpha\242\002\003AAX\252\002\031Artifact.Artifact.V1alpha\312\002\031Artifact\\Artifact\\V1alpha\342\002%Artifact\\Artifact\\V1alpha\\GPBMetadata\352\002\033Artifact::Artifact::V1alpha'
  _LIVENESSREQUEST.fields_by_name['health_check_request']._options = None
  _LIVENESSREQUEST.fields_by_name['health_check_request']._serialized_options = b'\342A\001\001'
  _READINESSREQUEST.fields_by_name['health_check_request']._options = None
  _READINESSREQUEST.fields_by_name['health_check_request']._serialized_options = b'\342A\001\001'
  _REPOSITORYTAG.fields_by_name['name']._options = None
  _REPOSITORYTAG.fields_by_name['name']._serialized_options = b'\342A\001\005'
  _REPOSITORYTAG.fields_by_name['id']._options = None
  _REPOSITORYTAG.fields_by_name['id']._serialized_options = b'\342A\001\005'
  _REPOSITORYTAG.fields_by_name['digest']._options = None
  _REPOSITORYTAG.fields_by_name['digest']._serialized_options = b'\342A\001\001'
  _REPOSITORYTAG.fields_by_name['update_time']._options = None
  _REPOSITORYTAG.fields_by_name['update_time']._serialized_options = b'\342A\002\003\001'
  _LISTREPOSITORYTAGSREQUEST.fields_by_name['page_size']._options = None
  _LISTREPOSITORYTAGSREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTREPOSITORYTAGSREQUEST.fields_by_name['page']._options = None
  _LISTREPOSITORYTAGSREQUEST.fields_by_name['page']._serialized_options = b'\342A\001\001'
  _LISTREPOSITORYTAGSREQUEST.fields_by_name['parent']._options = None
  _LISTREPOSITORYTAGSREQUEST.fields_by_name['parent']._serialized_options = b'\342A\001\002\372A\035\n\033api.instill.tech/Repository'
  _DELETEREPOSITORYTAGREQUEST.fields_by_name['name']._options = None
  _DELETEREPOSITORYTAGREQUEST.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _FILE.fields_by_name['file_uid']._options = None
  _FILE.fields_by_name['file_uid']._serialized_options = b'\342A\001\003'
  _FILE.fields_by_name['name']._options = None
  _FILE.fields_by_name['name']._serialized_options = b'\342A\001\002'
  _FILE.fields_by_name['type']._options = None
  _FILE.fields_by_name['type']._serialized_options = b'\342A\001\002'
  _FILE.fields_by_name['process_status']._options = None
  _FILE.fields_by_name['process_status']._serialized_options = b'\342A\001\003'
  _FILE.fields_by_name['process_outcome']._options = None
  _FILE.fields_by_name['process_outcome']._serialized_options = b'\342A\001\003'
  _FILE.fields_by_name['retrievable']._options = None
  _FILE.fields_by_name['retrievable']._serialized_options = b'\342A\001\003'
  _FILE.fields_by_name['content']._options = None
  _FILE.fields_by_name['content']._serialized_options = b'\342A\001\001'
  _FILE.fields_by_name['owner_uid']._options = None
  _FILE.fields_by_name['owner_uid']._serialized_options = b'\342A\001\003'
  _FILE.fields_by_name['creator_uid']._options = None
  _FILE.fields_by_name['creator_uid']._serialized_options = b'\342A\001\003'
  _FILE.fields_by_name['kb_uid']._options = None
  _FILE.fields_by_name['kb_uid']._serialized_options = b'\342A\001\003'
  _FILE.fields_by_name['create_time']._options = None
  _FILE.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _FILE.fields_by_name['update_time']._options = None
  _FILE.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _FILE.fields_by_name['delete_time']._options = None
  _FILE.fields_by_name['delete_time']._serialized_options = b'\342A\001\003'
  _UPLOADKNOWLEDGEBASEFILEREQUEST.fields_by_name['owner_id']._options = None
  _UPLOADKNOWLEDGEBASEFILEREQUEST.fields_by_name['owner_id']._serialized_options = b'\342A\001\002'
  _UPLOADKNOWLEDGEBASEFILEREQUEST.fields_by_name['kb_id']._options = None
  _UPLOADKNOWLEDGEBASEFILEREQUEST.fields_by_name['kb_id']._serialized_options = b'\342A\001\002'
  _DELETEKNOWLEDGEBASEFILEREQUEST.fields_by_name['file_uid']._options = None
  _DELETEKNOWLEDGEBASEFILEREQUEST.fields_by_name['file_uid']._serialized_options = b'\342A\001\002'
  _PROCESSKNOWLEDGEBASEFILESREQUEST.fields_by_name['file_uids']._options = None
  _PROCESSKNOWLEDGEBASEFILESREQUEST.fields_by_name['file_uids']._serialized_options = b'\342A\001\002'
  _LISTKNOWLEDGEBASEFILESFILTER.fields_by_name['file_uids']._options = None
  _LISTKNOWLEDGEBASEFILESFILTER.fields_by_name['file_uids']._serialized_options = b'\342A\001\001'
  _LISTKNOWLEDGEBASEFILESREQUEST.fields_by_name['page_size']._options = None
  _LISTKNOWLEDGEBASEFILESREQUEST.fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _LISTKNOWLEDGEBASEFILESREQUEST.fields_by_name['page_token']._options = None
  _LISTKNOWLEDGEBASEFILESREQUEST.fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _LISTKNOWLEDGEBASEFILESREQUEST.fields_by_name['filter']._options = None
  _LISTKNOWLEDGEBASEFILESREQUEST.fields_by_name['filter']._serialized_options = b'\342A\001\001'
  _globals['_FILEPROCESSSTATUS']._serialized_start=4549
  _globals['_FILEPROCESSSTATUS']._serialized_end=4814
  _globals['_FILETYPE']._serialized_start=4817
  _globals['_FILETYPE']._serialized_end=4975
  _globals['_LIVENESSREQUEST']._serialized_start=210
  _globals['_LIVENESSREQUEST']._serialized_end=360
  _globals['_LIVENESSRESPONSE']._serialized_start=362
  _globals['_LIVENESSRESPONSE']._serialized_end=480
  _globals['_READINESSREQUEST']._serialized_start=483
  _globals['_READINESSREQUEST']._serialized_end=634
  _globals['_READINESSRESPONSE']._serialized_start=636
  _globals['_READINESSRESPONSE']._serialized_end=755
  _globals['_REPOSITORYTAG']._serialized_start=758
  _globals['_REPOSITORYTAG']._serialized_end=919
  _globals['_LISTREPOSITORYTAGSREQUEST']._serialized_start=922
  _globals['_LISTREPOSITORYTAGSREQUEST']._serialized_end=1105
  _globals['_LISTREPOSITORYTAGSRESPONSE']._serialized_start=1108
  _globals['_LISTREPOSITORYTAGSRESPONSE']._serialized_end=1278
  _globals['_CREATEREPOSITORYTAGREQUEST']._serialized_start=1280
  _globals['_CREATEREPOSITORYTAGREQUEST']._serialized_end=1368
  _globals['_CREATEREPOSITORYTAGRESPONSE']._serialized_start=1370
  _globals['_CREATEREPOSITORYTAGRESPONSE']._serialized_end=1459
  _globals['_DELETEREPOSITORYTAGREQUEST']._serialized_start=1461
  _globals['_DELETEREPOSITORYTAGREQUEST']._serialized_end=1515
  _globals['_DELETEREPOSITORYTAGRESPONSE']._serialized_start=1517
  _globals['_DELETEREPOSITORYTAGRESPONSE']._serialized_end=1546
  _globals['_KNOWLEDGEBASE']._serialized_start=1549
  _globals['_KNOWLEDGEBASE']._serialized_end=1946
  _globals['_CREATEKNOWLEDGEBASEREQUEST']._serialized_start=1949
  _globals['_CREATEKNOWLEDGEBASEREQUEST']._serialized_end=2078
  _globals['_CREATEKNOWLEDGEBASERESPONSE']._serialized_start=2080
  _globals['_CREATEKNOWLEDGEBASERESPONSE']._serialized_end=2190
  _globals['_LISTKNOWLEDGEBASESREQUEST']._serialized_start=2192
  _globals['_LISTKNOWLEDGEBASESREQUEST']._serialized_end=2246
  _globals['_LISTKNOWLEDGEBASESRESPONSE']._serialized_start=2248
  _globals['_LISTKNOWLEDGEBASESRESPONSE']._serialized_end=2359
  _globals['_UPDATEKNOWLEDGEBASEREQUEST']._serialized_start=2362
  _globals['_UPDATEKNOWLEDGEBASEREQUEST']._serialized_end=2492
  _globals['_UPDATEKNOWLEDGEBASERESPONSE']._serialized_start=2494
  _globals['_UPDATEKNOWLEDGEBASERESPONSE']._serialized_end=2604
  _globals['_DELETEKNOWLEDGEBASEREQUEST']._serialized_start=2606
  _globals['_DELETEKNOWLEDGEBASEREQUEST']._serialized_end=2682
  _globals['_DELETEKNOWLEDGEBASERESPONSE']._serialized_start=2684
  _globals['_DELETEKNOWLEDGEBASERESPONSE']._serialized_end=2794
  _globals['_FILE']._serialized_start=2797
  _globals['_FILE']._serialized_end=3439
  _globals['_UPLOADKNOWLEDGEBASEFILEREQUEST']._serialized_start=3442
  _globals['_UPLOADKNOWLEDGEBASEFILEREQUEST']._serialized_end=3587
  _globals['_UPLOADKNOWLEDGEBASEFILERESPONSE']._serialized_start=3589
  _globals['_UPLOADKNOWLEDGEBASEFILERESPONSE']._serialized_end=3675
  _globals['_DELETEKNOWLEDGEBASEFILEREQUEST']._serialized_start=3677
  _globals['_DELETEKNOWLEDGEBASEFILEREQUEST']._serialized_end=3742
  _globals['_DELETEKNOWLEDGEBASEFILERESPONSE']._serialized_start=3744
  _globals['_DELETEKNOWLEDGEBASEFILERESPONSE']._serialized_end=3804
  _globals['_PROCESSKNOWLEDGEBASEFILESREQUEST']._serialized_start=3806
  _globals['_PROCESSKNOWLEDGEBASEFILESREQUEST']._serialized_end=3875
  _globals['_PROCESSKNOWLEDGEBASEFILESRESPONSE']._serialized_start=3877
  _globals['_PROCESSKNOWLEDGEBASEFILESRESPONSE']._serialized_end=3967
  _globals['_LISTKNOWLEDGEBASEFILESFILTER']._serialized_start=3969
  _globals['_LISTKNOWLEDGEBASEFILESFILTER']._serialized_end=4034
  _globals['_LISTKNOWLEDGEBASEFILESREQUEST']._serialized_start=4037
  _globals['_LISTKNOWLEDGEBASEFILESREQUEST']._serialized_end=4275
  _globals['_LISTKNOWLEDGEBASEFILESRESPONSE']._serialized_start=4278
  _globals['_LISTKNOWLEDGEBASEFILESRESPONSE']._serialized_end=4546
# @@protoc_insertion_point(module_scope)
