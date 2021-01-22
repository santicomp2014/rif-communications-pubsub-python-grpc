import sys

from grpc import insecure_channel

from api_pb2_grpc import CommunicationsApiStub
from utils import get_peer_id


def run(rif_comms_node_address: str, our_rsk_address: str):
    with insecure_channel(rif_comms_node_address) as channel:
        stub = CommunicationsApiStub(channel)
        print("our rsk address", our_rsk_address)
        print("Peer id:", get_peer_id(stub, our_rsk_address))


if __name__ == "__main__":
    comms_addr_param = sys.argv[1]
    rsk_address = sys.argv[2]

    run(comms_addr_param, rsk_address)
