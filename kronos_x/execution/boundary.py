from dataclasses import dataclass
from ..models.records import EvidenceStatus

@dataclass(frozen=True, slots=True)
class ExecutionResult:
    status: EvidenceStatus
    reason: str
    worker_identity: str="NOT_CONNECTED"

class ExecutionBoundary:
    """Safe foundation: arbitrary repository execution is explicitly unavailable until a worker is implemented and verified."""
    def execute(self,*args,**kwargs)->ExecutionResult:
        return ExecutionResult(EvidenceStatus.BLOCKED,"isolated execution worker is not connected")
