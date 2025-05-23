# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from model.ray import serve_pb2 as model_dot_ray_dot_serve__pb2


class RayServeAPIServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListApplications = channel.unary_unary(
                '/ray.serve.RayServeAPIService/ListApplications',
                request_serializer=model_dot_ray_dot_serve__pb2.ListApplicationsRequest.SerializeToString,
                response_deserializer=model_dot_ray_dot_serve__pb2.ListApplicationsResponse.FromString,
                )
        self.Healthz = channel.unary_unary(
                '/ray.serve.RayServeAPIService/Healthz',
                request_serializer=model_dot_ray_dot_serve__pb2.HealthzRequest.SerializeToString,
                response_deserializer=model_dot_ray_dot_serve__pb2.HealthzResponse.FromString,
                )


class RayServeAPIServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListApplications(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Healthz(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RayServeAPIServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListApplications': grpc.unary_unary_rpc_method_handler(
                    servicer.ListApplications,
                    request_deserializer=model_dot_ray_dot_serve__pb2.ListApplicationsRequest.FromString,
                    response_serializer=model_dot_ray_dot_serve__pb2.ListApplicationsResponse.SerializeToString,
            ),
            'Healthz': grpc.unary_unary_rpc_method_handler(
                    servicer.Healthz,
                    request_deserializer=model_dot_ray_dot_serve__pb2.HealthzRequest.FromString,
                    response_serializer=model_dot_ray_dot_serve__pb2.HealthzResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ray.serve.RayServeAPIService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RayServeAPIService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListApplications(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ray.serve.RayServeAPIService/ListApplications',
            model_dot_ray_dot_serve__pb2.ListApplicationsRequest.SerializeToString,
            model_dot_ray_dot_serve__pb2.ListApplicationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Healthz(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ray.serve.RayServeAPIService/Healthz',
            model_dot_ray_dot_serve__pb2.HealthzRequest.SerializeToString,
            model_dot_ray_dot_serve__pb2.HealthzResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class UserDefinedServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.__call__ = channel.unary_unary(
                '/ray.serve.UserDefinedService/__call__',
                request_serializer=model_dot_ray_dot_serve__pb2.UserDefinedMessage.SerializeToString,
                response_deserializer=model_dot_ray_dot_serve__pb2.UserDefinedResponse.FromString,
                )
        self.Method1 = channel.unary_unary(
                '/ray.serve.UserDefinedService/Method1',
                request_serializer=model_dot_ray_dot_serve__pb2.UserDefinedMessage.SerializeToString,
                response_deserializer=model_dot_ray_dot_serve__pb2.UserDefinedResponse.FromString,
                )
        self.Method2 = channel.unary_unary(
                '/ray.serve.UserDefinedService/Method2',
                request_serializer=model_dot_ray_dot_serve__pb2.UserDefinedMessage2.SerializeToString,
                response_deserializer=model_dot_ray_dot_serve__pb2.UserDefinedResponse2.FromString,
                )
        self.Streaming = channel.unary_stream(
                '/ray.serve.UserDefinedService/Streaming',
                request_serializer=model_dot_ray_dot_serve__pb2.UserDefinedMessage.SerializeToString,
                response_deserializer=model_dot_ray_dot_serve__pb2.UserDefinedResponse.FromString,
                )


class UserDefinedServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def __call__(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Method1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Method2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Streaming(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserDefinedServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            '__call__': grpc.unary_unary_rpc_method_handler(
                    servicer.__call__,
                    request_deserializer=model_dot_ray_dot_serve__pb2.UserDefinedMessage.FromString,
                    response_serializer=model_dot_ray_dot_serve__pb2.UserDefinedResponse.SerializeToString,
            ),
            'Method1': grpc.unary_unary_rpc_method_handler(
                    servicer.Method1,
                    request_deserializer=model_dot_ray_dot_serve__pb2.UserDefinedMessage.FromString,
                    response_serializer=model_dot_ray_dot_serve__pb2.UserDefinedResponse.SerializeToString,
            ),
            'Method2': grpc.unary_unary_rpc_method_handler(
                    servicer.Method2,
                    request_deserializer=model_dot_ray_dot_serve__pb2.UserDefinedMessage2.FromString,
                    response_serializer=model_dot_ray_dot_serve__pb2.UserDefinedResponse2.SerializeToString,
            ),
            'Streaming': grpc.unary_stream_rpc_method_handler(
                    servicer.Streaming,
                    request_deserializer=model_dot_ray_dot_serve__pb2.UserDefinedMessage.FromString,
                    response_serializer=model_dot_ray_dot_serve__pb2.UserDefinedResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ray.serve.UserDefinedService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserDefinedService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def __call__(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ray.serve.UserDefinedService/__call__',
            model_dot_ray_dot_serve__pb2.UserDefinedMessage.SerializeToString,
            model_dot_ray_dot_serve__pb2.UserDefinedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Method1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ray.serve.UserDefinedService/Method1',
            model_dot_ray_dot_serve__pb2.UserDefinedMessage.SerializeToString,
            model_dot_ray_dot_serve__pb2.UserDefinedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Method2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ray.serve.UserDefinedService/Method2',
            model_dot_ray_dot_serve__pb2.UserDefinedMessage2.SerializeToString,
            model_dot_ray_dot_serve__pb2.UserDefinedResponse2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Streaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ray.serve.UserDefinedService/Streaming',
            model_dot_ray_dot_serve__pb2.UserDefinedMessage.SerializeToString,
            model_dot_ray_dot_serve__pb2.UserDefinedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class FruitServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FruitStand = channel.unary_unary(
                '/ray.serve.FruitService/FruitStand',
                request_serializer=model_dot_ray_dot_serve__pb2.FruitAmounts.SerializeToString,
                response_deserializer=model_dot_ray_dot_serve__pb2.FruitCosts.FromString,
                )


class FruitServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FruitStand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FruitServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FruitStand': grpc.unary_unary_rpc_method_handler(
                    servicer.FruitStand,
                    request_deserializer=model_dot_ray_dot_serve__pb2.FruitAmounts.FromString,
                    response_serializer=model_dot_ray_dot_serve__pb2.FruitCosts.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ray.serve.FruitService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FruitService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FruitStand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ray.serve.FruitService/FruitStand',
            model_dot_ray_dot_serve__pb2.FruitAmounts.SerializeToString,
            model_dot_ray_dot_serve__pb2.FruitCosts.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RayServeBenchmarkServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.grpc_call = channel.unary_unary(
                '/ray.serve.RayServeBenchmarkService/grpc_call',
                request_serializer=model_dot_ray_dot_serve__pb2.ArrayData.SerializeToString,
                response_deserializer=model_dot_ray_dot_serve__pb2.ModelOutput.FromString,
                )
        self.call_with_string = channel.unary_unary(
                '/ray.serve.RayServeBenchmarkService/call_with_string',
                request_serializer=model_dot_ray_dot_serve__pb2.StringData.SerializeToString,
                response_deserializer=model_dot_ray_dot_serve__pb2.ModelOutput.FromString,
                )


class RayServeBenchmarkServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def grpc_call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def call_with_string(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RayServeBenchmarkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'grpc_call': grpc.unary_unary_rpc_method_handler(
                    servicer.grpc_call,
                    request_deserializer=model_dot_ray_dot_serve__pb2.ArrayData.FromString,
                    response_serializer=model_dot_ray_dot_serve__pb2.ModelOutput.SerializeToString,
            ),
            'call_with_string': grpc.unary_unary_rpc_method_handler(
                    servicer.call_with_string,
                    request_deserializer=model_dot_ray_dot_serve__pb2.StringData.FromString,
                    response_serializer=model_dot_ray_dot_serve__pb2.ModelOutput.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ray.serve.RayServeBenchmarkService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RayServeBenchmarkService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def grpc_call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ray.serve.RayServeBenchmarkService/grpc_call',
            model_dot_ray_dot_serve__pb2.ArrayData.SerializeToString,
            model_dot_ray_dot_serve__pb2.ModelOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def call_with_string(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ray.serve.RayServeBenchmarkService/call_with_string',
            model_dot_ray_dot_serve__pb2.StringData.SerializeToString,
            model_dot_ray_dot_serve__pb2.ModelOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
