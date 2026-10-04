import pytest
from kronos_x.repair.provenance import *

def finding():
    return RepairFinding("F-001","a"*40,"fix ownership boundary",("engine.py","models.py"))

def candidate(**kw):
    base=dict(repair_id="R-001",finding_id="F-001",parent_commit="a"*40,proposed_paths=("engine.py",),patch_hash="c"*64,reviewer_id="reviewer",producer_id="repair-agent")
    base.update(kw)
    return RepairCandidate(**base)

def test_repair_must_trace_to_finding():
    with pytest.raises(RepairBoundaryError):
        validate_repair(candidate(finding_id="F-999"),finding())

def test_repair_parent_must_match_source():
    with pytest.raises(RepairBoundaryError):
        validate_repair(candidate(parent_commit="b"*40),finding())

def test_repair_requires_patch_identity():
    with pytest.raises(RepairBoundaryError):
        validate_repair(candidate(patch_hash=""),finding())

def test_repair_producer_cannot_self_validate():
    with pytest.raises(RepairBoundaryError):
        validate_repair(candidate(reviewer_id="repair-agent"),finding())

def test_unrelated_change_is_not_silently_accepted():
    d=validate_repair(candidate(proposed_paths=("engine.py","governance.py")),finding())
    assert d.valid is False
    assert d.independent_review_required is True

def test_scoped_repair_remains_subject_to_independent_review():
    d=validate_repair(candidate(),finding())
    assert d.valid is True
    assert d.independent_review_required is True
