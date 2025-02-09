from http.client import responses

import grpc
from service_pb2 import CheckAccessRequest
from service_pb2_grpc import AccessControlStub


def check_access(username, repository_name, organization_name):
    channel = grpc.insecure_channel("localhost:50051")
    client = AccessControlStub(channel)

    # Sample request
    request = CheckAccessRequest(
        username=username,
        repository_name=repository_name,
        organization_name=organization_name
    )

    try:
        return client.CheckAccess(request)
    except grpc.RpcError as e:
        print(f"gRPC error: {e.details()}")


if __name__ == "__main__":
    # Test the gRPC service
    username = "lironbilya"
    repository_name = "Secret-Project"
    organization_name = "LiRoNaORG"
    
    response = check_access(username, repository_name, organization_name)
    if response:
        access = "has access" if response.allowed else "does NOT have access"
        result = f"User {username} {access} to repository {repository_name} in the organization {organization_name}"
    else:
        result = "Error occurred on server."
    
    print(result)
