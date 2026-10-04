from dataclasses import dataclass
from typing import Optional
from .records import EvidenceStatus, SourcePin

@dataclass(frozen=True, slots=True)
class ExecutionRecord:
    execution_id: str
    run_id: str
    source: SourcePin
    command: tuple[str, ...]
    status: EvidenceStatus
    worker_identity: str
    stdout_sha256: Optional[str] = None
    stderr_sha256: Optional[str] = None
    exit_code: Optional[int] = None
    network: str = "DENIED"
    secrets: str = "NONE"
