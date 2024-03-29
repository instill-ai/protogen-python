"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import common.healthcheck.v1beta.healthcheck_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

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

@typing_extensions.final
class RepositoryTag(google.protobuf.message.Message):
    """

    This API is under development and, therefore, some of its entitites and
    entpoints are not implemented yet. This section aims to give context about the
    current interface and how it fits in the Artifact vision.

    # Artifact

    The Artifact domain is responsible of storing data that will later be used for
    processing unstructured data. Artifact will support the following types of
    data:

    - Repositories
    - Objects
    - Vectors

    ## Repositories

    An implementation of the [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec?tab=readme-ov-file)
    is used to manage versioned content. The main use for repositories is storing
    container images that can be used to deploy AI models or VDP pipelines.

    The ID of a repository has 2 segments, the owner (an Instill user or
    organization) and the content ID (the AI model or pipeline ID), e.g.
    `curious-wombat/llava-34b`.

    ## Objects

    Raw data is stored in binary blobs. Object storage allows users to upload data
    (e.g. images, audio) that can be used by pipelines or to store the results or a
    pipeline trigger.

    ## Vectors

    Vector embeddings have their own storage, which allows fast retrieval and similarity search.

    RepositoryTag contains information about the version of some content in a
    repository.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    DIGEST_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of the tag, defined by its parent repository and ID.
    - Format: `repositories/{repository.id}/tags/{tag.id}`.
    """
    id: builtins.str
    """The tag identifier."""
    digest: builtins.str
    """The Artifact backend will register the tag digest and timestamp when a
    new version is pushed. However, the registry remains the source of truth
    for tags, so if this information isn't found in the Artifact database,
    these fields will be empty.

    Unique identifier, computed from the manifest the tag refers to.
    """
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Tag update time, i.e. timestamp of the last push."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        id: builtins.str = ...,
        digest: builtins.str = ...,
        update_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_time", b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["digest", b"digest", "id", b"id", "name", b"name", "update_time", b"update_time"]) -> None: ...

global___RepositoryTag = RepositoryTag

@typing_extensions.final
class ListRepositoryTagsRequest(google.protobuf.message.Message):
    """ListRepositoryTagsRequest represents a request to list the tags of a
    repository.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """The maximum number of tags to return. The default and cap values are 10
    and 100, respectively.
    """
    page: builtins.int
    """Page number."""
    parent: builtins.str
    """The repository holding the different versions of a given content.
    - Format: `repositories/{repository.id}`.
    - Example: `repositories/flaming-wombat/llama-2-7b`.
    """
    def __init__(
        self,
        *,
        page_size: builtins.int | None = ...,
        page: builtins.int | None = ...,
        parent: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_page", b"_page", "_page_size", b"_page_size", "page", b"page", "page_size", b"page_size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_page", b"_page", "_page_size", b"_page_size", "page", b"page", "page_size", b"page_size", "parent", b"parent"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_page", b"_page"]) -> typing_extensions.Literal["page"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_page_size", b"_page_size"]) -> typing_extensions.Literal["page_size"] | None: ...

global___ListRepositoryTagsRequest = ListRepositoryTagsRequest

@typing_extensions.final
class ListRepositoryTagsResponse(google.protobuf.message.Message):
    """ListRepositoryTagsResponse contains a list of container image tags."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TAGS_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RepositoryTag]:
        """A list of repository tags."""
    total_size: builtins.int
    """Total number of tags."""
    page_size: builtins.int
    """The requested page size."""
    page: builtins.int
    """The requested page offset."""
    def __init__(
        self,
        *,
        tags: collections.abc.Iterable[global___RepositoryTag] | None = ...,
        total_size: builtins.int = ...,
        page_size: builtins.int = ...,
        page: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page", b"page", "page_size", b"page_size", "tags", b"tags", "total_size", b"total_size"]) -> None: ...

global___ListRepositoryTagsResponse = ListRepositoryTagsResponse

@typing_extensions.final
class CreateRepositoryTagRequest(google.protobuf.message.Message):
    """CreateRepositoryTagRequest represents a request to add a tag to a given
    repository.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TAG_FIELD_NUMBER: builtins.int
    @property
    def tag(self) -> global___RepositoryTag:
        """The tag information."""
    def __init__(
        self,
        *,
        tag: global___RepositoryTag | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tag", b"tag"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tag", b"tag"]) -> None: ...

global___CreateRepositoryTagRequest = CreateRepositoryTagRequest

@typing_extensions.final
class CreateRepositoryTagResponse(google.protobuf.message.Message):
    """CreateRepositoryTagResponse contains the created tag."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TAG_FIELD_NUMBER: builtins.int
    @property
    def tag(self) -> global___RepositoryTag:
        """The created tag."""
    def __init__(
        self,
        *,
        tag: global___RepositoryTag | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tag", b"tag"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tag", b"tag"]) -> None: ...

global___CreateRepositoryTagResponse = CreateRepositoryTagResponse
