"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import artifact.artifact.v1alpha.artifact_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Folder(google.protobuf.message.Message):
    """Folder represents a folder resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Permission(google.protobuf.message.Message):
        """Permission defines how a folder can be used."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CAN_EDIT_FIELD_NUMBER: builtins.int
        can_edit: builtins.bool
        """Defines whether the folder can be modified."""
        def __init__(
            self,
            *,
            can_edit: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["can_edit", b"can_edit"]) -> None: ...

    UID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    CATALOG_ID_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    CATALOG_INFO_FIELD_NUMBER: builtins.int
    uid: builtins.str
    """The unique identifier of the folder."""
    name: builtins.str
    """The name of the folder."""
    description: builtins.str
    """A description of the folder."""
    @property
    def metadata(self) -> google.protobuf.struct_pb2.Struct:
        """Additional metadata associated with the folder."""
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp when the folder was created."""
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The timestamp when the folder was last updated."""
    catalog_id: builtins.str
    """The ID of the catalog that this folder is bound to."""
    @property
    def permission(self) -> global___Folder.Permission:
        """Permission defines how a folder can be used."""
    @property
    def catalog_info(self) -> global___CatalogInfo:
        """The information about the catalog."""
    def __init__(
        self,
        *,
        uid: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        metadata: google.protobuf.struct_pb2.Struct | None = ...,
        create_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        update_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        catalog_id: builtins.str = ...,
        permission: global___Folder.Permission | None = ...,
        catalog_info: global___CatalogInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["catalog_info", b"catalog_info", "create_time", b"create_time", "metadata", b"metadata", "permission", b"permission", "update_time", b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["catalog_id", b"catalog_id", "catalog_info", b"catalog_info", "create_time", b"create_time", "description", b"description", "metadata", b"metadata", "name", b"name", "permission", b"permission", "uid", b"uid", "update_time", b"update_time"]) -> None: ...

global___Folder = Folder

@typing_extensions.final
class CatalogInfo(google.protobuf.message.Message):
    """CatalogInfo contains the information about the catalog."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_COUNT_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_BYTES_FIELD_NUMBER: builtins.int
    file_count: builtins.int
    """The number of files in the catalog."""
    total_size_bytes: builtins.int
    """The total size of all files in the catalog in bytes."""
    def __init__(
        self,
        *,
        file_count: builtins.int = ...,
        total_size_bytes: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_count", b"file_count", "total_size_bytes", b"total_size_bytes"]) -> None: ...

global___CatalogInfo = CatalogInfo

@typing_extensions.final
class ListFoldersRequest(google.protobuf.message.Message):
    """ListFoldersRequest represents a request to list folders."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The ID of the namespace that owns the folders."""
    page_token: builtins.str
    """The page token for pagination."""
    page_size: builtins.int
    """The maximum number of folders to return."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        page_token: builtins.str = ...,
        page_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["namespace_id", b"namespace_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListFoldersRequest = ListFoldersRequest

@typing_extensions.final
class ListFoldersResponse(google.protobuf.message.Message):
    """ListFoldersResponse contains the list of folders."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    @property
    def folders(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Folder]:
        """The list of folders."""
    next_page_token: builtins.str
    """The token for the next page of results."""
    total_size: builtins.int
    """The total number of tables."""
    def __init__(
        self,
        *,
        folders: collections.abc.Iterable[global___Folder] | None = ...,
        next_page_token: builtins.str = ...,
        total_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folders", b"folders", "next_page_token", b"next_page_token", "total_size", b"total_size"]) -> None: ...

global___ListFoldersResponse = ListFoldersResponse

@typing_extensions.final
class CreateFolderRequest(google.protobuf.message.Message):
    """CreateFolderRequest represents a request to create a folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    FOLDER_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The ID of the namespace where the folder will be created."""
    @property
    def folder(self) -> global___Folder:
        """The folder resource to create."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        folder: global___Folder | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["folder", b"folder"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder", b"folder", "namespace_id", b"namespace_id"]) -> None: ...

global___CreateFolderRequest = CreateFolderRequest

@typing_extensions.final
class CreateFolderResponse(google.protobuf.message.Message):
    """CreateFolderResponse contains the created folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_FIELD_NUMBER: builtins.int
    @property
    def folder(self) -> global___Folder:
        """The created folder resource."""
    def __init__(
        self,
        *,
        folder: global___Folder | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["folder", b"folder"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder", b"folder"]) -> None: ...

global___CreateFolderResponse = CreateFolderResponse

@typing_extensions.final
class GetFolderRequest(google.protobuf.message.Message):
    """GetFolderRequest represents a request to fetch a folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    FOLDER_UID_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The ID of the namespace that owns the folder."""
    folder_uid: builtins.str
    """The UID of the folder to fetch."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        folder_uid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_uid", b"folder_uid", "namespace_id", b"namespace_id"]) -> None: ...

global___GetFolderRequest = GetFolderRequest

@typing_extensions.final
class GetFolderResponse(google.protobuf.message.Message):
    """GetFolderResponse contains the requested folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_FIELD_NUMBER: builtins.int
    @property
    def folder(self) -> global___Folder:
        """The folder resource."""
    def __init__(
        self,
        *,
        folder: global___Folder | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["folder", b"folder"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder", b"folder"]) -> None: ...

global___GetFolderResponse = GetFolderResponse

@typing_extensions.final
class UpdateFolderRequest(google.protobuf.message.Message):
    """UpdateFolderRequest represents a request to update a folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    FOLDER_UID_FIELD_NUMBER: builtins.int
    FOLDER_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The ID of the namespace that owns the folder."""
    folder_uid: builtins.str
    """The UID of the folder to update."""
    @property
    def folder(self) -> global___Folder:
        """The folder fields that will replace the existing ones."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """The update mask specifies the subset of fields that should be modified."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        folder_uid: builtins.str = ...,
        folder: global___Folder | None = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["folder", b"folder", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder", b"folder", "folder_uid", b"folder_uid", "namespace_id", b"namespace_id", "update_mask", b"update_mask"]) -> None: ...

global___UpdateFolderRequest = UpdateFolderRequest

@typing_extensions.final
class UpdateFolderResponse(google.protobuf.message.Message):
    """UpdateFolderResponse contains the updated folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_FIELD_NUMBER: builtins.int
    @property
    def folder(self) -> global___Folder:
        """The updated folder resource."""
    def __init__(
        self,
        *,
        folder: global___Folder | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["folder", b"folder"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder", b"folder"]) -> None: ...

global___UpdateFolderResponse = UpdateFolderResponse

@typing_extensions.final
class DeleteFolderRequest(google.protobuf.message.Message):
    """DeleteFolderRequest represents a request to delete a folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    FOLDER_UID_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The ID of the namespace that owns the folder."""
    folder_uid: builtins.str
    """The UID of the folder to delete."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        folder_uid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["folder_uid", b"folder_uid", "namespace_id", b"namespace_id"]) -> None: ...

global___DeleteFolderRequest = DeleteFolderRequest

@typing_extensions.final
class DeleteFolderResponse(google.protobuf.message.Message):
    """DeleteFolderResponse is an empty response for deleting a folder."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteFolderResponse = DeleteFolderResponse

@typing_extensions.final
class CreateFolderFileRequest(google.protobuf.message.Message):
    """create folder file request"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    FOLDER_UID_FIELD_NUMBER: builtins.int
    FILE_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """owner/namespace uid"""
    folder_uid: builtins.str
    """folder uid"""
    @property
    def file(self) -> artifact.artifact.v1alpha.artifact_pb2.File:
        """file"""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        folder_uid: builtins.str = ...,
        file: artifact.artifact.v1alpha.artifact_pb2.File | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["file", b"file"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["file", b"file", "folder_uid", b"folder_uid", "namespace_id", b"namespace_id"]) -> None: ...

global___CreateFolderFileRequest = CreateFolderFileRequest

@typing_extensions.final
class CreateFolderFileResponse(google.protobuf.message.Message):
    """create folder file response"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_FIELD_NUMBER: builtins.int
    @property
    def file(self) -> artifact.artifact.v1alpha.artifact_pb2.File:
        """file"""
    def __init__(
        self,
        *,
        file: artifact.artifact.v1alpha.artifact_pb2.File | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["file", b"file"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["file", b"file"]) -> None: ...

global___CreateFolderFileResponse = CreateFolderFileResponse

@typing_extensions.final
class DeleteFolderFileRequest(google.protobuf.message.Message):
    """delete folder file request"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    FOLDER_UID_FIELD_NUMBER: builtins.int
    FILE_UID_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The namespace id."""
    folder_uid: builtins.str
    """The folder uid."""
    file_uid: builtins.str
    """The file uid."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        folder_uid: builtins.str = ...,
        file_uid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_uid", b"file_uid", "folder_uid", b"folder_uid", "namespace_id", b"namespace_id"]) -> None: ...

global___DeleteFolderFileRequest = DeleteFolderFileRequest

@typing_extensions.final
class DeleteFolderFileResponse(google.protobuf.message.Message):
    """delete folder file response"""

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

global___DeleteFolderFileResponse = DeleteFolderFileResponse

@typing_extensions.final
class ListFolderFilesRequest(google.protobuf.message.Message):
    """list folder files request"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    FOLDER_UID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The owner/namespace uid id."""
    folder_uid: builtins.str
    """The folder uid."""
    page_size: builtins.int
    """The page size (default:10; max 100)."""
    page_token: builtins.str
    """The next page token(default from first file's token)."""
    @property
    def filter(self) -> artifact.artifact.v1alpha.artifact_pb2.ListCatalogFilesFilter:
        """The filter."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        folder_uid: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: artifact.artifact.v1alpha.artifact_pb2.ListCatalogFilesFilter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter", b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter", b"filter", "folder_uid", b"folder_uid", "namespace_id", b"namespace_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListFolderFilesRequest = ListFolderFilesRequest

@typing_extensions.final
class ListFolderFilesResponse(google.protobuf.message.Message):
    """list folder files response"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILES_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[artifact.artifact.v1alpha.artifact_pb2.File]:
        """The list of files."""
    total_size: builtins.int
    """The total number of files."""
    page_size: builtins.int
    """The requested page size."""
    next_page_token: builtins.str
    """next page token"""
    @property
    def filter(self) -> artifact.artifact.v1alpha.artifact_pb2.ListCatalogFilesFilter:
        """The filter."""
    def __init__(
        self,
        *,
        files: collections.abc.Iterable[artifact.artifact.v1alpha.artifact_pb2.File] | None = ...,
        total_size: builtins.int = ...,
        page_size: builtins.int = ...,
        next_page_token: builtins.str = ...,
        filter: artifact.artifact.v1alpha.artifact_pb2.ListCatalogFilesFilter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter", b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["files", b"files", "filter", b"filter", "next_page_token", b"next_page_token", "page_size", b"page_size", "total_size", b"total_size"]) -> None: ...

global___ListFolderFilesResponse = ListFolderFilesResponse

@typing_extensions.final
class GetFolderFileRequest(google.protobuf.message.Message):
    """GetFolderFileRequest represents a request to get a folder file."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    FOLDER_UID_FIELD_NUMBER: builtins.int
    FILE_UID_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    """The namespace id."""
    folder_uid: builtins.str
    """The folder uid."""
    file_uid: builtins.str
    """The file uid."""
    def __init__(
        self,
        *,
        namespace_id: builtins.str = ...,
        folder_uid: builtins.str = ...,
        file_uid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_uid", b"file_uid", "folder_uid", b"folder_uid", "namespace_id", b"namespace_id"]) -> None: ...

global___GetFolderFileRequest = GetFolderFileRequest

@typing_extensions.final
class GetFolderFileResponse(google.protobuf.message.Message):
    """GetFolderFileResponse represents a response for getting a folder file."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_FIELD_NUMBER: builtins.int
    @property
    def file(self) -> artifact.artifact.v1alpha.artifact_pb2.File:
        """The file."""
    def __init__(
        self,
        *,
        file: artifact.artifact.v1alpha.artifact_pb2.File | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["file", b"file"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["file", b"file"]) -> None: ...

global___GetFolderFileResponse = GetFolderFileResponse
