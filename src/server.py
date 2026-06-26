import time
import threading
from dataclasses import dataclass, field
from typing import Dict, List, Callable, Any

@dataclass
class Server:
    name: str
    status: str = "unknown"  # could be "running", "stopped", "error"
    metrics: Dict[str, float] = field(default_factory=dict)

class ServerManager:
    """
    Manages a collection of servers, provides real-time status,
    triggers alerts on critical issues, and stores performance metrics.
    """
    def __init__(self):
        self._servers: Dict[str, Server] = {}
        self._alert_callbacks: List[Callable[[Server], None]] = []
        self._lock = threading.Lock()

    def add_server(self, server: Server) -> None:
        with self._lock:
            self._servers[server.name] = server

    def remove_server(self, name: str) -> None:
        with self._lock:
            self._servers.pop(name, None)

    def update_status(self, name: str, status: str) -> None:
        with self._lock:
            server = self._servers.get(name)
            if not server:
                raise KeyError(f"Server {name} not found")
            server.status = status
            if status == "error":
                self._trigger_alert(server)

    def update_metrics(self, name: str, metrics: Dict[str, float]) -> None:
        with self._lock:
            server = self._servers.get(name)
            if not server:
                raise KeyError(f"Server {name} not found")
            server.metrics.update(metrics)

    def get_dashboard(self) -> List[Dict[str, Any]]:
        with self._lock:
            return [
                {"name": s.name, "status": s.status, "metrics": s.metrics.copy()}
                for s in self._servers.values()
            ]

    def register_alert(self, callback: Callable[[Server], None]) -> None:
        with self._lock:
            self._alert_callbacks.append(callback)

    def _trigger_alert(self, server: Server) -> None:
        for cb in self._alert_callbacks:
            cb(server)

    # Simulate real-time polling (not used in tests)
    def start_polling(self, interval: float = 5.0) -> None:
        def poll():
            while True:
                time.sleep(interval)
                # In a real system, we would fetch status here
        thread = threading.Thread(target=poll, daemon=True)
        thread.start()
