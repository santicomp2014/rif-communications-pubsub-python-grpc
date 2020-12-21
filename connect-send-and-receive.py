import sys

from grpc import insecure_channel

from api_pb2 import RskAddress, PublishPayload, Channel, Msg, RskAddressPublish
from api_pb2_grpc import CommunicationsApiStub
from utils import subscribe_to_topic, notification_to_message, unsubscribe_from_topic


def run(rif_comms_node_address: str, our_rsk_address: str, peer_rsk_address: str):
    with insecure_channel(rif_comms_node_address) as channel:
        print("connecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)

        our_rsk_addr = RskAddress(address=our_rsk_address)
        print("registering our rsk address", our_rsk_addr.address)
        # TODO: how can we keep this from blocking without a var assignment?
        notification = stub.ConnectToCommunicationsNode(our_rsk_addr)

        our_topic, our_topic_id = subscribe_to_topic(stub, our_rsk_address, our_rsk_address)

        input("\npress enter to say \"hello\" to peer topic for rsk address " + peer_rsk_address)

        stub.SendMessageToRskAddress(
            RskAddressPublish(
                sender=RskAddress(address=our_rsk_address),
                receiver=RskAddress(address=peer_rsk_address),
                message=Msg(payload=str.encode("hello from " + our_rsk_address))
            )
        )

        while True:
            try:
                print("\nlistening on our topic", our_topic_id)
                print("press ctrl+c to stop listening and say \"goodbye\" to peer topic " + peer_topic_id)

                for topic_message in our_topic:
                    print("\ngot message \"%s\" for topic %s from %s" % (notification_to_message(topic_message), our_topic_id, topic_message.channelNewData.sender.address))

            except KeyboardInterrupt:
                print("\nsaying \"goodbye\" to peer topic " + peer_topic_id)

                stub.SendMessageToRskAddress(
                    RskAddressPublish(
                        sender=RskAddress(address=our_rsk_address),
                        receiver=RskAddress(address=peer_rsk_address),
                        message=Msg(payload=str.encode("goodbye from " + our_rsk_address))
                    )
                )

                unsubscribe_from_topic(stub, our_rsk_address)
                unsubscribe_from_topic(stub, peer_rsk_address)

                exit()


if __name__ == "__main__":
    comms_addr_param = sys.argv[1]
    our_rsk_addr_param = sys.argv[2]
    peer_rsk_address_param = sys.argv[3]
    run(comms_addr_param, our_rsk_addr_param, peer_rsk_address_param)
