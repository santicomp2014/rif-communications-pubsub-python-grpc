import sys

from grpc import insecure_channel
from pynput.keyboard import Key, Listener

from api_pb2 import Channel, PublishPayload, Msg, RskAddress
from api_pb2_grpc import CommunicationsApiStub


def run(rif_comms_address, rsk_addr_to_use):
    with insecure_channel(rif_comms_address) as channel:
        print("connecting to comms node at", rif_comms_address)
        stub = CommunicationsApiStub(channel)

        rsk_addr = RskAddress(address=rsk_addr_to_use)
        print("rsk address for destination is", rsk_addr.address)

        peer_id = stub.LocatePeerId(rsk_addr).address
        print("peer ID for destination is", peer_id)

        print("press space to send a message or escape to exit")

        def on_release(key):
            if key == Key.space:
                stub.SendMessageToTopic(
                    PublishPayload(
                        topic=Channel(channelId=peer_id),
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
    rsk_address = sys.argv[2]
    run(node_address, rsk_address)
