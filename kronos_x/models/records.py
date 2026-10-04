from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class EvidenceStatus(str, Enum):
    NOT_MEASURED="NOT_MEASURED"; BLOCKED="BLOCKED"; INCONCLUSIVE="INCONCLUSIVE"; OBSERVED="OBSERVED"; VERIFIED="VERIFIED"; FAILED="FAILED"; UNRESOLVED="UNRESOLVED"; NOT_CLAIMED="NOT_CLAIMED"

@dataclass(frozen=True, slots=True)
class SourcePin:
    repository: str
    commit_sha: str
    tree_sha: Optional[str]=None
    working_tree_state: str="UNKNOWN"
    runtime_version: Optional[str]=None
    dependency_lock_hash: Optional[str]=None

@dataclass(frozen=True, slots=True)
class StageRecord:
    stage_id: str
    name: str
    status: EvidenceStatus
    reason: Optional[str]=None
    provenance: dict=field(default_factory=dict)

@dataclass(frozen=True, slots=True)
class RunRecord:
    run_id: str
    source: SourcePin
    status: EvidenceStatus=EvidenceStatus.NOT_MEASURED
    stages: tuple[StageRecord,...]=()

@dataclass(frozen=True, slots=True)
class EvidenceRecord:
    evidence_id: str
    run_id: str
    status: EvidenceStatus
    content_sha256: Optional[str]=None
    observation_type: Optional[str]=None
    provenance: dict=field(default_factory=dict)

@dataclass(frozen=True, slots=True)
class ReconciliationRecord:
    reconciliation_id: str
    run_id: str
    index_identity: str
    execution_identity: str
    status: EvidenceStatus
    discrepancy: Optional[str]=None
