# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vdp.mgmt.v1alpha import mgmt_pb2 as vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2


class MgmtAdminServiceStub(object):
    """Mgmt service responds to incoming requests.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListUser = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtAdminService/ListUser',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ListUserRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ListUserResponse.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtAdminService/CreateUser',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.CreateUserResponse.FromString,
                )
        self.GetUser = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtAdminService/GetUser',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetUserRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetUserResponse.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtAdminService/UpdateUser',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateUserResponse.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtAdminService/DeleteUser',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.DeleteUserResponse.FromString,
                )
        self.LookUpUser = channel.unary_unary(
                '/vdp.mgmt.v1alpha.MgmtAdminService/LookUpUser',
                request_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.LookUpUserRequest.SerializeToString,
                response_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.LookUpUserResponse.FromString,
                )


class MgmtAdminServiceServicer(object):
    """Mgmt service responds to incoming requests.
    """

    def ListUser(self, request, context):
        """========== Admin API: create, get, update and delete user accounts

        ListUser method receives a ListUserRequest message and returns a
        ListUserResponse message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """CreateUser receives a CreateUserRequest message and returns a
        aGetUserResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """GetUser method receives a GetUserRequest message and returns
        a GetUserResponse message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """UpdateUser method receives a UpdateUserRequest message and returns
        a UpdateUserResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """DeleteUser method receives a DeleteUserRequest message and returns a
        DeleteUserResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookUpUser(self, request, context):
        """LookUpUser method receives a LookUpUserRequest message and returns a
        LookUpUserResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MgmtAdminServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListUser': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUser,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ListUserRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ListUserResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.CreateUserRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.CreateUserResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetUserRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetUserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateUserRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateUserResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.DeleteUserRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.DeleteUserResponse.SerializeToString,
            ),
            'LookUpUser': grpc.unary_unary_rpc_method_handler(
                    servicer.LookUpUser,
                    request_deserializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.LookUpUserRequest.FromString,
                    response_serializer=vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.LookUpUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vdp.mgmt.v1alpha.MgmtAdminService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MgmtAdminService(object):
    """Mgmt service responds to incoming requests.
    """

    @staticmethod
    def ListUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtAdminService/ListUser',
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ListUserRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.ListUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtAdminService/CreateUser',
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.CreateUserRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtAdminService/GetUser',
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetUserRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.GetUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtAdminService/UpdateUser',
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateUserRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.UpdateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtAdminService/DeleteUser',
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.DeleteUserRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.DeleteUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookUpUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.mgmt.v1alpha.MgmtAdminService/LookUpUser',
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.LookUpUserRequest.SerializeToString,
            vdp_dot_mgmt_dot_v1alpha_dot_mgmt__pb2.LookUpUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)