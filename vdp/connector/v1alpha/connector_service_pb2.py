# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vdp/connector/v1alpha/connector_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from vdp.connector.v1alpha import healthcheck_pb2 as vdp_dot_connector_dot_v1alpha_dot_healthcheck__pb2
from vdp.connector.v1alpha import connector_definition_pb2 as vdp_dot_connector_dot_v1alpha_dot_connector__definition__pb2
from vdp.connector.v1alpha import connector_pb2 as vdp_dot_connector_dot_v1alpha_dot_connector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-vdp/connector/v1alpha/connector_service.proto\x12\x15vdp.connector.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\'vdp/connector/v1alpha/healthcheck.proto\x1a\x30vdp/connector/v1alpha/connector_definition.proto\x1a%vdp/connector/v1alpha/connector.proto2\xca*\n\x10\x43onnectorService\x12\x95\x01\n\x08Liveness\x12&.vdp.connector.v1alpha.LivenessRequest\x1a\'.vdp.connector.v1alpha.LivenessResponse\"8\x82\xd3\xe4\x93\x02\x32Z\x1b\x12\x19/v1alpha/health/connector\x12\x13/v1alpha/__liveness\x12|\n\tReadiness\x12\'.vdp.connector.v1alpha.ReadinessRequest\x1a(.vdp.connector.v1alpha.ReadinessResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1alpha/__readiness\x12\xc9\x01\n\x1dListSourceConnectorDefinition\x12;.vdp.connector.v1alpha.ListSourceConnectorDefinitionRequest\x1a<.vdp.connector.v1alpha.ListSourceConnectorDefinitionResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v1alpha/source-connector-definitions\x12\xd6\x01\n\x1cGetSourceConnectorDefinition\x12:.vdp.connector.v1alpha.GetSourceConnectorDefinitionRequest\x1a;.vdp.connector.v1alpha.GetSourceConnectorDefinitionResponse\"=\xda\x41\x04name\x82\xd3\xe4\x93\x02\x30\x12./v1alpha/{name=source-connector-definitions/*}\x12\xdd\x01\n\"ListDestinationConnectorDefinition\x12@.vdp.connector.v1alpha.ListDestinationConnectorDefinitionRequest\x1a\x41.vdp.connector.v1alpha.ListDestinationConnectorDefinitionResponse\"2\x82\xd3\xe4\x93\x02,\x12*/v1alpha/destination-connector-definitions\x12\xea\x01\n!GetDestinationConnectorDefinition\x12?.vdp.connector.v1alpha.GetDestinationConnectorDefinitionRequest\x1a@.vdp.connector.v1alpha.GetDestinationConnectorDefinitionResponse\"B\xda\x41\x04name\x82\xd3\xe4\x93\x02\x35\x12\x33/v1alpha/{name=destination-connector-definitions/*}\x12\xcb\x01\n\x15\x43reateSourceConnector\x12\x33.vdp.connector.v1alpha.CreateSourceConnectorRequest\x1a\x34.vdp.connector.v1alpha.CreateSourceConnectorResponse\"G\xda\x41\x10source_connector\x82\xd3\xe4\x93\x02.:\x10source_connector\"\x1a/v1alpha/source-connectors\x12\xa0\x01\n\x13ListSourceConnector\x12\x31.vdp.connector.v1alpha.ListSourceConnectorRequest\x1a\x32.vdp.connector.v1alpha.ListSourceConnectorResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1alpha/source-connectors\x12\xad\x01\n\x12GetSourceConnector\x12\x30.vdp.connector.v1alpha.GetSourceConnectorRequest\x1a\x31.vdp.connector.v1alpha.GetSourceConnectorResponse\"2\xda\x41\x04name\x82\xd3\xe4\x93\x02%\x12#/v1alpha/{name=source-connectors/*}\x12\xf1\x01\n\x15UpdateSourceConnector\x12\x33.vdp.connector.v1alpha.UpdateSourceConnectorRequest\x1a\x34.vdp.connector.v1alpha.UpdateSourceConnectorResponse\"m\xda\x41\x1csource_connector,update_mask\x82\xd3\xe4\x93\x02H:\x10source_connector24/v1alpha/{source_connector.name=source-connectors/*}\x12\xb6\x01\n\x15\x44\x65leteSourceConnector\x12\x33.vdp.connector.v1alpha.DeleteSourceConnectorRequest\x1a\x34.vdp.connector.v1alpha.DeleteSourceConnectorResponse\"2\xda\x41\x04name\x82\xd3\xe4\x93\x02%*#/v1alpha/{name=source-connectors/*}\x12\xc7\x01\n\x15LookUpSourceConnector\x12\x33.vdp.connector.v1alpha.LookUpSourceConnectorRequest\x1a\x34.vdp.connector.v1alpha.LookUpSourceConnectorResponse\"C\xda\x41\tpermalink\x82\xd3\xe4\x93\x02\x31\x12//v1alpha/{permalink=source-connectors/*}:lookUp\x12\xc4\x01\n\x16\x43onnectSourceConnector\x12\x34.vdp.connector.v1alpha.ConnectSourceConnectorRequest\x1a\x35.vdp.connector.v1alpha.ConnectSourceConnectorResponse\"=\xda\x41\x04name\x82\xd3\xe4\x93\x02\x30:\x01*\"+/v1alpha/{name=source-connectors/*}:connect\x12\xd0\x01\n\x19\x44isconnectSourceConnector\x12\x37.vdp.connector.v1alpha.DisconnectSourceConnectorRequest\x1a\x38.vdp.connector.v1alpha.DisconnectSourceConnectorResponse\"@\xda\x41\x04name\x82\xd3\xe4\x93\x02\x33:\x01*\"./v1alpha/{name=source-connectors/*}:disconnect\x12\xd8\x01\n\x15RenameSourceConnector\x12\x33.vdp.connector.v1alpha.RenameSourceConnectorRequest\x1a\x34.vdp.connector.v1alpha.RenameSourceConnectorResponse\"T\xda\x41\x1cname,new_source_connector_id\x82\xd3\xe4\x93\x02/:\x01*\"*/v1alpha/{name=source-connectors/*}:rename\x12\xd0\x01\n\x13ReadSourceConnector\x12\x31.vdp.connector.v1alpha.ReadSourceConnectorRequest\x1a\x32.vdp.connector.v1alpha.ReadSourceConnectorResponse\"R\xda\x41\x1cname,new_source_connector_id\x82\xd3\xe4\x93\x02-:\x01*\"(/v1alpha/{name=source-connectors/*}:read\x12\xe9\x01\n\x1a\x43reateDestinationConnector\x12\x38.vdp.connector.v1alpha.CreateDestinationConnectorRequest\x1a\x39.vdp.connector.v1alpha.CreateDestinationConnectorResponse\"V\xda\x41\x15\x64\x65stination_connector\x82\xd3\xe4\x93\x02\x38:\x15\x64\x65stination_connector\"\x1f/v1alpha/destination-connectors\x12\xb4\x01\n\x18ListDestinationConnector\x12\x36.vdp.connector.v1alpha.ListDestinationConnectorRequest\x1a\x37.vdp.connector.v1alpha.ListDestinationConnectorResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1alpha/destination-connectors\x12\xc1\x01\n\x17GetDestinationConnector\x12\x35.vdp.connector.v1alpha.GetDestinationConnectorRequest\x1a\x36.vdp.connector.v1alpha.GetDestinationConnectorResponse\"7\xda\x41\x04name\x82\xd3\xe4\x93\x02*\x12(/v1alpha/{name=destination-connectors/*}\x12\x95\x02\n\x1aUpdateDestinationConnector\x12\x38.vdp.connector.v1alpha.UpdateDestinationConnectorRequest\x1a\x39.vdp.connector.v1alpha.UpdateDestinationConnectorResponse\"\x81\x01\xda\x41!destination_connector,update_mask\x82\xd3\xe4\x93\x02W:\x15\x64\x65stination_connector2>/v1alpha/{destination_connector.name=destination-connectors/*}\x12\xca\x01\n\x1a\x44\x65leteDestinationConnector\x12\x38.vdp.connector.v1alpha.DeleteDestinationConnectorRequest\x1a\x39.vdp.connector.v1alpha.DeleteDestinationConnectorResponse\"7\xda\x41\x04name\x82\xd3\xe4\x93\x02**(/v1alpha/{name=destination-connectors/*}\x12\xdb\x01\n\x1aLookUpDestinationConnector\x12\x38.vdp.connector.v1alpha.LookUpDestinationConnectorRequest\x1a\x39.vdp.connector.v1alpha.LookUpDestinationConnectorResponse\"H\xda\x41\tpermalink\x82\xd3\xe4\x93\x02\x36\x12\x34/v1alpha/{permalink=destination-connectors/*}:lookUp\x12\xd8\x01\n\x1b\x43onnectDestinationConnector\x12\x39.vdp.connector.v1alpha.ConnectDestinationConnectorRequest\x1a:.vdp.connector.v1alpha.ConnectDestinationConnectorResponse\"B\xda\x41\x04name\x82\xd3\xe4\x93\x02\x35:\x01*\"0/v1alpha/{name=destination-connectors/*}:connect\x12\xe4\x01\n\x1e\x44isconnectDestinationConnector\x12<.vdp.connector.v1alpha.DisconnectDestinationConnectorRequest\x1a=.vdp.connector.v1alpha.DisconnectDestinationConnectorResponse\"E\xda\x41\x04name\x82\xd3\xe4\x93\x02\x38:\x01*\"3/v1alpha/{name=destination-connectors/*}:disconnect\x12\xf1\x01\n\x1aRenameDestinationConnector\x12\x38.vdp.connector.v1alpha.RenameDestinationConnectorRequest\x1a\x39.vdp.connector.v1alpha.RenameDestinationConnectorResponse\"^\xda\x41!name,new_destination_connector_id\x82\xd3\xe4\x93\x02\x34:\x01*\"//v1alpha/{name=destination-connectors/*}:rename\x12\xed\x01\n\x19WriteDestinationConnector\x12\x37.vdp.connector.v1alpha.WriteDestinationConnectorRequest\x1a\x38.vdp.connector.v1alpha.WriteDestinationConnectorResponse\"]\xda\x41!name,new_destination_connector_id\x82\xd3\xe4\x93\x02\x33:\x01*\"./v1alpha/{name=destination-connectors/*}:writeB\xf2\x01\n\x19\x63om.vdp.connector.v1alphaB\x15\x43onnectorServiceProtoP\x01ZHgithub.com/instill-ai/protogen-go/vdp/connector/v1alpha;connectorv1alpha\xa2\x02\x03VCX\xaa\x02\x15Vdp.Connector.V1alpha\xca\x02\x15Vdp\\Connector\\V1alpha\xe2\x02!Vdp\\Connector\\V1alpha\\GPBMetadata\xea\x02\x17Vdp::Connector::V1alphab\x06proto3')



_CONNECTORSERVICE = DESCRIPTOR.services_by_name['ConnectorService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.vdp.connector.v1alphaB\025ConnectorServiceProtoP\001ZHgithub.com/instill-ai/protogen-go/vdp/connector/v1alpha;connectorv1alpha\242\002\003VCX\252\002\025Vdp.Connector.V1alpha\312\002\025Vdp\\Connector\\V1alpha\342\002!Vdp\\Connector\\V1alpha\\GPBMetadata\352\002\027Vdp::Connector::V1alpha'
  _CONNECTORSERVICE.methods_by_name['Liveness']._options = None
  _CONNECTORSERVICE.methods_by_name['Liveness']._serialized_options = b'\202\323\344\223\0022Z\033\022\031/v1alpha/health/connector\022\023/v1alpha/__liveness'
  _CONNECTORSERVICE.methods_by_name['Readiness']._options = None
  _CONNECTORSERVICE.methods_by_name['Readiness']._serialized_options = b'\202\323\344\223\002\026\022\024/v1alpha/__readiness'
  _CONNECTORSERVICE.methods_by_name['ListSourceConnectorDefinition']._options = None
  _CONNECTORSERVICE.methods_by_name['ListSourceConnectorDefinition']._serialized_options = b'\202\323\344\223\002\'\022%/v1alpha/source-connector-definitions'
  _CONNECTORSERVICE.methods_by_name['GetSourceConnectorDefinition']._options = None
  _CONNECTORSERVICE.methods_by_name['GetSourceConnectorDefinition']._serialized_options = b'\332A\004name\202\323\344\223\0020\022./v1alpha/{name=source-connector-definitions/*}'
  _CONNECTORSERVICE.methods_by_name['ListDestinationConnectorDefinition']._options = None
  _CONNECTORSERVICE.methods_by_name['ListDestinationConnectorDefinition']._serialized_options = b'\202\323\344\223\002,\022*/v1alpha/destination-connector-definitions'
  _CONNECTORSERVICE.methods_by_name['GetDestinationConnectorDefinition']._options = None
  _CONNECTORSERVICE.methods_by_name['GetDestinationConnectorDefinition']._serialized_options = b'\332A\004name\202\323\344\223\0025\0223/v1alpha/{name=destination-connector-definitions/*}'
  _CONNECTORSERVICE.methods_by_name['CreateSourceConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['CreateSourceConnector']._serialized_options = b'\332A\020source_connector\202\323\344\223\002.:\020source_connector\"\032/v1alpha/source-connectors'
  _CONNECTORSERVICE.methods_by_name['ListSourceConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['ListSourceConnector']._serialized_options = b'\202\323\344\223\002\034\022\032/v1alpha/source-connectors'
  _CONNECTORSERVICE.methods_by_name['GetSourceConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['GetSourceConnector']._serialized_options = b'\332A\004name\202\323\344\223\002%\022#/v1alpha/{name=source-connectors/*}'
  _CONNECTORSERVICE.methods_by_name['UpdateSourceConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['UpdateSourceConnector']._serialized_options = b'\332A\034source_connector,update_mask\202\323\344\223\002H:\020source_connector24/v1alpha/{source_connector.name=source-connectors/*}'
  _CONNECTORSERVICE.methods_by_name['DeleteSourceConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['DeleteSourceConnector']._serialized_options = b'\332A\004name\202\323\344\223\002%*#/v1alpha/{name=source-connectors/*}'
  _CONNECTORSERVICE.methods_by_name['LookUpSourceConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['LookUpSourceConnector']._serialized_options = b'\332A\tpermalink\202\323\344\223\0021\022//v1alpha/{permalink=source-connectors/*}:lookUp'
  _CONNECTORSERVICE.methods_by_name['ConnectSourceConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['ConnectSourceConnector']._serialized_options = b'\332A\004name\202\323\344\223\0020:\001*\"+/v1alpha/{name=source-connectors/*}:connect'
  _CONNECTORSERVICE.methods_by_name['DisconnectSourceConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['DisconnectSourceConnector']._serialized_options = b'\332A\004name\202\323\344\223\0023:\001*\"./v1alpha/{name=source-connectors/*}:disconnect'
  _CONNECTORSERVICE.methods_by_name['RenameSourceConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['RenameSourceConnector']._serialized_options = b'\332A\034name,new_source_connector_id\202\323\344\223\002/:\001*\"*/v1alpha/{name=source-connectors/*}:rename'
  _CONNECTORSERVICE.methods_by_name['ReadSourceConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['ReadSourceConnector']._serialized_options = b'\332A\034name,new_source_connector_id\202\323\344\223\002-:\001*\"(/v1alpha/{name=source-connectors/*}:read'
  _CONNECTORSERVICE.methods_by_name['CreateDestinationConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['CreateDestinationConnector']._serialized_options = b'\332A\025destination_connector\202\323\344\223\0028:\025destination_connector\"\037/v1alpha/destination-connectors'
  _CONNECTORSERVICE.methods_by_name['ListDestinationConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['ListDestinationConnector']._serialized_options = b'\202\323\344\223\002!\022\037/v1alpha/destination-connectors'
  _CONNECTORSERVICE.methods_by_name['GetDestinationConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['GetDestinationConnector']._serialized_options = b'\332A\004name\202\323\344\223\002*\022(/v1alpha/{name=destination-connectors/*}'
  _CONNECTORSERVICE.methods_by_name['UpdateDestinationConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['UpdateDestinationConnector']._serialized_options = b'\332A!destination_connector,update_mask\202\323\344\223\002W:\025destination_connector2>/v1alpha/{destination_connector.name=destination-connectors/*}'
  _CONNECTORSERVICE.methods_by_name['DeleteDestinationConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['DeleteDestinationConnector']._serialized_options = b'\332A\004name\202\323\344\223\002**(/v1alpha/{name=destination-connectors/*}'
  _CONNECTORSERVICE.methods_by_name['LookUpDestinationConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['LookUpDestinationConnector']._serialized_options = b'\332A\tpermalink\202\323\344\223\0026\0224/v1alpha/{permalink=destination-connectors/*}:lookUp'
  _CONNECTORSERVICE.methods_by_name['ConnectDestinationConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['ConnectDestinationConnector']._serialized_options = b'\332A\004name\202\323\344\223\0025:\001*\"0/v1alpha/{name=destination-connectors/*}:connect'
  _CONNECTORSERVICE.methods_by_name['DisconnectDestinationConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['DisconnectDestinationConnector']._serialized_options = b'\332A\004name\202\323\344\223\0028:\001*\"3/v1alpha/{name=destination-connectors/*}:disconnect'
  _CONNECTORSERVICE.methods_by_name['RenameDestinationConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['RenameDestinationConnector']._serialized_options = b'\332A!name,new_destination_connector_id\202\323\344\223\0024:\001*\"//v1alpha/{name=destination-connectors/*}:rename'
  _CONNECTORSERVICE.methods_by_name['WriteDestinationConnector']._options = None
  _CONNECTORSERVICE.methods_by_name['WriteDestinationConnector']._serialized_options = b'\332A!name,new_destination_connector_id\202\323\344\223\0023:\001*\"./v1alpha/{name=destination-connectors/*}:write'
  _CONNECTORSERVICE._serialized_start=258
  _CONNECTORSERVICE._serialized_end=5708
# @@protoc_insertion_point(module_scope)