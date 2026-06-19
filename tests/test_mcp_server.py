from mcp_server import MCPServer, MCPDeployment, MCPPlatform

def test_add_server():
    deployment = MCPDeployment()
    server = MCPServer("TestServer", "available")
    deployment.add_server(server)
    assert server in deployment.servers

def test_add_security_policy():
    deployment = MCPDeployment()
    policy = "TestPolicy"
    deployment.add_security_policy(policy)
    assert policy in deployment.security_policies

def test_add_governance_policy():
    deployment = MCPDeployment()
    policy = "TestPolicy"
    deployment.add_governance_policy(policy)
    assert policy in deployment.governance_policies

def test_deploy_server():
    deployment = MCPDeployment()
    server = MCPServer("TestServer", "available")
    deployment.add_server(server)
    deployment.add_security_policy("TestSecurityPolicy")
    deployment.add_governance_policy("TestGovernancePolicy")
    deployed_server = deployment.deploy_server(server)
    assert deployed_server.status == "deploying"

def test_get_deployment_status():
    deployment = MCPDeployment()
    server = MCPServer("TestServer", "available")
    deployment.add_server(server)
    deployment.add_security_policy("TestSecurityPolicy")
    deployment.add_governance_policy("TestGovernancePolicy")
    deployment.deploy_server(server)
    status = deployment.get_deployment_status(server)
    assert status == "deploying"

def test_get_deployment_logs():
    deployment = MCPDeployment()
    server = MCPServer("TestServer", "available")
    deployment.add_server(server)
    deployment.add_security_policy("TestSecurityPolicy")
    deployment.add_governance_policy("TestGovernancePolicy")
    deployment.deploy_server(server)
    logs = deployment.get_deployment_logs(server)
    assert logs == "Deployment logs for TestServer"

def test_discover_servers():
    platform = MCPPlatform()
    servers = platform.discover_servers()
    assert len(servers) == 2

def test_initiate_deployment():
    platform = MCPPlatform()
    server = MCPServer("TestServer", "available")
    platform.deployment.add_server(server)
    platform.deployment.add_security_policy("TestSecurityPolicy")
    platform.deployment.add_governance_policy("TestGovernancePolicy")
    deployed_server = platform.initiate_deployment(server)
    assert deployed_server.status == "deploying"

def test_get_managed_servers():
    platform = MCPPlatform()
    server = MCPServer("TestServer", "available")
    platform.deployment.add_server(server)
    managed_servers = platform.get_managed_servers()
    assert server in managed_servers
