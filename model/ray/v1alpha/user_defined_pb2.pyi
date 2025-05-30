"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CallRequest(google.protobuf.message.Message):
    """CallRequest represents a request for model inference"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_INPUTS_FIELD_NUMBER: builtins.int
    @property
    def task_inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Struct]:
        """Inference input parameters."""
    def __init__(
        self,
        *,
        task_inputs: collections.abc.Iterable[google.protobuf.struct_pb2.Struct] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_inputs", b"task_inputs"]) -> None: ...

global___CallRequest = CallRequest

@typing_extensions.final
class CallResponse(google.protobuf.message.Message):
    """CallResponse represents a response for model inference"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TASK_OUTPUTS_FIELD_NUMBER: builtins.int
    @property
    def task_outputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Struct]:
        """Model inference outputs."""
    def __init__(
        self,
        *,
        task_outputs: collections.abc.Iterable[google.protobuf.struct_pb2.Struct] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["task_outputs", b"task_outputs"]) -> None: ...

global___CallResponse = CallResponse
