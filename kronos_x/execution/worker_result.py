from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True, slots=True)
class RawObservation:
    execution_id: str
    stdout: bytes
    stderr: bytes
    exit_code: Optional[int]
    started_at: str
    finished_at: str

    @property
    def combined_bytes(self) -> bytes:
        return self.stdout + b"\x00" + self.stderr
