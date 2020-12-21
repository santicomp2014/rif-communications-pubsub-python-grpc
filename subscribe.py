import sys

from grpc import insecure_channel

from api_pb2 import Channel, RskAddress
from api_pb2_grpc import CommunicationsApiStub
from utils import get_peer_id, subscribe_to_topic


def run(our_comms_node_address: str, our_rsk_address: str, peer_comms_node_address: str, peer_rsk_address: str):
    with insecure_channel(our_comms_node_address) as channel:
        print("\nconnecting to comms node at", our_comms_node_address)
        stub = CommunicationsApiStub(channel)

        our_rsk_addr = RskAddress(address=our_rsk_address)
        print("registering our rsk address", our_rsk_addr.address)
        notification = stub.ConnectToCommunicationsNode(our_rsk_addr)

        # TODO: this shouldn't be necessary
        print("self-subscribing our node")
        subscribe_to_topic(stub, our_rsk_address, our_rsk_address)

    with insecure_channel(peer_comms_node_address) as channel:
        print("\nconnecting to comms node at", peer_comms_node_address)
        stub = CommunicationsApiStub(channel)

        peer_rsk_addr = RskAddress(address=peer_rsk_address)
        print("registering peer rsk address", peer_rsk_addr.address)
        notification = stub.ConnectToCommunicationsNode(peer_rsk_addr)

        # TODO: this shouldn't be necessary
        print("self-subscribing peer node")
        subscribe_to_topic(stub, peer_rsk_address, peer_rsk_address)

        # subscribing to our topic from peer node
        print("\nfetching channel ID from peer")
        peer_id = get_peer_id(stub, our_rsk_address)
        print("fetched peer id is", peer_id)
        print("subscribing to our rsk address from peer")
        stub.Subscribe(Channel(channelId=peer_id))


if __name__ == "__main__":
    our_comms_addr_param = sys.argv[1]
    our_rsk_addr_param = sys.argv[2]
    peer_comms_addr_param = sys.argv[3]
    peer_rsk_address_param = sys.argv[4]
    run(our_comms_addr_param, our_rsk_addr_param, peer_comms_addr_param, peer_rsk_address_param)
