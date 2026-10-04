from kronos_x.models import RunRecord, SourcePin, EvidenceStatus
from kronos_x.execution.boundary import ExecutionBoundary
from kronos_x.orchestration.execution_pipeline import ExecutionPipeline

class BoundaryAdapter:
    def execute(self, execution_id, run_id, source, command):
        result=ExecutionBoundary().execute()
        from kronos_x.models import ExecutionRecord
        return ExecutionRecord(execution_id,run_id,source,command,result.status,result.worker_identity)

def test_pipeline_preserves_blocked_state_and_source():
    run=RunRecord("RUN-1",SourcePin("repo","abc"))
    execution,evidence=ExecutionPipeline(BoundaryAdapter()).run(run,"EX-1",("pytest","-q"))
    assert execution.status is EvidenceStatus.BLOCKED
    assert evidence.status is EvidenceStatus.BLOCKED
    assert evidence.source_commit=="abc"
    assert evidence.qualification=="NOT_CLAIMED"
    assert evidence.authority_granted is False
