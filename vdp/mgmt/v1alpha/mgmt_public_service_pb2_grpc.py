# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vdp.mgmt.v1alpha import healthcheck_pb2 as vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2
from vdp.mgmt.v1alpha import mgmt_pb2 as vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2


class MgmtPublicServiceStub(object):
    """Mgmt service responds to incoming requests.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Liveness = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtPublicService/Liveness',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.LivenessRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.LivenessResponse.FromString,
                )
        self.Readiness = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtPublicService/Readiness',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.ReadinessRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.ReadinessResponse.FromString,
                )
        self.GetAuthenticatedUser = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtPublicService/GetAuthenticatedUser',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetAuthenticatedUserRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetAuthenticatedUserResponse.FromString,
                )
        self.UpdateAuthenticatedUser = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtPublicService/UpdateAuthenticatedUser',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateAuthenticatedUserRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateAuthenticatedUserResponse.FromString,
                )
        self.ExistUsername = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtPublicService/ExistUsername',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ExistUsernameRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ExistUsernameResponse.FromString,
                )


class MgmtPublicServiceServicer(object):
    """Mgmt service responds to incoming requests.
    """

    def Liveness(self, request, context):
        """Liveness method receives a LivenessRequest message and returns a
        LivenessResponse message.
        See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Readiness(self, request, context):
        """Readiness method receives a ReadinessRequest message and returns a
        ReadinessResponse message.
        See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAuthenticatedUser(self, request, context):
        """========== Public API: endpoints exposed to public internet traffic

        GetAuthenticatedUser method receives a GetAuthenticatedUserRequest message and returns
        a GetAuthenticatedUserResponse message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAuthenticatedUser(self, request, context):
        """UpdateAuthenticatedUser method receives a UpdateAuthenticatedUserRequest message and returns 
        a UpdateAuthenticatedUserResponse message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExistUsername(self, request, context):
        """ExistUsername method receives a ExistUsernameRequest message and returns a
        ExistUsernameResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MgmtPublicServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Liveness': grpc.unary_unary_rpc_method_handler(
                    servicer.Liveness,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.LivenessRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.LivenessResponse.SerializeToString,
            ),
            'Readiness': grpc.unary_unary_rpc_method_handler(
                    servicer.Readiness,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.ReadinessRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.ReadinessResponse.SerializeToString,
            ),
            'GetAuthenticatedUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAuthenticatedUser,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetAuthenticatedUserRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetAuthenticatedUserResponse.SerializeToString,
            ),
            'UpdateAuthenticatedUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAuthenticatedUser,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateAuthenticatedUserRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateAuthenticatedUserResponse.SerializeToString,
            ),
            'ExistUsername': grpc.unary_unary_rpc_method_handler(
                    servicer.ExistUsername,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ExistUsernameRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ExistUsernameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vdp.mgmt.v1alpha.MgmtPublicService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MgmtPublicService(object):
    """Mgmt service responds to incoming requests.
    """

    @staticmethod
    def Liveness(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtPublicService/Liveness',
            vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.LivenessRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.LivenessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Readiness(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtPublicService/Readiness',
            vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.ReadinessRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_healthcheck__pb2.ReadinessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAuthenticatedUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtPublicService/GetAuthenticatedUser',
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetAuthenticatedUserRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetAuthenticatedUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAuthenticatedUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtPublicService/UpdateAuthenticatedUser',
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateAuthenticatedUserRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateAuthenticatedUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExistUsername(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtPublicService/ExistUsername',
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ExistUsernameRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ExistUsernameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)