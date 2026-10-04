from dataclasses import dataclass
from ..provenance.hashing import sha256_bytes
from .worker_result import RawObservation

@dataclass(frozen=True, slots=True)
class CapturedObservation:
    observation:RawObservation
    stdout_sha256:str
    stderr_sha256:str
    combined_sha256:str

def capture(observation:RawObservation)->CapturedObservation:
    combined=observation.stdout+b"\x00"+observation.stderr
    return CapturedObservation(observation,sha256_bytes(observation.stdout),sha256_bytes(observation.stderr),sha256_bytes(combined))
