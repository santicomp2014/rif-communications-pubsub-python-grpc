import os
import api_pb2_grpc
import time
import grpc

def run():
    with grpc.insecure_channel("localhost:6012") as channel:
        stub = api_pb2_grpc.CommunicationsApiStub(channel)
        while True:
            try:
                notification = stub.ConnectToCommunicationsNode(api_pb2_grpc.api__pb2.RskAddress(address="0x2aCc95758f8b5F583470bA265Eb685a8f45fC9D5"))
                print("notification=%s" % 
                (notification))
                #subscription = stub.Subscribe(api_pb2_grpc.api__pb2.Channel(channelId="0xtestroom"))
                #print("subscription=%s" % 
                #(subscription))

                stub.Publish(api_pb2_grpc.api__pb2.PublishPayload(topic="16Uiu2HAmJgg1YDeeNKxY2PJ11LCWx56spjfEJdhvD5HvSCjyszaX", message=str.encode("HELLO")))
                print("response=%s" % 
                (response))

                #print("subscription=%s" % 
                #(subscription))
                for resp in notification:
                    print(resp)
                #exit()
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                stub.EndCommunication(api_pb2_grpc.api__pb2.NoParams())
                channel.unsubscribe(close)
                exit()

def close(channel):
    channel.close()

if __name__ == "__main__":
    run()