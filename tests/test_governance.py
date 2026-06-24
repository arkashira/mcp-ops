from governance import GovernanceEngine, Policy, Server

def test_get_compliance_status():
    engine = GovernanceEngine([Policy("policy1", ["rule1", "rule2"])])
    server = Server("server1", True, [])
    engine.add_server(server)
    result = engine.get_compliance_status("server1")
    assert result.name == "server1"
    assert result.compliant

def test_flag_for_remediation():
    engine = GovernanceEngine([Policy("policy1", ["rule1", "rule2"])])
    server = Server("server1", True, [])
    engine.add_server(server)
    engine.flag_for_remediation("server1")
    result = engine.get_compliance_status("server1")
    assert not result.compliant

def test_violated_rules():
    engine = GovernanceEngine([Policy("policy1", ["rule1", "rule2"])])
    server = Server("server1", False, ["rule1"])
    engine.add_server(server)
    result = engine.get_compliance_status("server1")
    assert result.violated_rules == ["rule1"]

def test_non_existent_server():
    engine = GovernanceEngine([Policy("policy1", ["rule1", "rule2"])])
    result = engine.get_compliance_status("non_existent_server")
    assert result is None
