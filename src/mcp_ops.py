import json
from dataclasses import dataclass
from typing import List

@dataclass
class MCP_Server:
    version: str
    capabilities: List[str]
    security_patches: List[str]
    server_type: str
    location: str

class MCP_Ops:
    def __init__(self):
        self.servers = []

    def add_server(self, server: MCP_Server):
        self.servers.append(server)

    def search_servers(self, keyword: str) -> List[MCP_Server]:
        return [server for server in self.servers if keyword in server.version or keyword in server.capabilities or keyword in server.security_patches]

    def filter_servers(self, server_type: str = None, location: str = None) -> List[MCP_Server]:
        filtered_servers = self.servers
        if server_type:
            filtered_servers = [server for server in filtered_servers if server.server_type == server_type]
        if location:
            filtered_servers = [server for server in filtered_servers if server.location == location]
        return filtered_servers

    def get_server_details(self, server: MCP_Server) -> dict:
        return {
            "version": server.version,
            "capabilities": server.capabilities,
            "security_patches": server.security_patches,
            "server_type": server.server_type,
            "location": server.location
        }
