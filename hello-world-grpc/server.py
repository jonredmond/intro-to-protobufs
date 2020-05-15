import grpc
from concurrent import futures
import time

# import the generated classes
import hello_world_pb2
import hello_world_pb2_grpc

# Define our service class (derived from our protoc generated class)
class HelloWorldServicer(hello_world_pb2_grpc.HelloWorldServicer):
  def Hello(self, request, context):
    response = hello_world_pb2.Response()
    response.greeting = "Hello " + request.name + "!"
    return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

hello_world_pb2_grpc.add_HelloWorldServicer_to_server(HelloWorldServicer(), server)

# listen on port 8080
print('Starting server. Listening on port 8080.')
server.add_insecure_port('[::]:8080')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)