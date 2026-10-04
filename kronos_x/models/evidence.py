from dataclasses import dataclass
from .records import EvidenceStatus

@dataclass(frozen=True, slots=True)
class EvidenceManifest:
    evidence_id: str
    run_id: str
    execution_id: str
    source_commit: str
    observation_sha256: str
    status: EvidenceStatus
    qualification: str = "NOT_CLAIMED"
    authority_granted: bool = False
    schema_version: str = "1"
