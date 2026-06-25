from mcp_ops import MCPRegistry, Server
import pytest

def test_register_server():
    registry = MCPRegistry()
    server = Server("1.0", ["tag1", "tag2"], "compliant")
    registry.register_server(server)
    assert len(registry.get_servers()) == 1

def test_register_server_missing_mandatory_fields():
    registry = MCPRegistry()
    server = Server("", ["tag1", "tag2"], "compliant")
    with pytest.raises(ValueError):
        registry.register_server(server)

def test_get_servers_by_tags():
    registry = MCPRegistry()
    server1 = Server("1.0", ["tag1", "tag2"], "compliant")
    server2 = Server("2.0", ["tag2", "tag3"], "non-compliant")
    registry.register_server(server1)
    registry.register_server(server2)
    assert len(registry.get_servers(tags=["tag1"])) == 1

def test_get_servers_by_compliance_status():
    registry = MCPRegistry()
    server1 = Server("1.0", ["tag1", "tag2"], "compliant")
    server2 = Server("2.0", ["tag2", "tag3"], "non-compliant")
    registry.register_server(server1)
    registry.register_server(server2)
    assert len(registry.get_servers(compliance_status="compliant")) == 1

def test_to_json():
    registry = MCPRegistry()
    server = Server("1.0", ["tag1", "tag2"], "compliant")
    registry.register_server(server)
    expected_json = '[{"version": "1.0", "tags": ["tag1", "tag2"], "compliance_status": "compliant"}]'
    assert registry.to_json() == expected_json
