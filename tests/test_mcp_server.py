from mcp_server import MCPServer, MCPDeployment

def test_add_server():
    deployment = MCPDeployment()
    server = MCPServer("test_server", "pending")
    deployment.add_server(server)
    assert len(deployment.servers) == 1

def test_deploy_server():
    deployment = MCPDeployment()
    server = MCPServer("test_server", "pending")
    deployment.add_server(server)
    deployed_server = deployment.deploy_server("test_server")
    assert deployed_server.status == "deploying"

def test_get_deployment_status():
    deployment = MCPDeployment()
    server = MCPServer("test_server", "pending")
    deployment.add_server(server)
    deployment.deploy_server("test_server")
    status = deployment.get_deployment_status("test_server")
    assert status == "deploying"

def test_enforce_policies():
    deployment = MCPDeployment()
    server = MCPServer("test_server", "pending")
    deployment.add_server(server)
    deployment.add_security_policy("policy1")
    deployment.add_governance_policy("policy2")
    result = deployment.enforce_policies("test_server")
    assert result == True

def test_add_to_managed_servers():
    deployment = MCPDeployment()
    server = MCPServer("test_server", "pending")
    deployment.add_server(server)
    deployment.deploy_server("test_server")
    result = deployment.add_to_managed_servers("test_server")
    assert result == True

def test_deploy_non_existent_server():
    deployment = MCPDeployment()
    result = deployment.deploy_server("non_existent_server")
    assert result is None

def test_get_deployment_status_non_existent_server():
    deployment = MCPDeployment()
    result = deployment.get_deployment_status("non_existent_server")
    assert result is None

def test_enforce_policies_non_existent_server():
    deployment = MCPDeployment()
    result = deployment.enforce_policies("non_existent_server")
    assert result == False

def test_add_to_managed_servers_non_existent_server():
    deployment = MCPDeployment()
    result = deployment.add_to_managed_servers("non_existent_server")
    assert result == False
