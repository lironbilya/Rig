import grpc
from concurrent import futures
import service_pb2
import service_pb2_grpc
from github_handler import get_permissions
import policies_engine

class AccessControlService(service_pb2_grpc.AccessControlServicer):
    def CheckAccess(self, request, context):
        username = request.username
        repository_name = request.repository_name
        organization_name = request.organization_name

        org_data = get_permissions(organization_name)
        policies_engine.add_data({"repos": org_data}, "github_data")
        result = policies_engine.check_access({"username": username, "repository_name": repository_name}, "access_control", "allow")
        return service_pb2.CheckAccessResponse(allowed=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    service_pb2_grpc.add_AccessControlServicer_to_server(AccessControlService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server is running on port 50051...")
    server.wait_for_termination()
