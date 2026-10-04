from dataclasses import dataclass
from enum import Enum

class QualificationStatus(str, Enum):
    NOT_CLAIMED="NOT_CLAIMED"
    REVIEW_REQUIRED="REVIEW_REQUIRED"
    QUALIFIED="QUALIFIED"

class QualificationBoundaryError(PermissionError):
    pass

@dataclass(frozen=True, slots=True)
class QualificationInput:
    evidence_status: str
    verification_status: str
    reconciliation_status: str
    authority_granted: bool = False

@dataclass(frozen=True, slots=True)
class QualificationDecision:
    status: QualificationStatus
    human_review_required: bool
    authority_granted: bool
    reason: str

def evaluate_qualification(i: QualificationInput) -> QualificationDecision:
    if i.authority_granted:
        raise QualificationBoundaryError("qualification evaluation cannot grant authority")
    if i.reconciliation_status != "AGREEMENT":
        return QualificationDecision(QualificationStatus.NOT_CLAIMED, True, False, "reconciliation is not AGREEMENT")
    if i.evidence_status in {"BLOCKED", "NOT_MEASURED"} or i.verification_status != "VERIFIED":
        return QualificationDecision(QualificationStatus.NOT_CLAIMED, True, False, "evidence or verification is insufficient")
    return QualificationDecision(QualificationStatus.REVIEW_REQUIRED, True, False, "explicit qualification review required")
