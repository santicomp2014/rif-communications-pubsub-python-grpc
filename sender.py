import sys

from grpc import insecure_channel
from pynput.keyboard import Key, Listener

from api_pb2 import Channel, PublishPayload, Msg
from api_pb2_grpc import CommunicationsApiStub


def run(rif_comms_node_address, topic_id):
    with insecure_channel(rif_comms_node_address) as channel:
        print("connecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)

        print("subscribing to topic", topic_id)
        stub.Subscribe(Channel(channelId=topic_id))  # this crashes if already subscribed

        print("press space to send messages and esc to stop")

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

        # enter sending messages loop
        with Listener(on_release=on_release) as listener:
            listener.join()

        print("done sending messages, now listening for messages")

        while True:
            try:
                print("creating topic with id", topic_id)
                topic = stub.CreateTopicWithPeerId(topic_id)  # this is failing, so did CreateTopicWithRskAddress()

                print("listening on topic", topic_id)
                for response in topic:
                    print("got response %s for topic %s" % (response, topic_id))

            except KeyboardInterrupt:
                print("halting")

                print("unsubscribing from topic", topic_id)
                stub.CloseTopic(Channel(channelId=topic_id))
                exit()


if __name__ == "__main__":
    node_address = sys.argv[1]
    topic_id = sys.argv[2]  # this should be an rsk address, not a topic id, but LocatePeerID() fails
    run(node_address, topic_id)
