from kronos_x.models.records import EvidenceStatus, SourcePin
from kronos_x.orchestration.state import new_run
from kronos_x.execution.boundary import ExecutionBoundary
from kronos_x.reconciliation.service import reconcile

def test_unimplemented_execution_is_blocked():
    r=ExecutionBoundary().execute()
    assert r.status is EvidenceStatus.BLOCKED

def test_reconciliation_mismatch_is_unresolved():
    r=reconcile("R-1","RUN-1","A","B")
    assert r.status is EvidenceStatus.UNRESOLVED

def test_reconciliation_match_is_verified():
    r=reconcile("R-1","RUN-1","A","A")
    assert r.status is EvidenceStatus.VERIFIED

def test_new_run_is_not_measured():
    state=new_run("RUN-1",SourcePin("repo","abc"))
    assert state.run.status is EvidenceStatus.NOT_MEASURED

def test_source_pin_is_immutable():
    p=SourcePin("repo","abc")
    try: p.commit_sha="evil"
    except Exception: pass
    else: raise AssertionError("SourcePin must be immutable")
