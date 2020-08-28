import os
import api_pb2_grpc
import time
import grpc

def run():
    with grpc.insecure_channel("localhost:6012") as channel:
        stub = api_pb2_grpc.CommunicationsApiStub(channel)
        while True:
            try:
                response = stub.Publish(api_pb2_grpc.api__pb2.PublishPayload(topic="0xtestroom", message=str.encode("HELLO")))
                print("response=%s" % 
                (response))
                exit()
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(close)
                exit()

def close(channel):
    channel.close()

if __name__ == "__main__":
    run()