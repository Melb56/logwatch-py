from dataclasses import dataclass

@dataclass
class LogEntry:
    timestamp: str
    hostname: str
    service: str
    message: str

    def __str__(self):
        return f"[{self.timestamp}] {self.hostname} {self.service}: {self.message}"