from __future__ import print_function

import grpc
import time
import users_pb2
import users_pb2_grpc

class Users(users_pb2_grpc.UsersServicer):

    def GetUsers(self, request, context):
        return users_pb2.GetUsersResponse(users=[
            users_pb2.User(
                id = "1",
                name = "KPC",
                email = "kpc@kpc.com",
                password = "password"
            )
        ])
    
def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.GetUsers(users_pb2.GetUsersRequest())
        print(response.users)
        time.sleep(10)
        response = stub.GetUserById(users_pb2.GetUserByIdRequest(id='1'))
        print(response.user)

if __name__ == '__main__':
    run()
