import pytest
from mcp_ops import MCP_Ops, MCP_Server

@pytest.fixture
def mcp_ops():
    mcp_ops = MCP_Ops()
    mcp_ops.add_server(MCP_Server("1.0", ["capability1", "capability2"], ["patch1", "patch2"], "type1", "location1"))
    mcp_ops.add_server(MCP_Server("2.0", ["capability3", "capability4"], ["patch3", "patch4"], "type2", "location2"))
    return mcp_ops

def test_search_servers(mcp_ops):
    assert len(mcp_ops.search_servers("capability1")) == 1
    assert len(mcp_ops.search_servers("capability3")) == 1
    assert len(mcp_ops.search_servers("non-existent")) == 0

def test_filter_servers(mcp_ops):
    assert len(mcp_ops.filter_servers(server_type="type1")) == 1
    assert len(mcp_ops.filter_servers(location="location2")) == 1
    assert len(mcp_ops.filter_servers(server_type="type1", location="location1")) == 1
    assert len(mcp_ops.filter_servers(server_type="non-existent")) == 0

def test_get_server_details(mcp_ops):
    server = mcp_ops.servers[0]
    details = mcp_ops.get_server_details(server)
    assert details["version"] == "1.0"
    assert details["capabilities"] == ["capability1", "capability2"]
    assert details["security_patches"] == ["patch1", "patch2"]
    assert details["server_type"] == "type1"
    assert details["location"] == "location1"
