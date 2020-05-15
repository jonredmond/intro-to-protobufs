import grpc

# import the generated classes
import hello_world_pb2
import hello_world_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:8080')

stub = hello_world_pb2_grpc.HelloWorldStub(channel)

request = hello_world_pb2.Request(name="Espresso")

response = stub.Hello(request)

print(response.greeting)