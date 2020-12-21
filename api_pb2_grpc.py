# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import api_pb2 as api__pb2


class CommunicationsApiStub(object):
    """Server side stream, there's no need for a bidirectional stream, it's only needed so
    The client can be notified of events in their subscriptions
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConnectToCommunicationsNode = channel.unary_stream(
                '/communicationsapi.CommunicationsApi/ConnectToCommunicationsNode',
                request_serializer=api__pb2.RskAddress.SerializeToString,
                response_deserializer=api__pb2.Notification.FromString,
                )
        self.EndCommunication = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/EndCommunication',
                request_serializer=api__pb2.Void.SerializeToString,
                response_deserializer=api__pb2.Void.FromString,
                )
        self.Publish = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/Publish',
                request_serializer=api__pb2.PublishPayload.SerializeToString,
                response_deserializer=api__pb2.Void.FromString,
                )
        self.Subscribe = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/Subscribe',
                request_serializer=api__pb2.Channel.SerializeToString,
                response_deserializer=api__pb2.Void.FromString,
                )
        self.Unsubscribe = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/Unsubscribe',
                request_serializer=api__pb2.Channel.SerializeToString,
                response_deserializer=api__pb2.Void.FromString,
                )
        self.GetSubscribers = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/GetSubscribers',
                request_serializer=api__pb2.Channel.SerializeToString,
                response_deserializer=api__pb2.Subscribers.FromString,
                )
        self.HasSubscriber = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/HasSubscriber',
                request_serializer=api__pb2.Subscriber.SerializeToString,
                response_deserializer=api__pb2.BooleanResponse.FromString,
                )
        self.IsSubscribedToRskAddress = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/IsSubscribedToRskAddress',
                request_serializer=api__pb2.RskAddress.SerializeToString,
                response_deserializer=api__pb2.BooleanResponse.FromString,
                )
        self.SendMessage = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/SendMessage',
                request_serializer=api__pb2.Msg.SerializeToString,
                response_deserializer=api__pb2.Void.FromString,
                )
        self.LocatePeerId = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/LocatePeerId',
                request_serializer=api__pb2.RskAddress.SerializeToString,
                response_deserializer=api__pb2.PeerId.FromString,
                )
        self.CreateTopicWithPeerId = channel.unary_stream(
                '/communicationsapi.CommunicationsApi/CreateTopicWithPeerId',
                request_serializer=api__pb2.PeerId.SerializeToString,
                response_deserializer=api__pb2.Notification.FromString,
                )
        self.CreateTopicWithRskAddress = channel.unary_stream(
                '/communicationsapi.CommunicationsApi/CreateTopicWithRskAddress',
                request_serializer=api__pb2.RskSubscription.SerializeToString,
                response_deserializer=api__pb2.Notification.FromString,
                )
        self.CloseTopicWithRskAddress = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/CloseTopicWithRskAddress',
                request_serializer=api__pb2.RskSubscription.SerializeToString,
                response_deserializer=api__pb2.Void.FromString,
                )
        self.SendMessageToTopic = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/SendMessageToTopic',
                request_serializer=api__pb2.PublishPayload.SerializeToString,
                response_deserializer=api__pb2.Void.FromString,
                )
        self.SendMessageToRskAddress = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/SendMessageToRskAddress',
                request_serializer=api__pb2.RskAddressPublish.SerializeToString,
                response_deserializer=api__pb2.Void.FromString,
                )
        self.UpdateAddress = channel.unary_unary(
                '/communicationsapi.CommunicationsApi/UpdateAddress',
                request_serializer=api__pb2.RskAddress.SerializeToString,
                response_deserializer=api__pb2.Void.FromString,
                )


class CommunicationsApiServicer(object):
    """Server side stream, there's no need for a bidirectional stream, it's only needed so
    The client can be notified of events in their subscriptions
    """

    def ConnectToCommunicationsNode(self, request, context):
        """Open a data stream with the server, it can only receive messages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EndCommunication(self, request, context):
        """Close the data stream
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Publish(self, request, context):
        """Publish a message in a channel
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Subscribe to a channel
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unsubscribe(self, request, context):
        """Unsubscribe to a channel
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSubscribers(self, request, context):
        """Get the subscribers of a participating channel
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HasSubscriber(self, request, context):
        """Query if a subscriber exists in a participating channel
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsSubscribedToRskAddress(self, request, context):
        """Query if a subscriber exists in a participating channel
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessage(self, request, context):
        """Send a direct message to a peer
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LocatePeerId(self, request, context):
        """///LUMINO SPECIFIC COMMANDS

        Obtains peerId from RSKAddress
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTopicWithPeerId(self, request, context):
        """Creates topic for specific peerID/Rsk Address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTopicWithRskAddress(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseTopicWithRskAddress(self, request, context):
        """Close Topic for a specific topicID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessageToTopic(self, request, context):
        """Send Message to Specified Topic
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessageToRskAddress(self, request, context):
        """Send message to topic binded to an specific RSK address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAddress(self, request, context):
        """Update RSK Address after invitation
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommunicationsApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConnectToCommunicationsNode': grpc.unary_stream_rpc_method_handler(
                    servicer.ConnectToCommunicationsNode,
                    request_deserializer=api__pb2.RskAddress.FromString,
                    response_serializer=api__pb2.Notification.SerializeToString,
            ),
            'EndCommunication': grpc.unary_unary_rpc_method_handler(
                    servicer.EndCommunication,
                    request_deserializer=api__pb2.Void.FromString,
                    response_serializer=api__pb2.Void.SerializeToString,
            ),
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=api__pb2.PublishPayload.FromString,
                    response_serializer=api__pb2.Void.SerializeToString,
            ),
            'Subscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=api__pb2.Channel.FromString,
                    response_serializer=api__pb2.Void.SerializeToString,
            ),
            'Unsubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Unsubscribe,
                    request_deserializer=api__pb2.Channel.FromString,
                    response_serializer=api__pb2.Void.SerializeToString,
            ),
            'GetSubscribers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSubscribers,
                    request_deserializer=api__pb2.Channel.FromString,
                    response_serializer=api__pb2.Subscribers.SerializeToString,
            ),
            'HasSubscriber': grpc.unary_unary_rpc_method_handler(
                    servicer.HasSubscriber,
                    request_deserializer=api__pb2.Subscriber.FromString,
                    response_serializer=api__pb2.BooleanResponse.SerializeToString,
            ),
            'IsSubscribedToRskAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.IsSubscribedToRskAddress,
                    request_deserializer=api__pb2.RskAddress.FromString,
                    response_serializer=api__pb2.BooleanResponse.SerializeToString,
            ),
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=api__pb2.Msg.FromString,
                    response_serializer=api__pb2.Void.SerializeToString,
            ),
            'LocatePeerId': grpc.unary_unary_rpc_method_handler(
                    servicer.LocatePeerId,
                    request_deserializer=api__pb2.RskAddress.FromString,
                    response_serializer=api__pb2.PeerId.SerializeToString,
            ),
            'CreateTopicWithPeerId': grpc.unary_stream_rpc_method_handler(
                    servicer.CreateTopicWithPeerId,
                    request_deserializer=api__pb2.PeerId.FromString,
                    response_serializer=api__pb2.Notification.SerializeToString,
            ),
            'CreateTopicWithRskAddress': grpc.unary_stream_rpc_method_handler(
                    servicer.CreateTopicWithRskAddress,
                    request_deserializer=api__pb2.RskSubscription.FromString,
                    response_serializer=api__pb2.Notification.SerializeToString,
            ),
            'CloseTopicWithRskAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseTopicWithRskAddress,
                    request_deserializer=api__pb2.RskSubscription.FromString,
                    response_serializer=api__pb2.Void.SerializeToString,
            ),
            'SendMessageToTopic': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageToTopic,
                    request_deserializer=api__pb2.PublishPayload.FromString,
                    response_serializer=api__pb2.Void.SerializeToString,
            ),
            'SendMessageToRskAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageToRskAddress,
                    request_deserializer=api__pb2.RskAddressPublish.FromString,
                    response_serializer=api__pb2.Void.SerializeToString,
            ),
            'UpdateAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAddress,
                    request_deserializer=api__pb2.RskAddress.FromString,
                    response_serializer=api__pb2.Void.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'communicationsapi.CommunicationsApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommunicationsApi(object):
    """Server side stream, there's no need for a bidirectional stream, it's only needed so
    The client can be notified of events in their subscriptions
    """

    @staticmethod
    def ConnectToCommunicationsNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/communicationsapi.CommunicationsApi/ConnectToCommunicationsNode',
            api__pb2.RskAddress.SerializeToString,
            api__pb2.Notification.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EndCommunication(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/EndCommunication',
            api__pb2.Void.SerializeToString,
            api__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/Publish',
            api__pb2.PublishPayload.SerializeToString,
            api__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/Subscribe',
            api__pb2.Channel.SerializeToString,
            api__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unsubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/Unsubscribe',
            api__pb2.Channel.SerializeToString,
            api__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSubscribers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/GetSubscribers',
            api__pb2.Channel.SerializeToString,
            api__pb2.Subscribers.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HasSubscriber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/HasSubscriber',
            api__pb2.Subscriber.SerializeToString,
            api__pb2.BooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsSubscribedToRskAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/IsSubscribedToRskAddress',
            api__pb2.RskAddress.SerializeToString,
            api__pb2.BooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/SendMessage',
            api__pb2.Msg.SerializeToString,
            api__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LocatePeerId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/LocatePeerId',
            api__pb2.RskAddress.SerializeToString,
            api__pb2.PeerId.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTopicWithPeerId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/communicationsapi.CommunicationsApi/CreateTopicWithPeerId',
            api__pb2.PeerId.SerializeToString,
            api__pb2.Notification.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTopicWithRskAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/communicationsapi.CommunicationsApi/CreateTopicWithRskAddress',
            api__pb2.RskSubscription.SerializeToString,
            api__pb2.Notification.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseTopicWithRskAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/CloseTopicWithRskAddress',
            api__pb2.RskSubscription.SerializeToString,
            api__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessageToTopic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/SendMessageToTopic',
            api__pb2.PublishPayload.SerializeToString,
            api__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessageToRskAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/SendMessageToRskAddress',
            api__pb2.RskAddressPublish.SerializeToString,
            api__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/communicationsapi.CommunicationsApi/UpdateAddress',
            api__pb2.RskAddress.SerializeToString,
            api__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
