from kronos_x.models import EvidenceStatus, SourcePin, ExecutionRecord, EvidenceManifest
from kronos_x.execution.boundary import ExecutionBoundary

def test_execution_record_preserves_exact_source():
    p=SourcePin("repo","6167544")
    e=ExecutionRecord("EX-1","RUN-1",p,("pytest","-q"),EvidenceStatus.BLOCKED,"NOT_CONNECTED")
    assert e.source.commit_sha=="6167544"

def test_evidence_manifest_cannot_grant_authority():
    m=EvidenceManifest("EV-1","RUN-1","EX-1","abc","deadbeef",EvidenceStatus.VERIFIED)
    assert m.qualification=="NOT_CLAIMED"
    assert m.authority_granted is False

def test_safe_boundary_has_no_execution_success():
    result=ExecutionBoundary().execute()
    assert result.status is EvidenceStatus.BLOCKED
