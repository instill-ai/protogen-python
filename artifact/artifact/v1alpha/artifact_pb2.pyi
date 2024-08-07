"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import common.healthcheck.v1beta.healthcheck_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _FileProcessStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FileProcessStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FileProcessStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FILE_PROCESS_STATUS_UNSPECIFIED: _FileProcessStatus.ValueType  # 0
    """UNSPECIFIED"""
    FILE_PROCESS_STATUS_NOTSTARTED: _FileProcessStatus.ValueType  # 1
    """NOTSTARTED"""
    FILE_PROCESS_STATUS_WAITING: _FileProcessStatus.ValueType  # 2
    """file is waiting for embedding process"""
    FILE_PROCESS_STATUS_CONVERTING: _FileProcessStatus.ValueType  # 3
    """file is converting"""
    FILE_PROCESS_STATUS_CHUNKING: _FileProcessStatus.ValueType  # 4
    """file is chunking"""
    FILE_PROCESS_STATUS_EMBEDDING: _FileProcessStatus.ValueType  # 5
    """file is embedding"""
    FILE_PROCESS_STATUS_COMPLETED: _FileProcessStatus.ValueType  # 6
    """completed"""
    FILE_PROCESS_STATUS_FAILED: _FileProcessStatus.ValueType  # 7
    """failed"""

class FileProcessStatus(_FileProcessStatus, metaclass=_FileProcessStatusEnumTypeWrapper):
    """file embedding process status"""

FILE_PROCESS_STATUS_UNSPECIFIED: FileProcessStatus.ValueType  # 0
"""UNSPECIFIED"""
FILE_PROCESS_STATUS_NOTSTARTED: FileProcessStatus.ValueType  # 1
"""NOTSTARTED"""
FILE_PROCESS_STATUS_WAITING: FileProcessStatus.ValueType  # 2
"""file is waiting for embedding process"""
FILE_PROCESS_STATUS_CONVERTING: FileProcessStatus.ValueType  # 3
"""file is converting"""
FILE_PROCESS_STATUS_CHUNKING: FileProcessStatus.ValueType  # 4
"""file is chunking"""
FILE_PROCESS_STATUS_EMBEDDING: FileProcessStatus.ValueType  # 5
"""file is embedding"""
FILE_PROCESS_STATUS_COMPLETED: FileProcessStatus.ValueType  # 6
"""completed"""
FILE_PROCESS_STATUS_FAILED: FileProcessStatus.ValueType  # 7
"""failed"""
global___FileProcessStatus = FileProcessStatus

class _FileType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FileTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FileType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FILE_TYPE_UNSPECIFIED: _FileType.ValueType  # 0
    """upsecifid"""
    FILE_TYPE_TEXT: _FileType.ValueType  # 1
    """text"""
    FILE_TYPE_PDF: _FileType.ValueType  # 2
    """PDF"""
    FILE_TYPE_MARKDOWN: _FileType.ValueType  # 3
    """MARKDOWN"""
    FILE_TYPE_PNG: _FileType.ValueType  # 4
    """PNG"""
    FILE_TYPE_JPEG: _FileType.ValueType  # 5
    """JPEG"""
    FILE_TYPE_JPG: _FileType.ValueType  # 6
    """JPG"""
    FILE_TYPE_HTML: _FileType.ValueType  # 7
    """HTML"""
    FILE_TYPE_DOCX: _FileType.ValueType  # 8
    """DOCX"""
    FILE_TYPE_DOC: _FileType.ValueType  # 9
    """DOC"""
    FILE_TYPE_PPT: _FileType.ValueType  # 10
    """PPT"""
    FILE_TYPE_PPTX: _FileType.ValueType  # 11
    """PPTX"""

class FileType(_FileType, metaclass=_FileTypeEnumTypeWrapper):
    """file type"""

FILE_TYPE_UNSPECIFIED: FileType.ValueType  # 0
"""upsecifid"""
FILE_TYPE_TEXT: FileType.ValueType  # 1
"""text"""
FILE_TYPE_PDF: FileType.ValueType  # 2
"""PDF"""
FILE_TYPE_MARKDOWN: FileType.ValueType  # 3
"""MARKDOWN"""
FILE_TYPE_PNG: FileType.ValueType  # 4
"""PNG"""
FILE_TYPE_JPEG: FileType.ValueType  # 5
"""JPEG"""
FILE_TYPE_JPG: FileType.ValueType  # 6
"""JPG"""
FILE_TYPE_HTML: FileType.ValueType  # 7
"""HTML"""
FILE_TYPE_DOCX: FileType.ValueType  # 8
"""DOCX"""
FILE_TYPE_DOC: FileType.ValueType  # 9
"""DOC"""
FILE_TYPE_PPT: FileType.ValueType  # 10
"""PPT"""
FILE_TYPE_PPTX: FileType.ValueType  # 11
"""PPTX"""
global___FileType = FileType

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

@typing_extensions.final
class GetRepositoryTagRequest(google.protobuf.message.Message):
    """GetRepositoryTagRequest represents a request to add a tag to a given
    repository.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of the tag, defined by its parent repository and ID.
    - Format: `repositories/{repository.id}/tags/{tag.id}`.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___GetRepositoryTagRequest = GetRepositoryTagRequest

@typing_extensions.final
class GetRepositoryTagResponse(google.protobuf.message.Message):
    """GetRepositoryTagResponse contains the created tag."""

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

global___GetRepositoryTagResponse = GetRepositoryTagResponse

@typing_extensions.final
class DeleteRepositoryTagRequest(google.protobuf.message.Message):
    """DeleteRepositoryTagRequest represents a request to delete a tag to a given
    repository.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of the tag, defined by its parent repository and ID.
    - Format: `repositories/{repository.id}/tags/{tag.id}`.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___DeleteRepositoryTagRequest = DeleteRepositoryTagRequest

@typing_extensions.final
class DeleteRepositoryTagResponse(google.protobuf.message.Message):
    """DeleteRepositoryTagResponse represent an empty response."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteRepositoryTagResponse = DeleteRepositoryTagResponse

@typing_extensions.final
class Catalog(google.protobuf.message.Message):
    """Catalog represents a catalog."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CATALOG_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    OWNER_NAME_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    CONVERTING_PIPELINES_FIELD_NUMBER: builtins.int
    SPLITTING_PIPELINES_FIELD_NUMBER: builtins.int
    EMBEDDING_PIPELINES_FIELD_NUMBER: builtins.int
    DOWNSTREAM_APPS_FIELD_NUMBER: builtins.int
    TOTAL_FILES_FIELD_NUMBER: builtins.int
    TOTAL_TOKENS_FIELD_NUMBER: builtins.int
    USED_STORAGE_FIELD_NUMBER: builtins.int
    catalog_id: builtins.str
    """The catalog id."""
    name: builtins.str
    """The catalog name."""
    description: builtins.str
    """The catalog description."""
    create_time: builtins.str
    """The creation time of the catalog."""
    update_time: builtins.str
    """The last update time of the catalog."""
    owner_name: builtins.str
    """The owner/namespaceof the catalog."""
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The catalog tags."""
    @property
    def converting_pipelines(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The catalog converting pipelines."""
    @property
    def splitting_pipelines(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The catalog splitting pipelines."""
    @property
    def embedding_pipelines(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The catalog embedding pipelines."""
    @property
    def downstream_apps(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The downstream apps"""
    total_files: builtins.int
    """The total files in catalog."""
    total_tokens: builtins.int
    """The total tokens in catalog."""
    used_storage: builtins.int
    """The current used storage in catalog."""
    def __init__(
        self,
        *,
        catalog_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        create_time: builtins.str = ...,
        update_time: builtins.str = ...,
        owner_name: builtins.str = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
        converting_pipelines: collections.abc.Iterable[builtins.str] | None = ...,
        splitting_pipelines: collections.abc.Iterable[builtins.str] | None = ...,
        embedding_pipelines: collections.abc.Iterable[builtins.str] | None = ...,
        downstream_apps: collections.abc.Iterable[builtins.str] | None = ...,
        total_files: builtins.int = ...,
        total_tokens: builtins.int = ...,
        used_storage: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog_id", b"catalog_id", "converting_pipelines", b"converting_pipelines", "create_time", b"create_time", "description", b"description", "downstream_apps", b"downstream_apps", "embedding_pipelines", b"embedding_pipelines", "name", b"name", "owner_name", b"owner_name", "splitting_pipelines", b"splitting_pipelines", "tags", b"tags", "total_files", b"total_files", "total_tokens", b"total_tokens", "update_time", b"update_time", "used_storage", b"used_storage"]) -> None: ...

global___Catalog = Catalog

@typing_extensions.final
class CreateCatalogRequest(google.protobuf.message.Message):
    """CreateCatalogRequest represents a request to create a catalog."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The catalog's owner(nammespace)."""
    name: builtins.str
    """The catalog name."""
    description: builtins.str
    """The catalog description."""
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The catalog tags."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "name", b"name", "namespace_id", b"namespace_id", "tags", b"tags"]) -> None: ...

global___CreateCatalogRequest = CreateCatalogRequest

@typing_extensions.final
class CreateCatalogResponse(google.protobuf.message.Message):
    """CreateCatalogResponse represents a response for creating a catalog."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CATALOG_FIELD_NUMBER: builtins.int
    @property
    def catalog(self) -> global___Catalog:
        """The created catalog."""
    def __init__(
        self,
        *,
        catalog: global___Catalog | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["catalog", b"catalog"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog", b"catalog"]) -> None: ...

global___CreateCatalogResponse = CreateCatalogResponse

@typing_extensions.final
class ListCatalogsRequest(google.protobuf.message.Message):
    """Request message for ListCatalogs"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """User ID for which to list the catalogs"""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["namespace_id", b"namespace_id"]) -> None: ...

global___ListCatalogsRequest = ListCatalogsRequest

@typing_extensions.final
class ListCatalogsResponse(google.protobuf.message.Message):
    """GetCatalogsResponse represents a response for getting all catalogs from users."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CATALOGS_FIELD_NUMBER: builtins.int
    @property
    def catalogs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Catalog]:
        """The catalogs container."""
    def __init__(
        self,
        *,
        catalogs: collections.abc.Iterable[global___Catalog] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalogs", b"catalogs"]) -> None: ...

global___ListCatalogsResponse = ListCatalogsResponse

@typing_extensions.final
class UpdateCatalogRequest(google.protobuf.message.Message):
    """UpdateCatalogRequest represents a request to update a catalog."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CATALOG_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    catalog_id: builtins.str
    """The catalog id."""
    description: builtins.str
    """The catalog description."""
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The catalog tags."""
    namespace_id: builtins.str
    """The catalog owner(namespace)."""
    def __init__(
        self,
        *,
        catalog_id: builtins.str = ...,
        description: builtins.str = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
        namespace_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog_id", b"catalog_id", "description", b"description", "namespace_id", b"namespace_id", "tags", b"tags"]) -> None: ...

global___UpdateCatalogRequest = UpdateCatalogRequest

@typing_extensions.final
class UpdateCatalogResponse(google.protobuf.message.Message):
    """UpdateCatalogResponse represents a response for updating a catalog."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CATALOG_FIELD_NUMBER: builtins.int
    @property
    def catalog(self) -> global___Catalog:
        """The updated catalog."""
    def __init__(
        self,
        *,
        catalog: global___Catalog | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["catalog", b"catalog"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog", b"catalog"]) -> None: ...

global___UpdateCatalogResponse = UpdateCatalogResponse

@typing_extensions.final
class DeleteCatalogRequest(google.protobuf.message.Message):
    """DeleteCatalogRequest represents a request to delete a catalog."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    CATALOG_ID_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The owner's id. i.e. namespace."""
    catalog_id: builtins.str
    """The catalog id."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        catalog_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog_id", b"catalog_id", "namespace_id", b"namespace_id"]) -> None: ...

global___DeleteCatalogRequest = DeleteCatalogRequest

@typing_extensions.final
class DeleteCatalogResponse(google.protobuf.message.Message):
    """DeleteCatalogResponse represents a response for deleting a catalog."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CATALOG_FIELD_NUMBER: builtins.int
    @property
    def catalog(self) -> global___Catalog:
        """The catalog identifier."""
    def __init__(
        self,
        *,
        catalog: global___Catalog | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["catalog", b"catalog"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog", b"catalog"]) -> None: ...

global___DeleteCatalogResponse = DeleteCatalogResponse

@typing_extensions.final
class File(google.protobuf.message.Message):
    """file mata data"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_UID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PROCESS_STATUS_FIELD_NUMBER: builtins.int
    PROCESS_OUTCOME_FIELD_NUMBER: builtins.int
    RETRIEVABLE_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    OWNER_UID_FIELD_NUMBER: builtins.int
    CREATOR_UID_FIELD_NUMBER: builtins.int
    CATALOG_UID_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    DELETE_TIME_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    TOTAL_CHUNKS_FIELD_NUMBER: builtins.int
    TOTAL_TOKENS_FIELD_NUMBER: builtins.int
    file_uid: builtins.str
    """file uid"""
    name: builtins.str
    """file name"""
    type: global___FileType.ValueType
    """file type"""
    process_status: global___FileProcessStatus.ValueType
    """file process status"""
    process_outcome: builtins.str
    """file process message"""
    retrievable: builtins.bool
    """retrievable(this is reserved for future use)"""
    content: builtins.str
    """contect(this is reserved for future use)"""
    owner_uid: builtins.str
    """owner/namespaceuid"""
    creator_uid: builtins.str
    """cretor uid from authn token"""
    catalog_uid: builtins.str
    """catalog uid"""
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """create time"""
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """update time"""
    @property
    def delete_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """delete time"""
    size: builtins.int
    """file size in bytes"""
    total_chunks: builtins.int
    """total chunks"""
    total_tokens: builtins.int
    """total tokens"""
    def __init__(
        self,
        *,
        file_uid: builtins.str = ...,
        name: builtins.str = ...,
        type: global___FileType.ValueType = ...,
        process_status: global___FileProcessStatus.ValueType = ...,
        process_outcome: builtins.str = ...,
        retrievable: builtins.bool = ...,
        content: builtins.str = ...,
        owner_uid: builtins.str = ...,
        creator_uid: builtins.str = ...,
        catalog_uid: builtins.str = ...,
        create_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        update_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        delete_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        size: builtins.int = ...,
        total_chunks: builtins.int = ...,
        total_tokens: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time", b"create_time", "delete_time", b"delete_time", "update_time", b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog_uid", b"catalog_uid", "content", b"content", "create_time", b"create_time", "creator_uid", b"creator_uid", "delete_time", b"delete_time", "file_uid", b"file_uid", "name", b"name", "owner_uid", b"owner_uid", "process_outcome", b"process_outcome", "process_status", b"process_status", "retrievable", b"retrievable", "size", b"size", "total_chunks", b"total_chunks", "total_tokens", b"total_tokens", "type", b"type", "update_time", b"update_time"]) -> None: ...

global___File = File

@typing_extensions.final
class UploadCatalogFileRequest(google.protobuf.message.Message):
    """upload file request"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    CATALOG_ID_FIELD_NUMBER: builtins.int
    FILE_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """owner/namespace uid"""
    catalog_id: builtins.str
    """catalog id"""
    @property
    def file(self) -> global___File:
        """file"""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        catalog_id: builtins.str = ...,
        file: global___File | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["file", b"file"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog_id", b"catalog_id", "file", b"file", "namespace_id", b"namespace_id"]) -> None: ...

global___UploadCatalogFileRequest = UploadCatalogFileRequest

@typing_extensions.final
class UploadCatalogFileResponse(google.protobuf.message.Message):
    """upload file response"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_FIELD_NUMBER: builtins.int
    @property
    def file(self) -> global___File:
        """file"""
    def __init__(
        self,
        *,
        file: global___File | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["file", b"file"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["file", b"file"]) -> None: ...

global___UploadCatalogFileResponse = UploadCatalogFileResponse

@typing_extensions.final
class DeleteCatalogFileRequest(google.protobuf.message.Message):
    """delete file request"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_UID_FIELD_NUMBER: builtins.int
    file_uid: builtins.str
    """The file uid."""
    def __init__(
        self,
        *,
        file_uid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_uid", b"file_uid"]) -> None: ...

global___DeleteCatalogFileRequest = DeleteCatalogFileRequest

@typing_extensions.final
class DeleteCatalogFileResponse(google.protobuf.message.Message):
    """delete file response"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_UID_FIELD_NUMBER: builtins.int
    file_uid: builtins.str
    """The file uid."""
    def __init__(
        self,
        *,
        file_uid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_uid", b"file_uid"]) -> None: ...

global___DeleteCatalogFileResponse = DeleteCatalogFileResponse

@typing_extensions.final
class ProcessCatalogFilesRequest(google.protobuf.message.Message):
    """Process Catalog File Request"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_UIDS_FIELD_NUMBER: builtins.int
    @property
    def file_uids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The file uid."""
    def __init__(
        self,
        *,
        file_uids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_uids", b"file_uids"]) -> None: ...

global___ProcessCatalogFilesRequest = ProcessCatalogFilesRequest

@typing_extensions.final
class ProcessCatalogFilesResponse(google.protobuf.message.Message):
    """Process Catalog File Response"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILES_FIELD_NUMBER: builtins.int
    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]:
        """The file uid."""
    def __init__(
        self,
        *,
        files: collections.abc.Iterable[global___File] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["files", b"files"]) -> None: ...

global___ProcessCatalogFilesResponse = ProcessCatalogFilesResponse

@typing_extensions.final
class ListCatalogFilesFilter(google.protobuf.message.Message):
    """list file filter
    todo: support more parameters
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_UIDS_FIELD_NUMBER: builtins.int
    @property
    def file_uids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """The file uids."""
    def __init__(
        self,
        *,
        file_uids: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_uids", b"file_uids"]) -> None: ...

global___ListCatalogFilesFilter = ListCatalogFilesFilter

@typing_extensions.final
class ListCatalogFilesRequest(google.protobuf.message.Message):
    """list files request"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    CATALOG_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The owner/namespaceuid id."""
    catalog_id: builtins.str
    """The catalog id."""
    page_size: builtins.int
    """The page size (default:10; max 100)."""
    page_token: builtins.str
    """The next page token(default from first file's token)."""
    @property
    def filter(self) -> global___ListCatalogFilesFilter:
        """The filter."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        catalog_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: global___ListCatalogFilesFilter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter", b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog_id", b"catalog_id", "filter", b"filter", "namespace_id", b"namespace_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListCatalogFilesRequest = ListCatalogFilesRequest

@typing_extensions.final
class ListCatalogFilesResponse(google.protobuf.message.Message):
    """list files response"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILES_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___File]:
        """The list of files."""
    total_size: builtins.int
    """The total number of files."""
    page_size: builtins.int
    """The requested page size."""
    next_page_token: builtins.str
    """next page token"""
    @property
    def filter(self) -> global___ListCatalogFilesFilter:
        """The filter."""
    def __init__(
        self,
        *,
        files: collections.abc.Iterable[global___File] | None = ...,
        total_size: builtins.int = ...,
        page_size: builtins.int = ...,
        next_page_token: builtins.str = ...,
        filter: global___ListCatalogFilesFilter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter", b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["files", b"files", "filter", b"filter", "next_page_token", b"next_page_token", "page_size", b"page_size", "total_size", b"total_size"]) -> None: ...

global___ListCatalogFilesResponse = ListCatalogFilesResponse
