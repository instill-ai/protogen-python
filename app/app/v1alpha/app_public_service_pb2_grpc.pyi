"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import app.app.v1alpha.app_pb2
import app.app.v1alpha.conversation_pb2
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class AppPublicServiceStub:
    """AppPublicService exposes the public endpoints that allow clients to
    manage apps.
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Liveness: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.LivenessRequest,
        app.app.v1alpha.app_pb2.LivenessResponse,
    ]
    """Check if the app server is alive

    See https://github.com/grpc/grpc/blob/master/doc/health-checking.md.
    """
    Readiness: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.ReadinessRequest,
        app.app.v1alpha.app_pb2.ReadinessResponse,
    ]
    """Check if the app server is ready

    See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
    """
    CreateApp: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.CreateAppRequest,
        app.app.v1alpha.app_pb2.CreateAppResponse,
    ]
    """Create a App"""
    ListApps: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.ListAppsRequest,
        app.app.v1alpha.app_pb2.ListAppsResponse,
    ]
    """Get all apps info"""
    UpdateApp: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.UpdateAppRequest,
        app.app.v1alpha.app_pb2.UpdateAppResponse,
    ]
    """Update a app info"""
    DeleteApp: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.DeleteAppRequest,
        app.app.v1alpha.app_pb2.DeleteAppResponse,
    ]
    """Delete a app"""
    CreateConversation: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.CreateConversationRequest,
        app.app.v1alpha.conversation_pb2.CreateConversationResponse,
    ]
    """Create a Conversation"""
    ListConversations: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.ListConversationsRequest,
        app.app.v1alpha.conversation_pb2.ListConversationsResponse,
    ]
    """List conversations"""
    UpdateConversation: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.UpdateConversationRequest,
        app.app.v1alpha.conversation_pb2.UpdateConversationResponse,
    ]
    """Update a conversation"""
    DeleteConversation: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.DeleteConversationRequest,
        app.app.v1alpha.conversation_pb2.DeleteConversationResponse,
    ]
    """Delete a conversation"""
    CreateMessage: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.CreateMessageRequest,
        app.app.v1alpha.conversation_pb2.CreateMessageResponse,
    ]
    """Create a message"""
    ListMessages: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.ListMessagesRequest,
        app.app.v1alpha.conversation_pb2.ListMessagesResponse,
    ]
    """List messages"""
    UpdateMessage: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.UpdateMessageRequest,
        app.app.v1alpha.conversation_pb2.UpdateMessageResponse,
    ]
    """Update a message"""
    DeleteMessage: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.DeleteMessageRequest,
        app.app.v1alpha.conversation_pb2.DeleteMessageResponse,
    ]
    """Delete a message"""
    UpdateAiAssistantAppPlayground: grpc.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.UpdateAiAssistantAppPlaygroundRequest,
        app.app.v1alpha.app_pb2.UpdateAiAssistantAppPlaygroundResponse,
    ]
    """Update ai assistant app playground"""

class AppPublicServiceAsyncStub:
    """AppPublicService exposes the public endpoints that allow clients to
    manage apps.
    """

    Liveness: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.LivenessRequest,
        app.app.v1alpha.app_pb2.LivenessResponse,
    ]
    """Check if the app server is alive

    See https://github.com/grpc/grpc/blob/master/doc/health-checking.md.
    """
    Readiness: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.ReadinessRequest,
        app.app.v1alpha.app_pb2.ReadinessResponse,
    ]
    """Check if the app server is ready

    See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
    """
    CreateApp: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.CreateAppRequest,
        app.app.v1alpha.app_pb2.CreateAppResponse,
    ]
    """Create a App"""
    ListApps: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.ListAppsRequest,
        app.app.v1alpha.app_pb2.ListAppsResponse,
    ]
    """Get all apps info"""
    UpdateApp: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.UpdateAppRequest,
        app.app.v1alpha.app_pb2.UpdateAppResponse,
    ]
    """Update a app info"""
    DeleteApp: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.DeleteAppRequest,
        app.app.v1alpha.app_pb2.DeleteAppResponse,
    ]
    """Delete a app"""
    CreateConversation: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.CreateConversationRequest,
        app.app.v1alpha.conversation_pb2.CreateConversationResponse,
    ]
    """Create a Conversation"""
    ListConversations: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.ListConversationsRequest,
        app.app.v1alpha.conversation_pb2.ListConversationsResponse,
    ]
    """List conversations"""
    UpdateConversation: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.UpdateConversationRequest,
        app.app.v1alpha.conversation_pb2.UpdateConversationResponse,
    ]
    """Update a conversation"""
    DeleteConversation: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.DeleteConversationRequest,
        app.app.v1alpha.conversation_pb2.DeleteConversationResponse,
    ]
    """Delete a conversation"""
    CreateMessage: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.CreateMessageRequest,
        app.app.v1alpha.conversation_pb2.CreateMessageResponse,
    ]
    """Create a message"""
    ListMessages: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.ListMessagesRequest,
        app.app.v1alpha.conversation_pb2.ListMessagesResponse,
    ]
    """List messages"""
    UpdateMessage: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.UpdateMessageRequest,
        app.app.v1alpha.conversation_pb2.UpdateMessageResponse,
    ]
    """Update a message"""
    DeleteMessage: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.conversation_pb2.DeleteMessageRequest,
        app.app.v1alpha.conversation_pb2.DeleteMessageResponse,
    ]
    """Delete a message"""
    UpdateAiAssistantAppPlayground: grpc.aio.UnaryUnaryMultiCallable[
        app.app.v1alpha.app_pb2.UpdateAiAssistantAppPlaygroundRequest,
        app.app.v1alpha.app_pb2.UpdateAiAssistantAppPlaygroundResponse,
    ]
    """Update ai assistant app playground"""

class AppPublicServiceServicer(metaclass=abc.ABCMeta):
    """AppPublicService exposes the public endpoints that allow clients to
    manage apps.
    """

    @abc.abstractmethod
    def Liveness(
        self,
        request: app.app.v1alpha.app_pb2.LivenessRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.app_pb2.LivenessResponse, collections.abc.Awaitable[app.app.v1alpha.app_pb2.LivenessResponse]]:
        """Check if the app server is alive

        See https://github.com/grpc/grpc/blob/master/doc/health-checking.md.
        """
    @abc.abstractmethod
    def Readiness(
        self,
        request: app.app.v1alpha.app_pb2.ReadinessRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.app_pb2.ReadinessResponse, collections.abc.Awaitable[app.app.v1alpha.app_pb2.ReadinessResponse]]:
        """Check if the app server is ready

        See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
        """
    @abc.abstractmethod
    def CreateApp(
        self,
        request: app.app.v1alpha.app_pb2.CreateAppRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.app_pb2.CreateAppResponse, collections.abc.Awaitable[app.app.v1alpha.app_pb2.CreateAppResponse]]:
        """Create a App"""
    @abc.abstractmethod
    def ListApps(
        self,
        request: app.app.v1alpha.app_pb2.ListAppsRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.app_pb2.ListAppsResponse, collections.abc.Awaitable[app.app.v1alpha.app_pb2.ListAppsResponse]]:
        """Get all apps info"""
    @abc.abstractmethod
    def UpdateApp(
        self,
        request: app.app.v1alpha.app_pb2.UpdateAppRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.app_pb2.UpdateAppResponse, collections.abc.Awaitable[app.app.v1alpha.app_pb2.UpdateAppResponse]]:
        """Update a app info"""
    @abc.abstractmethod
    def DeleteApp(
        self,
        request: app.app.v1alpha.app_pb2.DeleteAppRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.app_pb2.DeleteAppResponse, collections.abc.Awaitable[app.app.v1alpha.app_pb2.DeleteAppResponse]]:
        """Delete a app"""
    @abc.abstractmethod
    def CreateConversation(
        self,
        request: app.app.v1alpha.conversation_pb2.CreateConversationRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.conversation_pb2.CreateConversationResponse, collections.abc.Awaitable[app.app.v1alpha.conversation_pb2.CreateConversationResponse]]:
        """Create a Conversation"""
    @abc.abstractmethod
    def ListConversations(
        self,
        request: app.app.v1alpha.conversation_pb2.ListConversationsRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.conversation_pb2.ListConversationsResponse, collections.abc.Awaitable[app.app.v1alpha.conversation_pb2.ListConversationsResponse]]:
        """List conversations"""
    @abc.abstractmethod
    def UpdateConversation(
        self,
        request: app.app.v1alpha.conversation_pb2.UpdateConversationRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.conversation_pb2.UpdateConversationResponse, collections.abc.Awaitable[app.app.v1alpha.conversation_pb2.UpdateConversationResponse]]:
        """Update a conversation"""
    @abc.abstractmethod
    def DeleteConversation(
        self,
        request: app.app.v1alpha.conversation_pb2.DeleteConversationRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.conversation_pb2.DeleteConversationResponse, collections.abc.Awaitable[app.app.v1alpha.conversation_pb2.DeleteConversationResponse]]:
        """Delete a conversation"""
    @abc.abstractmethod
    def CreateMessage(
        self,
        request: app.app.v1alpha.conversation_pb2.CreateMessageRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.conversation_pb2.CreateMessageResponse, collections.abc.Awaitable[app.app.v1alpha.conversation_pb2.CreateMessageResponse]]:
        """Create a message"""
    @abc.abstractmethod
    def ListMessages(
        self,
        request: app.app.v1alpha.conversation_pb2.ListMessagesRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.conversation_pb2.ListMessagesResponse, collections.abc.Awaitable[app.app.v1alpha.conversation_pb2.ListMessagesResponse]]:
        """List messages"""
    @abc.abstractmethod
    def UpdateMessage(
        self,
        request: app.app.v1alpha.conversation_pb2.UpdateMessageRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.conversation_pb2.UpdateMessageResponse, collections.abc.Awaitable[app.app.v1alpha.conversation_pb2.UpdateMessageResponse]]:
        """Update a message"""
    @abc.abstractmethod
    def DeleteMessage(
        self,
        request: app.app.v1alpha.conversation_pb2.DeleteMessageRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.conversation_pb2.DeleteMessageResponse, collections.abc.Awaitable[app.app.v1alpha.conversation_pb2.DeleteMessageResponse]]:
        """Delete a message"""
    @abc.abstractmethod
    def UpdateAiAssistantAppPlayground(
        self,
        request: app.app.v1alpha.app_pb2.UpdateAiAssistantAppPlaygroundRequest,
        context: _ServicerContext,
    ) -> typing.Union[app.app.v1alpha.app_pb2.UpdateAiAssistantAppPlaygroundResponse, collections.abc.Awaitable[app.app.v1alpha.app_pb2.UpdateAiAssistantAppPlaygroundResponse]]:
        """Update ai assistant app playground"""

def add_AppPublicServiceServicer_to_server(servicer: AppPublicServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...