from dataclasses import dataclass
from typing import List

@dataclass
class Policy:
    name: str
    rules: List[str]

@dataclass
class Server:
    name: str
    compliant: bool
    violated_rules: List[str]

class GovernanceEngine:
    def __init__(self, policies: List[Policy]):
        self.policies = policies
        self.servers = []

    def add_server(self, server: Server):
        self.servers.append(server)

    def get_compliance_status(self, server_name: str) -> Server:
        for server in self.servers:
            if server.name == server_name:
                return server
        return None

    def flag_for_remediation(self, server_name: str):
        for server in self.servers:
            if server.name == server_name:
                server.compliant = False
                return
