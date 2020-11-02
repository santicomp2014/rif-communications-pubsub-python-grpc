import grpc

import api_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:6012") as channel:
        stub = api_pb2_grpc.CommunicationsApiStub(channel)
        while True:
            try:
                print("SendMessageToTopic")
                response = stub.SendMessageToTopic(api_pb2_grpc.api__pb2.PublishPayload(
                    topic=api_pb2_grpc.api__pb2.Channel(
                        channelId="16Uiu2HAmJgg1YDeeNKxY2PJ11LCWx56spjfEJdhvD5HvSCjyszaX"
                    ),
                    message=api_pb2_grpc.api__pb2.Msg(payload=str.encode("HELLO")))
                )
                print("response=%s" % response)

                exit()
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                print("CloseTopic")
                channel.unsubscribe(close)
                exit()


def close(channel):
    channel.close()


if __name__ == "__main__":
    run()
