import sys

from grpc import insecure_channel

from api_pb2 import RskAddress, Msg, PublishPayload, Channel
from api_pb2_grpc import CommunicationsApiStub


def run(rif_comms_node_address, rsk_addr_to_use):
    with insecure_channel(rif_comms_node_address) as channel:
        print("connecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)

        rsk_addr = RskAddress(address=rsk_addr_to_use)
        print("registering rsk address", rsk_addr.address)
        notification = stub.ConnectToCommunicationsNode(rsk_addr)  # what is this for? (also: ignored returned value)

        while True:
            try:
                peer_id = stub.LocatePeerId(rsk_addr).address
                print("peer ID for rsk address is", peer_id)

                print("creating topic for rsk address", rsk_addr.address)
                topic = stub.CreateTopicWithRskAddress(rsk_addr)
                topic_id = peer_id  # how to get topic id from topic var?

                print("listening on topic", topic_id)
                for response in topic:
                    print("got response %s for topic %s" % (response, topic_id))

            except KeyboardInterrupt:
                print("halting")

                stub.SendMessageToTopic(
                    PublishPayload(
                        topic=Channel(channelId=topic_id),
                        message=Msg(payload=str.encode("bye"))
                    )
                )

                print("unsubscribing from topic", topic_id)
                stub.CloseTopic(Channel(channelId=topic_id))
                exit()


if __name__ == "__main__":
    node_address = sys.argv[1]
    rsk_address = sys.argv[2]
    run(node_address, rsk_address)
