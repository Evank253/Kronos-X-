from kronos_x.models.records import EvidenceStatus, SourcePin, RunRecord
from kronos_x.orchestration.runner import LaboratoryOrchestrator

def test_orchestrator_records_blocked_stage():
    run=RunRecord("RUN-1",SourcePin("repo","abc"))
    o=LaboratoryOrchestrator(run).blocked("ISOLATE","worker unavailable")
    result=o.snapshot()
    assert result.ledger.entries[0].status=="BLOCKED"
    assert result.run.stages[0].status is EvidenceStatus.BLOCKED

def test_orchestrator_never_invents_measurement():
    run=RunRecord("RUN-1",SourcePin("repo","abc"))
    o=LaboratoryOrchestrator(run).not_measured("FULL_E2E","not implemented")
    assert o.snapshot().run.stages[0].status is EvidenceStatus.NOT_MEASURED
