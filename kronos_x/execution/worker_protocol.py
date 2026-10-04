from dataclasses import dataclass
from typing import Protocol
from ..models import SourcePin, ExecutionRecord

@dataclass(frozen=True, slots=True)
class WorkerLimits:
    timeout_seconds: int
    memory_mb: int
    cpu_seconds: int
    max_output_bytes: int

@dataclass(frozen=True, slots=True)
class WorkerRequest:
    execution_id: str
    run_id: str
    source: SourcePin
    command: tuple[str, ...]
    limits: WorkerLimits

class WorkerProtocol(Protocol):
    def execute(self, request: WorkerRequest) -> ExecutionRecord:
        """Run only inside a separately controlled worker and return signed/provenanced observation metadata."""
