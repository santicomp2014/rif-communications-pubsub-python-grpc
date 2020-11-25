import sys

from grpc import insecure_channel

from api_pb2 import RskAddress, Msg, PublishPayload, Channel
from api_pb2_grpc import CommunicationsApiStub


def run(rif_comms_node_address, our_rsk_address, peer_rsk_address):
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
                our_topic_id = response.channelPeerJoined.peerId
                print("our topic ID is", our_topic_id)
                break
        

        input("press enter to say hi on our topic")

        stub.SendMessageToTopic(
            PublishPayload(
                topic=Channel(channelId=our_topic_id),
                message=Msg(payload=str.encode("hi"))
            )
        )

        peer_rsk_addr = RskAddress(address=peer_rsk_address)
        print("subscribing to peer rsk address", peer_rsk_addr.address)
        
        peer_topic_id = ""
        print("creating topic for peer address", peer_rsk_addr.address)
        peer_topic = stub.CreateTopicWithRskAddress(peer_rsk_addr)
        for response in peer_topic:
            if (response.channelPeerJoined.peerId):
                peer_topic_id = response.channelPeerJoined.peerId
                print("peer topic ID is", peer_topic_id)
                break

        while True:
            try:
                print("listening on topic", peer_topic_id)
                for response in peer_topic:
                    print("got response %s for topic %s" % (response, peer_topic_id))

            except KeyboardInterrupt:
                print("saying goodby on our topic")

                stub.SendMessageToTopic(
                    PublishPayload(
                        topic=Channel(channelId=our_topic_id),
                        message=Msg(payload=str.encode("bye"))
                    )
                )

                print("closing our topic", our_topic_id)
                stub.CloseTopic(Channel(channelId=our_topic_id))

                print("closing peer topic", peer_topic_id)
                stub.CloseTopic(Channel(channelId=peer_topic_id))

                exit()


if __name__ == "__main__":
    node_address = sys.argv[1]
    our_rsk_address = sys.argv[2]
    peer_rsk_address = sys.argv[3]
    run(node_address, our_rsk_address, peer_rsk_address)
