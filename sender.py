import sys

from grpc import insecure_channel
from pynput.keyboard import Key, Listener

from api_pb2 import RskAddress, Channel, PublishPayload, Msg
from api_pb2_grpc import CommunicationsApiStub
import time


def run(rif_comms_node_address, rsk_address):
    with insecure_channel(rif_comms_node_address) as channel:
        print("connecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)
        rsk_addr = RskAddress(address=rsk_address)
        topic_id = stub.LocatePeerId(rsk_addr).address
        print(topic_id)

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
                return False  # stop message sending loop

        # enter message sending loop
        with Listener(on_release=on_release) as listener:
            listener.join()

        print("done sending messages, now listening for messages")

        # enter message receiving loop
        while True:
            try:
                print("creating topic with id", topic_id)
                topic = stub.CreateTopicWithPeerId(topic_id)

                print("listening on topic", topic_id)
                for response in topic:
                    print("got response %s for topic %s" % (response, topic_id))

            except KeyboardInterrupt:
                print("halting")

                print("closing topic", topic_id)
                stub.CloseTopic(Channel(channelId=topic_id))
                exit()


if __name__ == "__main__":
    node_address = sys.argv[1]
    rsk_address = sys.argv[2]  # this should be an rsk address, not a topic id, but LocatePeerID() fails
    run(node_address, rsk_address)
