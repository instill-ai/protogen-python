"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import common.healthcheck.v1beta.healthcheck_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class LivenessRequest(google.protobuf.message.Message):
    """LivenessRequest represents a request to check a service liveness status"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEALTH_CHECK_REQUEST_FIELD_NUMBER: builtins.int
    @property
    def health_check_request(self) -> common.healthcheck.v1beta.healthcheck_pb2.HealthCheckRequest:
        """HealthCheckRequest message"""
    def __init__(
        self,
        *,
        health_check_request: common.healthcheck.v1beta.healthcheck_pb2.HealthCheckRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_health_check_request", b"_health_check_request", "health_check_request", b"health_check_request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_health_check_request", b"_health_check_request", "health_check_request", b"health_check_request"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_health_check_request", b"_health_check_request"]) -> typing_extensions.Literal["health_check_request"] | None: ...

global___LivenessRequest = LivenessRequest

@typing_extensions.final
class LivenessResponse(google.protobuf.message.Message):
    """LivenessResponse represents a response for a service liveness status"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEALTH_CHECK_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def health_check_response(self) -> common.healthcheck.v1beta.healthcheck_pb2.HealthCheckResponse:
        """HealthCheckResponse message"""
    def __init__(
        self,
        *,
        health_check_response: common.healthcheck.v1beta.healthcheck_pb2.HealthCheckResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["health_check_response", b"health_check_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["health_check_response", b"health_check_response"]) -> None: ...

global___LivenessResponse = LivenessResponse

@typing_extensions.final
class ReadinessRequest(google.protobuf.message.Message):
    """ReadinessRequest represents a request to check a service readiness status"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEALTH_CHECK_REQUEST_FIELD_NUMBER: builtins.int
    @property
    def health_check_request(self) -> common.healthcheck.v1beta.healthcheck_pb2.HealthCheckRequest:
        """HealthCheckRequest message"""
    def __init__(
        self,
        *,
        health_check_request: common.healthcheck.v1beta.healthcheck_pb2.HealthCheckRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_health_check_request", b"_health_check_request", "health_check_request", b"health_check_request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_health_check_request", b"_health_check_request", "health_check_request", b"health_check_request"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_health_check_request", b"_health_check_request"]) -> typing_extensions.Literal["health_check_request"] | None: ...

global___ReadinessRequest = ReadinessRequest

@typing_extensions.final
class ReadinessResponse(google.protobuf.message.Message):
    """ReadinessResponse represents a response for a service readiness status"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEALTH_CHECK_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def health_check_response(self) -> common.healthcheck.v1beta.healthcheck_pb2.HealthCheckResponse:
        """HealthCheckResponse message"""
    def __init__(
        self,
        *,
        health_check_response: common.healthcheck.v1beta.healthcheck_pb2.HealthCheckResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["health_check_response", b"health_check_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["health_check_response", b"health_check_response"]) -> None: ...

global___ReadinessResponse = ReadinessResponse