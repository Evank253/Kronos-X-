from kronos_x.models import SourcePin, EvidenceStatus
from kronos_x.execution.isolated_worker import ReferenceIsolatedWorker

def test_reference_worker_is_explicitly_blocked():
    result=ReferenceIsolatedWorker().execute("EX-1","RUN-1",SourcePin("repo","a"*40),("pytest","-q"))
    assert result.status is EvidenceStatus.BLOCKED
    assert result.network=="DENIED"
    assert result.secrets=="NONE"
    assert result.worker_identity=="REFERENCE_NOT_CONNECTED"
