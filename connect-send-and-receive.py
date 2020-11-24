import sys

from grpc import insecure_channel

from api_pb2 import RskAddress, PublishPayload, Channel, Msg
from api_pb2_grpc import CommunicationsApiStub
from utils import subscribe_to_topic, unsubscribe_from_topic, notification_to_message


def run(rif_comms_node_address: str, our_rsk_address: str, peer_rsk_address: str):
    with insecure_channel(rif_comms_node_address) as channel:
        print("connecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)

        our_rsk_addr = RskAddress(address=our_rsk_address)
        print("registering our rsk address", our_rsk_addr.address)
        # TODO: how can we keep this from blocking without a var assignment?
        notification = stub.ConnectToCommunicationsNode(our_rsk_addr)

        _, our_topic_id = subscribe_to_topic(stub, our_rsk_address)
        print("our topic ID is", our_topic_id)

        input("press enter to say \"hello\" on our topic")

        stub.SendMessageToTopic(
            PublishPayload(
                topic=Channel(channelId=our_topic_id),
                message=Msg(payload=str.encode("hello"))
            )
        )

        peer_topic, peer_topic_id = subscribe_to_topic(stub, peer_rsk_address)

        while True:
            try:
                print("listening on topic", peer_topic_id)
                print("press ctrl+c to stop listening and say \"goodbye\" on our topic")

                for topic_message in peer_topic:
                    # TODO: deserialize response
                    print("got message %s for topic %s" % (notification_to_message(topic_message), peer_topic_id))

            except KeyboardInterrupt:
                print("saying goodbye on our topic")

                stub.SendMessageToTopic(
                    PublishPayload(
                        topic=Channel(channelId=our_topic_id),
                        message=Msg(payload=str.encode("goodbye"))
                    )
                )

                unsubscribe_from_topic(stub, our_topic_id)
                unsubscribe_from_topic(stub, peer_topic_id)

                exit()


if __name__ == "__main__":
    comms_addr_param = sys.argv[1]
    our_rsk_addr_param = sys.argv[2]
    peer_rsk_address_param = sys.argv[3]
    run(comms_addr_param, our_rsk_addr_param, peer_rsk_address_param)
