import json

from api_pb2 import RskAddress, Notification, Channel
from api_pb2_grpc import CommunicationsApiStub


def subscribe_to_topic(stub: CommunicationsApiStub, rsk_address: str) -> (Notification, str):
    rsk_addr = RskAddress(address=rsk_address)

    print("subscribing to topic for rsk address", rsk_addr.address)
    topic = stub.CreateTopicWithRskAddress(rsk_addr)
    topic_id = ""

    for response in topic:
            if (response.channelPeerJoined.peerId):
                topic_id = response.channelPeerJoined.peerId
                print("our topic ID is", topic_id)
                break

    print("topic id for rsk address", rsk_addr.address, "is", topic_id)

    return topic, topic_id


def unsubscribe_from_topic(stub: CommunicationsApiStub, topic_id: str):
    print("unsubscribing from topic", topic_id)

    stub.CloseTopic(Channel(channelId=topic_id))


def notification_to_message(notification: Notification) -> str:
    try:
        content_text = notification.channelNewData.data
        if content_text:
            content = json.loads(content_text.decode())
            return bytes(content["data"]).decode()
    except AttributeError:
        pass
    return None
