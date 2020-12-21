import sys

from grpc import insecure_channel

from api_pb2 import RskAddress, Msg, Channel, RskAddressPublish, RskSubscription
from api_pb2_grpc import CommunicationsApiStub
from utils import notification_to_message


def run(rif_comms_node_address, our_rsk_address):
    with insecure_channel(rif_comms_node_address) as channel:
        print("connecting to comms node at", rif_comms_node_address)
        stub = CommunicationsApiStub(channel)

        our_rsk_addr = RskAddress(address=our_rsk_address)
        print("registering our rsk address", our_rsk_addr.address)
        notification = stub.ConnectToCommunicationsNode(our_rsk_addr)

        print("creating topic for our address", our_rsk_addr.address)
        our_topic = stub.CreateTopicWithRskAddress(RskSubscription(subscriber=our_rsk_addr, topic=our_rsk_addr))

        i = 1
        for response in our_topic:
            print("received message:", notification_to_message(response))

            if (response.subscribeError.reason):
                print("Error Subscribing",response.subscribeError.reason)
                exit()    
            input("press enter to say \"ping\" on our own topic, or ctrl+c to exit")
            stub.SendMessageToRskAddress(
                RskAddressPublish(
                    sender=RskAddress(address=our_rsk_address),
                    receiver=RskAddress(address=our_rsk_address),
                    message=Msg(payload=str.encode("ping (" + str(i) + ")"))
                )
            )
            i += 1


if __name__ == "__main__":
    node_address = sys.argv[1]
    our_rsk_address = sys.argv[2]
    run(node_address, our_rsk_address)
