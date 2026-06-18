import pytest
from src.mcp_server import MCPServer, MCPDeployment, MCPPlatform

def test_mcp_server_to_json():
    server = MCPServer(1, "Server 1", ["policy1", "policy2"], ["governance1", "governance2"])
    json_string = server.to_json()
    assert json_string == '{"id": 1, "name": "Server 1", "security_policies": ["policy1", "policy2"], "governance_policies": ["governance1", "governance2"]}'

def test_mcp_deployment_deploy_server():
    deployment = MCPDeployment()
    server = MCPServer(1, "Server 1", ["policy1", "policy2"], ["governance1", "governance2"])
    deployed_server = deployment.deploy_server(server)
    assert deployed_server.id == 1
    assert deployed_server.name == "Server 1"

def test_mcp_deployment_get_deployment_status():
    deployment = MCPDeployment()
    server = MCPServer(1, "Server 1", ["policy1", "policy2"], ["governance1", "governance2"])
    deployment.deploy_server(server)
    status = deployment.get_deployment_status(1)
    assert status == "Server Server 1 deployed successfully"

def test_mcp_deployment_get_deployment_logs():
    deployment = MCPDeployment()
    server = MCPServer(1, "Server 1", ["policy1", "policy2"], ["governance1", "governance2"])
    deployment.deploy_server(server)
    logs = deployment.get_deployment_logs(1)
    assert logs == "Deployment logs for server Server 1"

def test_mcp_platform_discover_servers():
    platform = MCPPlatform()
    discovered_servers = platform.discover_servers()
    assert len(discovered_servers) == 2

def test_mcp_platform_initiate_deployment():
    platform = MCPPlatform()
    server = MCPServer(1, "Server 1", ["policy1", "policy2"], ["governance1", "governance2"])
    deployment = platform.initiate_deployment(server)
    assert deployment.deployed_servers[0].id == 1

def test_mcp_platform_get_managed_servers():
    platform = MCPPlatform()
    server = MCPServer(1, "Server 1", ["policy1", "policy2"], ["governance1", "governance2"])
    deployment = platform.initiate_deployment(server)
    managed_servers = platform.get_managed_servers()
    assert len(managed_servers) == 1
