import sys, time

from grpc import insecure_channel

from api_pb2 import RskAddress, Msg, PublishPayload, Channel
from api_pb2_grpc import CommunicationsApiStub


def run(rif_comms_node_address, our_rsk_address):
    with insecure_channel(rif_comms_node_address) as channel:
        print("connecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)

        our_rsk_addr = RskAddress(address=our_rsk_address)
        print("registering our rsk address", our_rsk_addr.address)
        notification = stub.ConnectToCommunicationsNode(our_rsk_addr)

        our_topic_id = ""

        print("creating topic for our address", our_rsk_addr.address)
        our_topic = stub.CreateTopicWithRskAddress(our_rsk_addr)
        for response in our_topic:
            if (response.channelPeerJoined.peerId):
                print("Received message")
                print(response)
                our_topic_id = response.channelPeerJoined.peerId
                break

        stub.SendMessageToTopic(
            PublishPayload(
                topic=Channel(channelId=our_topic_id),
                message=Msg(payload=str.encode("hi"))
            )
        )        

if __name__ == "__main__":
    node_address = sys.argv[1]
    our_rsk_address = sys.argv[2]
    run(node_address, our_rsk_address)