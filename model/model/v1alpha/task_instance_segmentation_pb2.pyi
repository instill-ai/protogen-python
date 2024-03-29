"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import model.model.v1alpha.common_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class InstanceSegmentationObject(google.protobuf.message.Message):
    """InstanceSegmentationObject is an object in an image, localized and
    delineated.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RLE_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    BOUNDING_BOX_FIELD_NUMBER: builtins.int
    rle: builtins.str
    """RLE segmentation mask."""
    category: builtins.str
    """Category."""
    score: builtins.float
    """Score."""
    @property
    def bounding_box(self) -> model.model.v1alpha.common_pb2.BoundingBox:
        """Bounding box."""
    def __init__(
        self,
        *,
        rle: builtins.str = ...,
        category: builtins.str = ...,
        score: builtins.float = ...,
        bounding_box: model.model.v1alpha.common_pb2.BoundingBox | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["bounding_box", b"bounding_box"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["bounding_box", b"bounding_box", "category", b"category", "rle", b"rle", "score", b"score"]) -> None: ...

global___InstanceSegmentationObject = InstanceSegmentationObject

@typing_extensions.final
class InstanceSegmentationInput(google.protobuf.message.Message):
    """InstanceSegmentationInput represents the input of an instance segmentation
    task.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMAGE_URL_FIELD_NUMBER: builtins.int
    IMAGE_BASE64_FIELD_NUMBER: builtins.int
    image_url: builtins.str
    """Image URL."""
    image_base64: builtins.str
    """Base64-encoded image."""
    def __init__(
        self,
        *,
        image_url: builtins.str = ...,
        image_base64: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["image_base64", b"image_base64", "image_url", b"image_url", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["image_base64", b"image_base64", "image_url", b"image_url", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["image_url", "image_base64"] | None: ...

global___InstanceSegmentationInput = InstanceSegmentationInput

@typing_extensions.final
class InstanceSegmentationInputStream(google.protobuf.message.Message):
    """InstanceSegmentationInputStream represents the input of an instance
    segmentation task when the input is streamed as binary files.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_LENGTHS_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    @property
    def file_lengths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """File length for each uploaded binary file."""
    content: builtins.bytes
    """Byte representation of the images."""
    def __init__(
        self,
        *,
        file_lengths: collections.abc.Iterable[builtins.int] | None = ...,
        content: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content", b"content", "file_lengths", b"file_lengths"]) -> None: ...

global___InstanceSegmentationInputStream = InstanceSegmentationInputStream

@typing_extensions.final
class InstanceSegmentationOutput(google.protobuf.message.Message):
    """InstanceSegmentationOutput contains the result of an instance segmentation
    task.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECTS_FIELD_NUMBER: builtins.int
    @property
    def objects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InstanceSegmentationObject]:
        """A list of instance segmentation objects."""
    def __init__(
        self,
        *,
        objects: collections.abc.Iterable[global___InstanceSegmentationObject] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["objects", b"objects"]) -> None: ...

global___InstanceSegmentationOutput = InstanceSegmentationOutput
