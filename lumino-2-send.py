import grpc
from pynput.keyboard import Key, Listener

import api_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:6013") as channel:
        stub = api_pb2_grpc.CommunicationsApiStub(channel)
        # time.sleep(10.0)
        # notification = stub.ConnectToCommunicationsNode(api_pb2_grpc.api__pb2.RskAddress(address="0x2aCc95758f8b5F583470bA265Eb685a8f45fC9D5"))
        stub.Subscribe(api_pb2_grpc.api__pb2.Channel(channelId="16Uiu2HAm7WTnfH5GLtFVTPMc79Qu8TzMoEKe4QEDnWiSBRjr8UZf"))
        stub.Subscribe(api_pb2_grpc.api__pb2.Channel(channelId="16Uiu2HAmJgg1YDeeNKxY2PJ11LCWx56spjfEJdhvD5HvSCjyszaX"))

        def on_release(key):
            if key == Key.space:
                stub.SendMessageToTopic(api_pb2_grpc.api__pb2.PublishPayload(topic=api_pb2_grpc.api__pb2.Channel(
                    channelId="16Uiu2HAmJgg1YDeeNKxY2PJ11LCWx56spjfEJdhvD5HvSCjyszaX"),
                    message=api_pb2_grpc.api__pb2.Msg(payload=str.encode("HELLO")))
                )
                print("SPACE")
            if key == Key.enter:
                stub.SendMessageToTopic(api_pb2_grpc.api__pb2.PublishPayload(topic=api_pb2_grpc.api__pb2.Channel(
                    channelId="16Uiu2HAm7WTnfH5GLtFVTPMc79Qu8TzMoEKe4QEDnWiSBRjr8UZf"),
                    message=api_pb2_grpc.api__pb2.Msg(payload=str.encode("HELLO")))
                )
                print("ENTER")
            if key == Key.esc:
                # Stop listener
                return False

        # Collect events until released
        with Listener(
                on_release=on_release) as listener:
            listener.join()

        while True:
            try:
                # response = stub.Publish(api_pb2_grpc.api__pb2.PublishPayload(topic="0xtestroom2", message=str.encode("HELLO")))
                # time.sleep(10.0)
                # print("LocatePeerId")
                # response = stub.LocatePeerId(api_pb2_grpc.api__pb2.RskAddress(address="0x2aCc95758f8b5F583470bA265Eb685a8f45fC9D5"))
                # print("response=%s" %
                # (response))

                # channel = stub.CreateTopicWithPeerId(api_pb2_grpc.api__pb2.PeerId(address="16Uiu2HAmJgg1YDeeNKxY2PJ11LCWx56spjfEJdhvD5HvSCjyszaX"))
                # print("CreateTopicWithRskAddress")
                # channel = stub.CreateTopicWithRskAddress(api_pb2_grpc.api__pb2.RskAddress(address="0x2aCc95758f8b5F583470bA265Eb685a8f45fC9D5"))
                for resp in channel:
                    print(resp)
                exit()
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(close)
                print("CloseTopic")
                # stub.CloseTopic(api_pb2_grpc.api__pb2.Channel(channelId="16Uiu2HAmJgg1YDeeNKxY2PJ11LCWx56spjfEJdhvD5HvSCjyszaX"))
                exit()


def close(channel):
    channel.close()


if __name__ == "__main__":
    run()
