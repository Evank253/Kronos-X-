from dataclasses import dataclass
from enum import Enum

class RepairBoundaryError(PermissionError):
    pass

class ChangeType(str, Enum):
    REPAIR="REPAIR"
    UNRELATED="UNRELATED"

@dataclass(frozen=True, slots=True)
class RepairFinding:
    finding_id: str
    source_commit: str
    hypothesis: str
    allowed_paths: tuple[str,...]

@dataclass(frozen=True, slots=True)
class RepairCandidate:
    repair_id: str
    finding_id: str
    parent_commit: str
    proposed_paths: tuple[str,...]
    patch_hash: str
    reviewer_id: str
    producer_id: str

@dataclass(frozen=True, slots=True)
class RepairValidation:
    repair_id: str
    finding_id: str
    valid: bool
    independent_review_required: bool
    reason: str

def validate_repair(candidate: RepairCandidate, finding: RepairFinding) -> RepairValidation:
    if candidate.finding_id != finding.finding_id:
        raise RepairBoundaryError("repair is not traceable to its originating finding")
    if candidate.parent_commit != finding.source_commit:
        raise RepairBoundaryError("repair parent does not match finding source state")
    if not candidate.patch_hash:
        raise RepairBoundaryError("repair must have a patch identity")
    if candidate.producer_id == candidate.reviewer_id:
        raise RepairBoundaryError("repair producer cannot validate its own repair")
    unexpected=set(candidate.proposed_paths)-set(finding.allowed_paths)
    if unexpected:
        return RepairValidation(candidate.repair_id,finding.finding_id,False,True,"repair modifies paths outside declared repair scope")
    return RepairValidation(candidate.repair_id,finding.finding_id,True,True,"repair is traceable and remains subject to independent review")
