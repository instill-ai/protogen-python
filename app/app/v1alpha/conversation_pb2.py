# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/app/v1alpha/conversation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"app/app/v1alpha/conversation.proto\x12\x0f\x61pp.app.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x82\x02\n\x0c\x43onversation\x12\x15\n\x03uid\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x03uid\x12&\n\x0cnamespace_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12\x1a\n\x06\x61pp_id\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x05\x61ppId\x12\x13\n\x02id\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x02id\x12@\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\ncreateTime\x12@\n\x0bupdate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\nupdateTime\"\xd8\x03\n\x07Message\x12\x15\n\x03uid\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x03uid\x12\x1c\n\x07\x61pp_uid\x18\x02 \x01(\tB\x03\xe0\x41\x03R\x06\x61ppUid\x12.\n\x10\x63onversation_uid\x18\x03 \x01(\tB\x03\xe0\x41\x03R\x0f\x63onversationUid\x12\x1d\n\x07\x63ontent\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x07\x63ontent\x12\x17\n\x04role\x18\x05 \x01(\tB\x03\xe0\x41\x02R\x04role\x12=\n\x04type\x18\x06 \x01(\x0e\x32$.app.app.v1alpha.Message.MessageTypeB\x03\xe0\x41\x02R\x04type\x12@\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\ncreateTime\x12@\n\x0bupdate_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x03R\nupdateTime\x12)\n\x0emsg_sender_uid\x18\t \x01(\tB\x03\xe0\x41\x03R\x0cmsgSenderUid\"B\n\x0bMessageType\x12\x1c\n\x18MESSAGE_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11MESSAGE_TYPE_TEXT\x10\x01\"\x8d\x01\n\x19\x43reateConversationRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12\x1a\n\x06\x61pp_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x05\x61ppId\x12,\n\x0f\x63onversation_id\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x0e\x63onversationId\"d\n\x1a\x43reateConversationResponse\x12\x46\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x1d.app.app.v1alpha.ConversationB\x03\xe0\x41\x03R\x0c\x63onversation\"\xee\x01\n\x18ListConversationsRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12\x1a\n\x06\x61pp_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x05\x61ppId\x12 \n\tpage_size\x18\x03 \x01(\x05\x42\x03\xe0\x41\x01R\x08pageSize\x12\"\n\npage_token\x18\x04 \x01(\tB\x03\xe0\x41\x01R\tpageToken\x12,\n\x0f\x63onversation_id\x18\x05 \x01(\tB\x03\xe0\x41\x01R\x0e\x63onversationId\x12\x1a\n\x06if_all\x18\x06 \x01(\x08\x42\x03\xe0\x41\x01R\x05ifAll\"\xb6\x01\n\x19ListConversationsResponse\x12H\n\rconversations\x18\x01 \x03(\x0b\x32\x1d.app.app.v1alpha.ConversationB\x03\xe0\x41\x03R\rconversations\x12+\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0\x41\x03R\rnextPageToken\x12\"\n\ntotal_size\x18\x03 \x01(\x05\x42\x03\xe0\x41\x03R\ttotalSize\"\xbd\x01\n\x19UpdateConversationRequest\x12!\n\x0cnamespace_id\x18\x01 \x01(\tR\x0bnamespaceId\x12\x1a\n\x06\x61pp_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x05\x61ppId\x12,\n\x0f\x63onversation_id\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x0e\x63onversationId\x12\x33\n\x13new_conversation_id\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x11newConversationId\"d\n\x1aUpdateConversationResponse\x12\x46\n\x0c\x63onversation\x18\x01 \x01(\x0b\x32\x1d.app.app.v1alpha.ConversationB\x03\xe0\x41\x03R\x0c\x63onversation\"\x8d\x01\n\x19\x44\x65leteConversationRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12\x1a\n\x06\x61pp_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x05\x61ppId\x12,\n\x0f\x63onversation_id\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x0e\x63onversationId\"\x1c\n\x1a\x44\x65leteConversationResponse\"\xff\x01\n\x14\x43reateMessageRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12\x1a\n\x06\x61pp_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x05\x61ppId\x12,\n\x0f\x63onversation_id\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x0e\x63onversationId\x12\x1d\n\x07\x63ontent\x18\x04 \x01(\tB\x03\xe0\x41\x02R\x07\x63ontent\x12\x17\n\x04role\x18\x05 \x01(\tB\x03\xe0\x41\x02R\x04role\x12=\n\x04type\x18\x06 \x01(\x0e\x32$.app.app.v1alpha.Message.MessageTypeB\x03\xe0\x41\x02R\x04type\"K\n\x15\x43reateMessageResponse\x12\x32\n\x07message\x18\x01 \x01(\x0b\x32\x18.app.app.v1alpha.MessageR\x07message\"\xd5\x01\n\x14MessageSenderProfile\x12)\n\x0emsg_sender_uid\x18\x01 \x01(\tB\x03\xe0\x41\x03R\x0cmsgSenderUid\x12\'\n\rmsg_sender_id\x18\x02 \x01(\tB\x03\xe0\x41\x03R\x0bmsgSenderId\x12+\n\x0c\x64isplay_name\x18\x03 \x01(\tB\x03\xe0\x41\x03H\x00R\x0b\x64isplayName\x88\x01\x01\x12 \n\x06\x61vatar\x18\x04 \x01(\tB\x03\xe0\x41\x03H\x01R\x06\x61vatar\x88\x01\x01\x42\x0f\n\r_display_nameB\t\n\x07_avatar\"\xc6\x02\n\x13ListMessagesRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12\x1a\n\x06\x61pp_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x05\x61ppId\x12,\n\x0f\x63onversation_id\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x0e\x63onversationId\x12\x1e\n\x08latest_k\x18\x04 \x01(\x05\x42\x03\xe0\x41\x01R\x07latestK\x12 \n\tpage_size\x18\x05 \x01(\x05\x42\x03\xe0\x41\x03R\x08pageSize\x12\"\n\npage_token\x18\x06 \x01(\tB\x03\xe0\x41\x03R\tpageToken\x12;\n\x17include_system_messages\x18\x07 \x01(\x08\x42\x03\xe0\x41\x03R\x15includeSystemMessages\x12\x1a\n\x06if_all\x18\x08 \x01(\x08\x42\x03\xe0\x41\x01R\x05ifAll\"\xf7\x01\n\x14ListMessagesResponse\x12\x39\n\x08messages\x18\x01 \x03(\x0b\x32\x18.app.app.v1alpha.MessageB\x03\xe0\x41\x03R\x08messages\x12+\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0\x41\x03R\rnextPageToken\x12\"\n\ntotal_size\x18\x03 \x01(\x05\x42\x03\xe0\x41\x03R\ttotalSize\x12S\n\x0fsender_profiles\x18\x04 \x03(\x0b\x32%.app.app.v1alpha.MessageSenderProfileB\x03\xe0\x41\x03R\x0esenderProfiles\"\xcd\x01\n\x14UpdateMessageRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12\x1a\n\x06\x61pp_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x05\x61ppId\x12,\n\x0f\x63onversation_id\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x0e\x63onversationId\x12$\n\x0bmessage_uid\x18\x04 \x01(\tB\x03\xe0\x41\x02R\nmessageUid\x12\x1d\n\x07\x63ontent\x18\x05 \x01(\tB\x03\xe0\x41\x02R\x07\x63ontent\"P\n\x15UpdateMessageResponse\x12\x37\n\x07message\x18\x01 \x01(\x0b\x32\x18.app.app.v1alpha.MessageB\x03\xe0\x41\x03R\x07message\"\xae\x01\n\x14\x44\x65leteMessageRequest\x12&\n\x0cnamespace_id\x18\x01 \x01(\tB\x03\xe0\x41\x02R\x0bnamespaceId\x12\x1a\n\x06\x61pp_id\x18\x02 \x01(\tB\x03\xe0\x41\x02R\x05\x61ppId\x12,\n\x0f\x63onversation_id\x18\x03 \x01(\tB\x03\xe0\x41\x02R\x0e\x63onversationId\x12$\n\x0bmessage_uid\x18\x04 \x01(\tB\x03\xe0\x41\x02R\nmessageUid\"\x17\n\x15\x44\x65leteMessageResponseB\xc4\x01\n\x13\x63om.app.app.v1alphaB\x11\x43onversationProtoP\x01Z<github.com/instill-ai/protogen-go/app/app/v1alpha;appv1alpha\xa2\x02\x03\x41\x41X\xaa\x02\x0f\x41pp.App.V1alpha\xca\x02\x0f\x41pp\\App\\V1alpha\xe2\x02\x1b\x41pp\\App\\V1alpha\\GPBMetadata\xea\x02\x11\x41pp::App::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.app.v1alpha.conversation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.app.app.v1alphaB\021ConversationProtoP\001Z<github.com/instill-ai/protogen-go/app/app/v1alpha;appv1alpha\242\002\003AAX\252\002\017App.App.V1alpha\312\002\017App\\App\\V1alpha\342\002\033App\\App\\V1alpha\\GPBMetadata\352\002\021App::App::V1alpha'
  _CONVERSATION.fields_by_name['uid']._options = None
  _CONVERSATION.fields_by_name['uid']._serialized_options = b'\340A\003'
  _CONVERSATION.fields_by_name['namespace_id']._options = None
  _CONVERSATION.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _CONVERSATION.fields_by_name['app_id']._options = None
  _CONVERSATION.fields_by_name['app_id']._serialized_options = b'\340A\002'
  _CONVERSATION.fields_by_name['id']._options = None
  _CONVERSATION.fields_by_name['id']._serialized_options = b'\340A\002'
  _CONVERSATION.fields_by_name['create_time']._options = None
  _CONVERSATION.fields_by_name['create_time']._serialized_options = b'\340A\003'
  _CONVERSATION.fields_by_name['update_time']._options = None
  _CONVERSATION.fields_by_name['update_time']._serialized_options = b'\340A\003'
  _MESSAGE.fields_by_name['uid']._options = None
  _MESSAGE.fields_by_name['uid']._serialized_options = b'\340A\003'
  _MESSAGE.fields_by_name['app_uid']._options = None
  _MESSAGE.fields_by_name['app_uid']._serialized_options = b'\340A\003'
  _MESSAGE.fields_by_name['conversation_uid']._options = None
  _MESSAGE.fields_by_name['conversation_uid']._serialized_options = b'\340A\003'
  _MESSAGE.fields_by_name['content']._options = None
  _MESSAGE.fields_by_name['content']._serialized_options = b'\340A\002'
  _MESSAGE.fields_by_name['role']._options = None
  _MESSAGE.fields_by_name['role']._serialized_options = b'\340A\002'
  _MESSAGE.fields_by_name['type']._options = None
  _MESSAGE.fields_by_name['type']._serialized_options = b'\340A\002'
  _MESSAGE.fields_by_name['create_time']._options = None
  _MESSAGE.fields_by_name['create_time']._serialized_options = b'\340A\003'
  _MESSAGE.fields_by_name['update_time']._options = None
  _MESSAGE.fields_by_name['update_time']._serialized_options = b'\340A\003'
  _MESSAGE.fields_by_name['msg_sender_uid']._options = None
  _MESSAGE.fields_by_name['msg_sender_uid']._serialized_options = b'\340A\003'
  _CREATECONVERSATIONREQUEST.fields_by_name['namespace_id']._options = None
  _CREATECONVERSATIONREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _CREATECONVERSATIONREQUEST.fields_by_name['app_id']._options = None
  _CREATECONVERSATIONREQUEST.fields_by_name['app_id']._serialized_options = b'\340A\002'
  _CREATECONVERSATIONREQUEST.fields_by_name['conversation_id']._options = None
  _CREATECONVERSATIONREQUEST.fields_by_name['conversation_id']._serialized_options = b'\340A\002'
  _CREATECONVERSATIONRESPONSE.fields_by_name['conversation']._options = None
  _CREATECONVERSATIONRESPONSE.fields_by_name['conversation']._serialized_options = b'\340A\003'
  _LISTCONVERSATIONSREQUEST.fields_by_name['namespace_id']._options = None
  _LISTCONVERSATIONSREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _LISTCONVERSATIONSREQUEST.fields_by_name['app_id']._options = None
  _LISTCONVERSATIONSREQUEST.fields_by_name['app_id']._serialized_options = b'\340A\002'
  _LISTCONVERSATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTCONVERSATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\001'
  _LISTCONVERSATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTCONVERSATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\001'
  _LISTCONVERSATIONSREQUEST.fields_by_name['conversation_id']._options = None
  _LISTCONVERSATIONSREQUEST.fields_by_name['conversation_id']._serialized_options = b'\340A\001'
  _LISTCONVERSATIONSREQUEST.fields_by_name['if_all']._options = None
  _LISTCONVERSATIONSREQUEST.fields_by_name['if_all']._serialized_options = b'\340A\001'
  _LISTCONVERSATIONSRESPONSE.fields_by_name['conversations']._options = None
  _LISTCONVERSATIONSRESPONSE.fields_by_name['conversations']._serialized_options = b'\340A\003'
  _LISTCONVERSATIONSRESPONSE.fields_by_name['next_page_token']._options = None
  _LISTCONVERSATIONSRESPONSE.fields_by_name['next_page_token']._serialized_options = b'\340A\003'
  _LISTCONVERSATIONSRESPONSE.fields_by_name['total_size']._options = None
  _LISTCONVERSATIONSRESPONSE.fields_by_name['total_size']._serialized_options = b'\340A\003'
  _UPDATECONVERSATIONREQUEST.fields_by_name['app_id']._options = None
  _UPDATECONVERSATIONREQUEST.fields_by_name['app_id']._serialized_options = b'\340A\002'
  _UPDATECONVERSATIONREQUEST.fields_by_name['conversation_id']._options = None
  _UPDATECONVERSATIONREQUEST.fields_by_name['conversation_id']._serialized_options = b'\340A\002'
  _UPDATECONVERSATIONREQUEST.fields_by_name['new_conversation_id']._options = None
  _UPDATECONVERSATIONREQUEST.fields_by_name['new_conversation_id']._serialized_options = b'\340A\002'
  _UPDATECONVERSATIONRESPONSE.fields_by_name['conversation']._options = None
  _UPDATECONVERSATIONRESPONSE.fields_by_name['conversation']._serialized_options = b'\340A\003'
  _DELETECONVERSATIONREQUEST.fields_by_name['namespace_id']._options = None
  _DELETECONVERSATIONREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _DELETECONVERSATIONREQUEST.fields_by_name['app_id']._options = None
  _DELETECONVERSATIONREQUEST.fields_by_name['app_id']._serialized_options = b'\340A\002'
  _DELETECONVERSATIONREQUEST.fields_by_name['conversation_id']._options = None
  _DELETECONVERSATIONREQUEST.fields_by_name['conversation_id']._serialized_options = b'\340A\002'
  _CREATEMESSAGEREQUEST.fields_by_name['namespace_id']._options = None
  _CREATEMESSAGEREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _CREATEMESSAGEREQUEST.fields_by_name['app_id']._options = None
  _CREATEMESSAGEREQUEST.fields_by_name['app_id']._serialized_options = b'\340A\002'
  _CREATEMESSAGEREQUEST.fields_by_name['conversation_id']._options = None
  _CREATEMESSAGEREQUEST.fields_by_name['conversation_id']._serialized_options = b'\340A\002'
  _CREATEMESSAGEREQUEST.fields_by_name['content']._options = None
  _CREATEMESSAGEREQUEST.fields_by_name['content']._serialized_options = b'\340A\002'
  _CREATEMESSAGEREQUEST.fields_by_name['role']._options = None
  _CREATEMESSAGEREQUEST.fields_by_name['role']._serialized_options = b'\340A\002'
  _CREATEMESSAGEREQUEST.fields_by_name['type']._options = None
  _CREATEMESSAGEREQUEST.fields_by_name['type']._serialized_options = b'\340A\002'
  _MESSAGESENDERPROFILE.fields_by_name['msg_sender_uid']._options = None
  _MESSAGESENDERPROFILE.fields_by_name['msg_sender_uid']._serialized_options = b'\340A\003'
  _MESSAGESENDERPROFILE.fields_by_name['msg_sender_id']._options = None
  _MESSAGESENDERPROFILE.fields_by_name['msg_sender_id']._serialized_options = b'\340A\003'
  _MESSAGESENDERPROFILE.fields_by_name['display_name']._options = None
  _MESSAGESENDERPROFILE.fields_by_name['display_name']._serialized_options = b'\340A\003'
  _MESSAGESENDERPROFILE.fields_by_name['avatar']._options = None
  _MESSAGESENDERPROFILE.fields_by_name['avatar']._serialized_options = b'\340A\003'
  _LISTMESSAGESREQUEST.fields_by_name['namespace_id']._options = None
  _LISTMESSAGESREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _LISTMESSAGESREQUEST.fields_by_name['app_id']._options = None
  _LISTMESSAGESREQUEST.fields_by_name['app_id']._serialized_options = b'\340A\002'
  _LISTMESSAGESREQUEST.fields_by_name['conversation_id']._options = None
  _LISTMESSAGESREQUEST.fields_by_name['conversation_id']._serialized_options = b'\340A\002'
  _LISTMESSAGESREQUEST.fields_by_name['latest_k']._options = None
  _LISTMESSAGESREQUEST.fields_by_name['latest_k']._serialized_options = b'\340A\001'
  _LISTMESSAGESREQUEST.fields_by_name['page_size']._options = None
  _LISTMESSAGESREQUEST.fields_by_name['page_size']._serialized_options = b'\340A\003'
  _LISTMESSAGESREQUEST.fields_by_name['page_token']._options = None
  _LISTMESSAGESREQUEST.fields_by_name['page_token']._serialized_options = b'\340A\003'
  _LISTMESSAGESREQUEST.fields_by_name['include_system_messages']._options = None
  _LISTMESSAGESREQUEST.fields_by_name['include_system_messages']._serialized_options = b'\340A\003'
  _LISTMESSAGESREQUEST.fields_by_name['if_all']._options = None
  _LISTMESSAGESREQUEST.fields_by_name['if_all']._serialized_options = b'\340A\001'
  _LISTMESSAGESRESPONSE.fields_by_name['messages']._options = None
  _LISTMESSAGESRESPONSE.fields_by_name['messages']._serialized_options = b'\340A\003'
  _LISTMESSAGESRESPONSE.fields_by_name['next_page_token']._options = None
  _LISTMESSAGESRESPONSE.fields_by_name['next_page_token']._serialized_options = b'\340A\003'
  _LISTMESSAGESRESPONSE.fields_by_name['total_size']._options = None
  _LISTMESSAGESRESPONSE.fields_by_name['total_size']._serialized_options = b'\340A\003'
  _LISTMESSAGESRESPONSE.fields_by_name['sender_profiles']._options = None
  _LISTMESSAGESRESPONSE.fields_by_name['sender_profiles']._serialized_options = b'\340A\003'
  _UPDATEMESSAGEREQUEST.fields_by_name['namespace_id']._options = None
  _UPDATEMESSAGEREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _UPDATEMESSAGEREQUEST.fields_by_name['app_id']._options = None
  _UPDATEMESSAGEREQUEST.fields_by_name['app_id']._serialized_options = b'\340A\002'
  _UPDATEMESSAGEREQUEST.fields_by_name['conversation_id']._options = None
  _UPDATEMESSAGEREQUEST.fields_by_name['conversation_id']._serialized_options = b'\340A\002'
  _UPDATEMESSAGEREQUEST.fields_by_name['message_uid']._options = None
  _UPDATEMESSAGEREQUEST.fields_by_name['message_uid']._serialized_options = b'\340A\002'
  _UPDATEMESSAGEREQUEST.fields_by_name['content']._options = None
  _UPDATEMESSAGEREQUEST.fields_by_name['content']._serialized_options = b'\340A\002'
  _UPDATEMESSAGERESPONSE.fields_by_name['message']._options = None
  _UPDATEMESSAGERESPONSE.fields_by_name['message']._serialized_options = b'\340A\003'
  _DELETEMESSAGEREQUEST.fields_by_name['namespace_id']._options = None
  _DELETEMESSAGEREQUEST.fields_by_name['namespace_id']._serialized_options = b'\340A\002'
  _DELETEMESSAGEREQUEST.fields_by_name['app_id']._options = None
  _DELETEMESSAGEREQUEST.fields_by_name['app_id']._serialized_options = b'\340A\002'
  _DELETEMESSAGEREQUEST.fields_by_name['conversation_id']._options = None
  _DELETEMESSAGEREQUEST.fields_by_name['conversation_id']._serialized_options = b'\340A\002'
  _DELETEMESSAGEREQUEST.fields_by_name['message_uid']._options = None
  _DELETEMESSAGEREQUEST.fields_by_name['message_uid']._serialized_options = b'\340A\002'
  _globals['_CONVERSATION']._serialized_start=122
  _globals['_CONVERSATION']._serialized_end=380
  _globals['_MESSAGE']._serialized_start=383
  _globals['_MESSAGE']._serialized_end=855
  _globals['_MESSAGE_MESSAGETYPE']._serialized_start=789
  _globals['_MESSAGE_MESSAGETYPE']._serialized_end=855
  _globals['_CREATECONVERSATIONREQUEST']._serialized_start=858
  _globals['_CREATECONVERSATIONREQUEST']._serialized_end=999
  _globals['_CREATECONVERSATIONRESPONSE']._serialized_start=1001
  _globals['_CREATECONVERSATIONRESPONSE']._serialized_end=1101
  _globals['_LISTCONVERSATIONSREQUEST']._serialized_start=1104
  _globals['_LISTCONVERSATIONSREQUEST']._serialized_end=1342
  _globals['_LISTCONVERSATIONSRESPONSE']._serialized_start=1345
  _globals['_LISTCONVERSATIONSRESPONSE']._serialized_end=1527
  _globals['_UPDATECONVERSATIONREQUEST']._serialized_start=1530
  _globals['_UPDATECONVERSATIONREQUEST']._serialized_end=1719
  _globals['_UPDATECONVERSATIONRESPONSE']._serialized_start=1721
  _globals['_UPDATECONVERSATIONRESPONSE']._serialized_end=1821
  _globals['_DELETECONVERSATIONREQUEST']._serialized_start=1824
  _globals['_DELETECONVERSATIONREQUEST']._serialized_end=1965
  _globals['_DELETECONVERSATIONRESPONSE']._serialized_start=1967
  _globals['_DELETECONVERSATIONRESPONSE']._serialized_end=1995
  _globals['_CREATEMESSAGEREQUEST']._serialized_start=1998
  _globals['_CREATEMESSAGEREQUEST']._serialized_end=2253
  _globals['_CREATEMESSAGERESPONSE']._serialized_start=2255
  _globals['_CREATEMESSAGERESPONSE']._serialized_end=2330
  _globals['_MESSAGESENDERPROFILE']._serialized_start=2333
  _globals['_MESSAGESENDERPROFILE']._serialized_end=2546
  _globals['_LISTMESSAGESREQUEST']._serialized_start=2549
  _globals['_LISTMESSAGESREQUEST']._serialized_end=2875
  _globals['_LISTMESSAGESRESPONSE']._serialized_start=2878
  _globals['_LISTMESSAGESRESPONSE']._serialized_end=3125
  _globals['_UPDATEMESSAGEREQUEST']._serialized_start=3128
  _globals['_UPDATEMESSAGEREQUEST']._serialized_end=3333
  _globals['_UPDATEMESSAGERESPONSE']._serialized_start=3335
  _globals['_UPDATEMESSAGERESPONSE']._serialized_end=3415
  _globals['_DELETEMESSAGEREQUEST']._serialized_start=3418
  _globals['_DELETEMESSAGEREQUEST']._serialized_end=3592
  _globals['_DELETEMESSAGERESPONSE']._serialized_start=3594
  _globals['_DELETEMESSAGERESPONSE']._serialized_end=3617
# @@protoc_insertion_point(module_scope)