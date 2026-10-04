from kronos_x.execution.capture import capture
from kronos_x.execution.worker_result import RawObservation
from kronos_x.execution.lifecycle import WorkerLifecycle

def test_raw_observation_hashes_are_deterministic():
    o=RawObservation("EX-1",b"out",b"err",0,"2026-01-01T00:00:00Z","2026-01-01T00:00:01Z")
    c=capture(o)
    assert len(c.stdout_sha256)==64 and len(c.stderr_sha256)==64 and len(c.combined_sha256)==64

def test_lifecycle_has_explicit_destroyed_state():
    assert WorkerLifecycle.DESTROYED.value=="DESTROYED"
