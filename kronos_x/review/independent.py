from dataclasses import dataclass
from enum import Enum

class ReviewStatus(str, Enum):
    REVIEW_REQUIRED="REVIEW_REQUIRED"
    ACCEPTED="ACCEPTED"
    REJECTED="REJECTED"

class IndependentReviewBoundaryError(PermissionError):
    pass

@dataclass(frozen=True, slots=True)
class ReviewSubject:
    subject_id: str
    source_commit: str
    evidence_hash: str
    producer_id: str

@dataclass(frozen=True, slots=True)
class ReviewRequest:
    subject: ReviewSubject
    reviewer_id: str
    evidence: bytes
    submitted_by: str

@dataclass(frozen=True, slots=True)
class ReviewDecision:
    status: ReviewStatus
    reviewer_id: str
    subject_id: str
    evidence_hash: str
    independent: bool
    reason: str

def create_review_request(subject: ReviewSubject, reviewer_id: str, evidence: bytes, submitted_by: str) -> ReviewRequest:
    if reviewer_id == subject.producer_id:
        raise IndependentReviewBoundaryError("producer cannot review its own result")
    if reviewer_id == submitted_by:
        raise IndependentReviewBoundaryError("submitter cannot act as independent reviewer")
    if not evidence:
        raise IndependentReviewBoundaryError("review requires actual evidence")
    return ReviewRequest(subject, reviewer_id, evidence, submitted_by)

def issue_review_decision(request: ReviewRequest, status: ReviewStatus, reviewer_id: str, reason: str) -> ReviewDecision:
    if reviewer_id != request.reviewer_id:
        raise IndependentReviewBoundaryError("only the designated independent reviewer may issue the decision")
    if reviewer_id == request.subject.producer_id or reviewer_id == request.submitted_by:
        raise IndependentReviewBoundaryError("reviewer is not independent")
    return ReviewDecision(status, reviewer_id, request.subject.subject_id, request.subject.evidence_hash, True, reason)
