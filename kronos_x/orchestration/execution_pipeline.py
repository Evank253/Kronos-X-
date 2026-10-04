from ..models import EvidenceStatus, RunRecord, ExecutionRecord, EvidenceManifest
from ..provenance.hashing import sha256_bytes
from ..execution.adapter import IsolatedExecutionAdapter

class ExecutionPipeline:
    def __init__(self, adapter:IsolatedExecutionAdapter):
        self.adapter=adapter

    def run(self, run:RunRecord, execution_id:str, command:tuple[str,...]):
        execution=self.adapter.execute(execution_id,run.run_id,run.source,command)
        observation=(execution.stdout_sha256 or "") + ":" + (execution.stderr_sha256 or "")
        observation_hash=sha256_bytes(observation.encode())
        evidence=EvidenceManifest(
            evidence_id=f"EV-{execution_id}",
            run_id=run.run_id,
            execution_id=execution.execution_id,
            source_commit=execution.source.commit_sha,
            observation_sha256=observation_hash,
            status=execution.status,
        )
        return execution,evidence
