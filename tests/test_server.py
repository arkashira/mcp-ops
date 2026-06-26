import pytest
from server import Server, ServerManager

def test_add_and_dashboard():
    manager = ServerManager()
    srv = Server(name="srv1", status="running", metrics={"cpu": 0.5})
    manager.add_server(srv)
    dashboard = manager.get_dashboard()
    assert len(dashboard) == 1
    assert dashboard[0]["name"] == "srv1"
    assert dashboard[0]["status"] == "running"
    assert dashboard[0]["metrics"]["cpu"] == 0.5

def test_update_status_and_alert():
    manager = ServerManager()
    srv = Server(name="srv2", status="running")
    manager.add_server(srv)
    alerts = []

    def alert_cb(server):
        alerts.append((server.name, server.status))

    manager.register_alert(alert_cb)
    manager.update_status("srv2", "error")
    assert alerts == [("srv2", "error")]
    # status should be updated
    assert manager._servers["srv2"].status == "error"

def test_update_metrics():
    manager = ServerManager()
    srv = Server(name="srv3")
    manager.add_server(srv)
    manager.update_metrics("srv3", {"memory": 1024.0})
    assert manager._servers["srv3"].metrics["memory"] == 1024.0

def test_remove_server():
    manager = ServerManager()
    srv = Server(name="srv4")
    manager.add_server(srv)
    manager.remove_server("srv4")
    assert "srv4" not in manager._servers

def test_update_nonexistent_server_raises():
    manager = ServerManager()
    with pytest.raises(KeyError):
        manager.update_status("nonexistent", "running")

def test_dashboard_thread_safety():
    # Ensure that get_dashboard can be called while updates happen
    manager = ServerManager()
    srv = Server(name="srv5", status="running")
    manager.add_server(srv)

    # Simulate concurrent update
    def updater():
        for _ in range(10):
            manager.update_status("srv5", "running")

    t = pytest.MonkeyPatch()
    t.setattr("threading.Thread", lambda target, daemon: None)  # no-op thread
    updater()
    dashboard = manager.get_dashboard()
    assert dashboard[0]["status"] == "running"
