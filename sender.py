import sys

from grpc import insecure_channel
from pynput.keyboard import Key, Listener

from api_pb2 import RskAddress, Channel, RskAddressPublish, Msg
from api_pb2_grpc import CommunicationsApiStub

from utils import unsubscribe_from_topic

def run(rif_comms_node_address, sender_rsk_address, receiver_rsk_address):
    with insecure_channel(rif_comms_node_address) as channel:
        print("connecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)

        print("press space to send messages and esc to stop")

        def on_release(key):
            if key == Key.space:
                stub.SendMessageToRskAddress(
                    RskAddressPublish(
                        sender=RskAddress(address=sender_rsk_address),
                        receiver=RskAddress(address=receiver_rsk_address),
                        message=Msg(payload=str.encode("hey"))
                    )
                )
            if key == Key.esc:
                return False  # stop message sending loop

        # enter message sending loop
        with Listener(on_release=on_release) as listener:
            listener.join()

        print("done sending messages")

        # enter message receiving loop



if __name__ == "__main__":
    node_address = sys.argv[1]
    sender_rsk_address = sys.argv[2]
    receiver_rsk_address = sys.argv[3]
    run(node_address, sender_rsk_address, receiver_rsk_address)
