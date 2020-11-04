import sys

from grpc import insecure_channel
from pynput.keyboard import Key, Listener

from api_pb2 import Channel, PublishPayload, Msg, RskAddress
from api_pb2_grpc import CommunicationsApiStub


def run(rif_comms_address, topic_id):
    with insecure_channel(rif_comms_address) as channel:
        print("connecting to comms node at", rif_comms_address)
        stub = CommunicationsApiStub(channel)

        print("topic id for destination is", topic_id)
        stub.Subscribe(Channel(channelId=topic_id))  # this crashes if already subscribed

        print("press space to send a message or escape to exit")

        def on_release(key):
            if key == Key.space:
                stub.SendMessageToTopic(
                    PublishPayload(
                        topic=Channel(channelId=topic_id),
                        message=Msg(payload=str.encode("hey"))
                    )
                )
            if key == Key.esc:
                return False  # stop listener

        # collect events until released
        with Listener(on_release=on_release) as listener:
            listener.join()


if __name__ == "__main__":
    node_address = sys.argv[1]
    topic_id = sys.argv[2]  # this should be an rsk address, not a topic id (LocatePeerID crashes)
    run(node_address, topic_id)
