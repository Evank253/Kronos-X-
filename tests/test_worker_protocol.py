from kronos_x.execution.worker_protocol import WorkerLimits, WorkerRequest
from kronos_x.models import SourcePin

def test_worker_request_requires_explicit_limits():
    r=WorkerRequest("EX-1","RUN-1",SourcePin("repo","a"*40),("pytest","-q"),WorkerLimits(60,512,60,100000))
    assert r.limits.timeout_seconds==60
    assert r.limits.memory_mb==512
