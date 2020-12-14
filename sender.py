import sys

from grpc import insecure_channel
from pynput.keyboard import Key, Listener

from api_pb2 import RskAddress, Channel, RskAddressPublish, Msg
from api_pb2_grpc import CommunicationsApiStub

from utils import unsubscribe_from_topic

def run(rif_comms_node_address, rsk_address):
    with insecure_channel(rif_comms_node_address) as channel:
        print("connecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)
        rsk_addr = RskAddress(address=rsk_address)

        topic_id = ""
        print("subscribing to topic", topic_id)
        topic = stub.CreateTopicWithRskAddress(rsk_addr)
        for response in topic:
            if (response.channelPeerJoined.peerId):
                topic_id = response.channelPeerJoined.peerId
                print("peer ID for rsk address is", topic_id)
                break
            if (response.subscribeError.reason):
                print("Error Subscribing",response.subscribeError.reason)
                exit()
            

        print("press space to send messages and esc to stop")

        def on_release(key):
            if key == Key.space:
                stub.SendMessageToRskAddress(
                    RskAddressPublish(
                        receiver=RskAddress(address=rsk_address),
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
                print("listening on topic", topic_id)
                for response in topic:
                    print("got response %s for topic %s" % (response, topic_id))

            except KeyboardInterrupt:
                print("halting")

                print("closing topic", topic_id)
                unsubscribe_from_topic(stub, rsk_address)
                exit()


if __name__ == "__main__":
    node_address = sys.argv[1]
    rsk_address = sys.argv[2]
    run(node_address, rsk_address)
