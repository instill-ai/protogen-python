"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import artifact.artifact.v1alpha.artifact_pb2
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class ArtifactPrivateServiceStub:
    """ArtifactPrivateService exposes the private endpoints that allow clients to
    manage artifacts.
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    ListRepositoryTags: grpc.UnaryUnaryMultiCallable[
        artifact.artifact.v1alpha.artifact_pb2.ListRepositoryTagsRequest,
        artifact.artifact.v1alpha.artifact_pb2.ListRepositoryTagsResponse,
    ]
    """List the tags in a repository.

    Returns a portion of the versions that the specified repository holds.
    """
    CreateRepositoryTag: grpc.UnaryUnaryMultiCallable[
        artifact.artifact.v1alpha.artifact_pb2.CreateRepositoryTagRequest,
        artifact.artifact.v1alpha.artifact_pb2.CreateRepositoryTagResponse,
    ]
    """Create a new repository tag.

    Adds a tag to a given repository. Note that this operation is only
    intended to register the information of an *already created* tag. This
    method should be called as part of the content push operation, right after
    the [PUT Manifest](https://distribution.github.io/distribution/#put-manifest) has
    succeeded. The distribution registry won't hold data such as the push time
    or the tag digest, so `artifact-backend` will hold this information locally.
    """

class ArtifactPrivateServiceAsyncStub:
    """ArtifactPrivateService exposes the private endpoints that allow clients to
    manage artifacts.
    """

    ListRepositoryTags: grpc.aio.UnaryUnaryMultiCallable[
        artifact.artifact.v1alpha.artifact_pb2.ListRepositoryTagsRequest,
        artifact.artifact.v1alpha.artifact_pb2.ListRepositoryTagsResponse,
    ]
    """List the tags in a repository.

    Returns a portion of the versions that the specified repository holds.
    """
    CreateRepositoryTag: grpc.aio.UnaryUnaryMultiCallable[
        artifact.artifact.v1alpha.artifact_pb2.CreateRepositoryTagRequest,
        artifact.artifact.v1alpha.artifact_pb2.CreateRepositoryTagResponse,
    ]
    """Create a new repository tag.

    Adds a tag to a given repository. Note that this operation is only
    intended to register the information of an *already created* tag. This
    method should be called as part of the content push operation, right after
    the [PUT Manifest](https://distribution.github.io/distribution/#put-manifest) has
    succeeded. The distribution registry won't hold data such as the push time
    or the tag digest, so `artifact-backend` will hold this information locally.
    """

class ArtifactPrivateServiceServicer(metaclass=abc.ABCMeta):
    """ArtifactPrivateService exposes the private endpoints that allow clients to
    manage artifacts.
    """

    @abc.abstractmethod
    def ListRepositoryTags(
        self,
        request: artifact.artifact.v1alpha.artifact_pb2.ListRepositoryTagsRequest,
        context: _ServicerContext,
    ) -> typing.Union[artifact.artifact.v1alpha.artifact_pb2.ListRepositoryTagsResponse, collections.abc.Awaitable[artifact.artifact.v1alpha.artifact_pb2.ListRepositoryTagsResponse]]:
        """List the tags in a repository.

        Returns a portion of the versions that the specified repository holds.
        """
    @abc.abstractmethod
    def CreateRepositoryTag(
        self,
        request: artifact.artifact.v1alpha.artifact_pb2.CreateRepositoryTagRequest,
        context: _ServicerContext,
    ) -> typing.Union[artifact.artifact.v1alpha.artifact_pb2.CreateRepositoryTagResponse, collections.abc.Awaitable[artifact.artifact.v1alpha.artifact_pb2.CreateRepositoryTagResponse]]:
        """Create a new repository tag.

        Adds a tag to a given repository. Note that this operation is only
        intended to register the information of an *already created* tag. This
        method should be called as part of the content push operation, right after
        the [PUT Manifest](https://distribution.github.io/distribution/#put-manifest) has
        succeeded. The distribution registry won't hold data such as the push time
        or the tag digest, so `artifact-backend` will hold this information locally.
        """

def add_ArtifactPrivateServiceServicer_to_server(servicer: ArtifactPrivateServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...