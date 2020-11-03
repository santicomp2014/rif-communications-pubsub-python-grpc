import sys

import grpc

from api_pb2 import RskAddress, Msg, PublishPayload, Channel
from api_pb2_grpc import CommunicationsApiStub


def run(target, address, channel_id):
    with grpc.insecure_channel(target) as channel:
        stub = CommunicationsApiStub(channel)
        rsk_address = RskAddress(address=address)
        # time.sleep(10.0)
        notification = stub.ConnectToCommunicationsNode(rsk_address)

        while True:
            try:
                # response = stub.Publish(PublishPayload(topic="0xtestroom2", message=str.encode("HELLO")))
                # time.sleep(10.0)
                print("LocatePeerId")
                response = stub.LocatePeerId(rsk_address)
                print("response=%s" % response)

                # channel = stub.CreateTopicWithPeerId(PeerId(address=channel_id))
                print("CreateTopicWithRskAddress")
                channel = stub.CreateTopicWithRskAddress(rsk_address)
                for resp in channel:
                    print(resp)
                exit()
            except KeyboardInterrupt:
                stub.SendMessageToTopic(PublishPayload(topic=Channel(
                    channelId=channel_id,
                    message=Msg(payload=str.encode("HELLO")))
                ))

                print("KeyboardInterrupt")
                channel.unsubscribe(close)
                print("CloseTopic")
                # stub.CloseTopic(Channel(channelId=channel_id))
                exit()


def close(channel):
    channel.close()


if __name__ == "__main__":
    cli_target = sys.argv[1]
    cli_address = sys.argv[2]
    cli_channel_id = sys.argv[3]
    run(cli_target, cli_address, cli_channel_id)

# previously hard-coded values:
# {
#     "lumino-1" : {
#         "target": "localhost:6012",
#         "address": "0x2aCc95758f8b5F583470bA265Eb685a8f45fC9D5",
#         "channel-id": "16Uiu2HAm7WTnfH5GLtFVTPMc79Qu8TzMoEKe4QEDnWiSBRjr8UZf",
#     },
#     "lumino-2" :{
#         "target": "localhost:6013",
#         "address": "0x3aCc95758f8b5F583470bA265Eb685a8f45fC9D5",
#         "channel-id": "16Uiu2HAmJgg1YDeeNKxY2PJ11LCWx56spjfEJdhvD5HvSCjyszaX",
#     }
# }
