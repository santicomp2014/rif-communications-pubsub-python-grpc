import json

from api_pb2 import RskAddress, Notification, Channel, Subscriber
from api_pb2_grpc import CommunicationsApiStub


def subscribe_to_topic(stub: CommunicationsApiStub, rsk_address: str) -> (Notification, str):
    rsk_addr = RskAddress(address=rsk_address)

    print("\nsubscribing to topic for rsk address", rsk_address)
    topic = stub.CreateTopicWithRskAddress(rsk_addr)

    topic_id = ""
    for response in topic:
        if response.channelPeerJoined.peerId:
            topic_id = response.channelPeerJoined.peerId
            break
        if (response.subscribeError.reason):
                raise Exception(("Error Subscribing",response.subscribeError.reason))

    print("topic id for rsk address", rsk_address, "is:\n" + topic_id)

    return topic, topic_id


def is_subscribed_to(stub: CommunicationsApiStub, subscriber_address: str, topic_address: str) -> bool:
    print("\nchecking subscription for", subscriber_address, "to topic", topic_address)

    our_peer_id = get_peer_id(stub, subscriber_address)
    topic_id = get_peer_id(stub, topic_address)
    return stub.HasSubscriber(
        Subscriber(
            peerId=our_peer_id,
            channel=Channel(channelId=topic_id)
        )
    ).value


def unsubscribe_from_topic(stub: CommunicationsApiStub, topic_id: str):
    print("\nunsubscribing from topic", topic_id)
    stub.CloseTopic(Channel(channelId=topic_id))


def get_peer_id(stub: CommunicationsApiStub, rsk_address: str) -> str:
    return stub.LocatePeerId(RskAddress(address=rsk_address)).address


def notification_to_message(notification: Notification) -> str:
    try:
        content_text = notification.channelNewData.data
        if content_text:
            content = json.loads(content_text.decode())
            return bytes(content["data"]).decode()
    except AttributeError:
        pass
    return None


def let_user_pick(prompt: str, options: []) -> int:
    while True:
        print(prompt)
        for idx, element in enumerate(options):
            print("{}) {}".format(idx + 1, element))
        i = input("enter number: ")
        if 0 < int(i) <= len(options):
            return int(i)
        else:
            print("invalid selection, try again.")
