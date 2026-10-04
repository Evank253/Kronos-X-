from kronos_x.models.lifecycle import *
from kronos_x.orchestration.ledger import RunLedger

def test_finding_requires_explicit_type():
 f=FindingRecord("F1","R1",FindingType.BUG,"x")
 assert f.finding_type is FindingType.BUG

def test_repair_traces_to_finding_and_parent():
 r=RepairRecord("P1","abc","F1")
 assert r.parent_commit=="abc" and r.finding_id=="F1"

def test_independent_review_defaults_to_not_measured():
 r=ReviewRecord("RV1","P1","reviewer")
 assert r.decision=="NOT_MEASURED" and r.independent

def test_qualification_defaults_not_claimed():
 q=QualificationReviewRecord("Q1","P1")
 assert q.decision=="NOT_CLAIMED" and q.human_ratification_id is None

def test_ledger_is_contiguous():
 l=RunLedger()
 l=l.append(RunLedgerEntry(1,"R1","SOURCE_PINNED","OBSERVED","abc"))
 l=l.append(RunLedgerEntry(2,"R1","ENVIRONMENT_CREATED","OBSERVED","abc"))
 assert [e.sequence for e in l.entries]==[1,2]
