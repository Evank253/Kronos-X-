import pytest
from kronos_x.review.independent import *

def subject():
    return ReviewSubject("RUN-001","a"*40,"b"*64,"producer")

def test_producer_cannot_review_own_result():
    with pytest.raises(IndependentReviewBoundaryError):
        create_review_request(subject(),"producer",b"actual evidence","runner")

def test_submitter_cannot_be_reviewer():
    with pytest.raises(IndependentReviewBoundaryError):
        create_review_request(subject(),"runner",b"actual evidence","runner")

def test_review_requires_actual_evidence():
    with pytest.raises(IndependentReviewBoundaryError):
        create_review_request(subject(),"reviewer",b"","runner")

def test_independent_reviewer_gets_actual_evidence():
    r=create_review_request(subject(),"reviewer",b"RAW-EVIDENCE","runner")
    assert r.evidence==b"RAW-EVIDENCE"
    assert r.subject.evidence_hash=="b"*64

def test_wrong_reviewer_cannot_decide():
    r=create_review_request(subject(),"reviewer",b"RAW-EVIDENCE","runner")
    with pytest.raises(IndependentReviewBoundaryError):
        issue_review_decision(r,ReviewStatus.ACCEPTED,"producer","not independent")

def test_independent_reviewer_can_decide():
    r=create_review_request(subject(),"reviewer",b"RAW-EVIDENCE","runner")
    d=issue_review_decision(r,ReviewStatus.ACCEPTED,"reviewer","evidence reviewed")
    assert d.independent is True
    assert d.status is ReviewStatus.ACCEPTED
