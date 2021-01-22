import sys

from grpc import insecure_channel, RpcError

from api_pb2 import RskAddress, Msg, RskAddressPublish, RskSubscription
from api_pb2_grpc import CommunicationsApiStub
from utils import unsubscribe_from_topic, get_peer_id


def run(rif_comms_node_address, our_addr, topic_addr):
    with insecure_channel(rif_comms_node_address) as channel:
        print("connecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)

        rsk_addr = RskAddress(address=topic_addr)
        our_rsk_addr = RskAddress(address=our_addr)
        print("registering rsk address", rsk_addr.address)
        stub.ConnectToCommunicationsNode(rsk_addr)
        topic_id = ""
        print("creating topic for rsk address", rsk_addr.address, ". Subscriber is:", our_rsk_addr.address)
        topic = stub.CreateTopicWithRskAddress(RskSubscription(topic=rsk_addr, subscriber=our_rsk_addr))
        try:
            for response in topic:
                if (response.channelPeerJoined.peerId):
                    topic_id = response.channelPeerJoined.peerId
                    print("peer ID for rsk address is", topic_id)
                    break
        except RpcError as e:
            print("Error Subscribing", str(e.details()))
            exit()

        while True:
            try:
                print("listening on topic", topic_id)
                for response in topic:
                    print("got response %s for topic %s" % (response, topic_id))

            except KeyboardInterrupt:
                print("halting")

                stub.SendMessageToRskAddress(
                    RskAddressPublish(
                        sender=RskAddress(address=topic_addr),
                        receiver=RskAddress(address=topic_addr),
                        message=Msg(payload=str.encode("bye"))
                    )
                )

                print("closing topic", topic_id)
                unsubscribe_from_topic(stub, topic_addr, our_addr)
                exit()


if __name__ == "__main__":
    node_address = sys.argv[1]
    our_addr = sys.argv[2]
    topic_addr = sys.argv[3]
    run(node_address, our_addr, topic_addr)
