import json

from api_pb2 import RskAddress, Notification, Channel, Subscriber, RskSubscription
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


def is_subscribed_to(stub: CommunicationsApiStub, address: str) -> bool:
    print("\nchecking subscription to", address)
    return stub.IsSubscribedToRskAddress(RskAddress(address=address)).value


def unsubscribe_from_topic(stub: CommunicationsApiStub, address: str, subscriber: str):
    print("\nunsubscribing from address", address)
    stub.CloseTopicWithRskAddress(
        RskSubscription(
            topic=RskAddress(address=address), subscriber=RskAddress(address=subscriber)
        )
    )


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
