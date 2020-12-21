import sys

from grpc import insecure_channel

from api_pb2 import RskAddress
from api_pb2_grpc import CommunicationsApiStub
from utils import subscribe_to_topic, let_user_pick, is_subscribed_to

addresses = [
    "0x8cb891510dF75C223C53f910A98c3b61B9083c3B",
    "0xeBfF0EEe8E2b6952E589B0475e3F0E34dA0655B1",
    "0xbE165fe06c03e4387F79615b7A0b79d535e8D325",
]


def run(rif_comms_node_address: str, our_rsk_address: str):
    with insecure_channel(rif_comms_node_address) as channel:
        print("\nconnecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)

        our_rsk_addr = RskAddress(address=our_rsk_address)
        print("registering rsk address", our_rsk_addr.address)
        notification = stub.ConnectToCommunicationsNode(our_rsk_addr)

        # subscribe to topics
        while True:
            try:
                sub_option = let_user_pick(
                    "\npick a REGISTERED address to subscribe to. press ctrl-c when done.", addresses
                ) - 1
                subscribe_to_topic(stub, our_rsk_addr.address,  addresses[sub_option])
            except KeyboardInterrupt:
                print("\n")
                break

        # check subscriptions to topic
        while True:
            try:
                sub_check_option = let_user_pick(
                    "\npick a REGISTERED address to check subscription to. press ctrl-c when done.", addresses
                ) - 1
                print(
                    "\nis\n    ", our_rsk_address, "\nsubscribed to\n    ", addresses[sub_check_option],
                    "\n?", "\n→ " + str(is_subscribed_to(stub, addresses[sub_check_option]))
                )
            except KeyboardInterrupt:
                exit()


if __name__ == "__main__":
    comms_addr_param = sys.argv[1]
    address_option = let_user_pick("pick an address to connect with:", addresses) - 1

    run(comms_addr_param, addresses[address_option])
