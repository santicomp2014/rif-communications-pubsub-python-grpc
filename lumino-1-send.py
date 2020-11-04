import sys

from grpc import insecure_channel
from pynput.keyboard import Key, Listener

from api_pb2 import Channel, PublishPayload, Msg
from api_pb2_grpc import CommunicationsApiStub


def run(target, channel_id_1, channel_id_2):
    with insecure_channel(target) as channel:
        stub = CommunicationsApiStub(channel)
        # time.sleep(10.0)
        # notification = stub.ConnectToCommunicationsNode(RskAddress(address=address))
        # stub.CreateTopicWithPeerId(PeerId(address=channel_id_1))
        # stub.CreateTopicWithPeerId(PeerId(address=channel_id_2))
        stub.Subscribe(Channel(channelId=channel_id_1))
        stub.Subscribe(Channel(channelId=channel_id_2))

        def on_release(key):
            if key == Key.space:
                stub.SendMessageToTopic(PublishPayload(
                    topic=Channel(channelId=channel_id_1),
                    message=Msg(payload=str.encode("HELLO"))
                ))
                print("SPACE")
            if key == Key.enter:
                stub.SendMessageToTopic(PublishPayload(
                    topic=Channel(channelId=channel_id_2),
                    message=Msg(payload=str.encode("HELLO"))
                ))
                print("ENTER")
            if key == Key.esc:
                # Stop listener
                return False

        # Collect events until released
        with Listener(on_release=on_release) as listener:
            listener.join()

        while True:
            try:
                # response = stub.Publish(PublishPayload(topic="0xtestroom2", message=str.encode("HELLO")))
                # time.sleep(10.0)
                # print("LocatePeerId")
                # response = stub.LocatePeerId(RskAddress(address=address))
                # print("response=%s" %
                # (response))

                # channel = stub.CreateTopicWithPeerId(PeerId(address=channel_id_2))
                # print("CreateTopicWithRskAddress")
                # channel = stub.CreateTopicWithRskAddress(RskAddress(address=address))

                for resp in channel:
                    print(resp)
                exit()
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(close)
                print("CloseTopic")
                # stub.CloseTopic(Channel(channelId=channel_id_2))
                exit()


def close(channel):
    channel.close()


if __name__ == "__main__":
    cli_target = sys.argv[1]
    cli_channel_id_1 = sys.argv[2]
    cli_channel_id_2 = sys.argv[3]
    run(cli_target, cli_channel_id_1, cli_channel_id_2)

# previously hard-coded values:
# {
#     "lumino-1-send" : {
#         "target": "localhost:6012",
#         "channel_id_1": "16Uiu2HAm7WTnfH5GLtFVTPMc79Qu8TzMoEKe4QEDnWiSBRjr8UZf",
#         "channel_id_2": "16Uiu2HAmJgg1YDeeNKxY2PJ11LCWx56spjfEJdhvD5HvSCjyszaX",
#     },
#     "lumino-2-send" :{
#         "target": "localhost:6013",
#         "channel_id_1": "16Uiu2HAmJgg1YDeeNKxY2PJ11LCWx56spjfEJdhvD5HvSCjyszaX",
#         "channel_id_2": "16Uiu2HAm7WTnfH5GLtFVTPMc79Qu8TzMoEKe4QEDnWiSBRjr8UZf",
#     }
# }
