"""Reference isolated-worker boundary.

This module intentionally does not execute host commands. It defines the contract and
returns BLOCKED until a separately controlled worker implementation is supplied.
"""
from dataclasses import dataclass
from ..models import EvidenceStatus, ExecutionRecord, SourcePin

@dataclass(frozen=True, slots=True)
class WorkerPolicy:
    network: str = "DENIED"
    secrets: str = "NONE"
    host_filesystem: str = "DENIED"
    privileged_operations: str = "DENIED"

class ReferenceIsolatedWorker:
    policy = WorkerPolicy()

    def execute(self, execution_id: str, run_id: str, source: SourcePin, command: tuple[str, ...]) -> ExecutionRecord:
        return ExecutionRecord(
            execution_id=execution_id,
            run_id=run_id,
            source=source,
            command=command,
            status=EvidenceStatus.BLOCKED,
            worker_identity="REFERENCE_NOT_CONNECTED",
            network=self.policy.network,
            secrets=self.policy.secrets,
        )
