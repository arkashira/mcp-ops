import json
from dataclasses import dataclass
from typing import List

@dataclass
class MCPServer:
    name: str
    status: str

class MCPDeployment:
    def __init__(self):
        self.servers = []
        self.security_policies = []
        self.governance_policies = []

    def add_server(self, server: MCPServer):
        self.servers.append(server)

    def add_security_policy(self, policy: str):
        self.security_policies.append(policy)

    def add_governance_policy(self, policy: str):
        self.governance_policies.append(policy)

    def deploy_server(self, server_name: str):
        for server in self.servers:
            if server.name == server_name:
                server.status = "deploying"
                return server
        return None

    def get_deployment_status(self, server_name: str):
        for server in self.servers:
            if server.name == server_name:
                return server.status
        return None

    def enforce_policies(self, server_name: str):
        for server in self.servers:
            if server.name == server_name:
                for policy in self.security_policies:
                    print(f"Enforcing security policy {policy} on {server_name}")
                for policy in self.governance_policies:
                    print(f"Enforcing governance policy {policy} on {server_name}")
                return True
        return False

    def add_to_managed_servers(self, server_name: str):
        for server in self.servers:
            if server.name == server_name:
                print(f"Adding {server_name} to managed servers list")
                return True
        return False
