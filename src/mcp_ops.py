import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Server:
    version: str
    tags: List[str]
    compliance_status: str

class MCPRegistry:
    def __init__(self):
        self.servers = []

    def register_server(self, server: Server) -> None:
        if not all([server.version, server.tags, server.compliance_status]):
            raise ValueError("Mandatory fields are missing")
        self.servers.append(server)

    def get_servers(self, tags: List[str] = None, compliance_status: str = None) -> List[Server]:
        filtered_servers = self.servers
        if tags:
            filtered_servers = [s for s in filtered_servers if any(t in s.tags for t in tags)]
        if compliance_status:
            filtered_servers = [s for s in filtered_servers if s.compliance_status == compliance_status]
        return filtered_servers

    def to_json(self) -> str:
        return json.dumps([{"version": s.version, "tags": s.tags, "compliance_status": s.compliance_status} for s in self.servers])
