from kronos_x.qualification.boundary import QualificationInput, QualificationStatus, evaluate_qualification

def test_evidence_cannot_auto_qualify():
    d=evaluate_qualification(QualificationInput("OBSERVED","VERIFIED","AGREEMENT"))
    assert d.status is QualificationStatus.REVIEW_REQUIRED
    assert d.authority_granted is False

def test_not_measured_blocks_qualification():
    d=evaluate_qualification(QualificationInput("NOT_MEASURED","VERIFIED","AGREEMENT"))
    assert d.status is QualificationStatus.NOT_CLAIMED

def test_blocked_blocks_qualification():
    d=evaluate_qualification(QualificationInput("BLOCKED","VERIFIED","AGREEMENT"))
    assert d.status is QualificationStatus.NOT_CLAIMED

def test_reconciliation_mismatch_blocks_qualification():
    d=evaluate_qualification(QualificationInput("OBSERVED","VERIFIED","MISMATCH"))
    assert d.status is QualificationStatus.NOT_CLAIMED

def test_verification_alone_does_not_qualify():
    d=evaluate_qualification(QualificationInput("OBSERVED","VERIFIED","AGREEMENT"))
    assert d.status is not QualificationStatus.QUALIFIED

def test_authority_cannot_be_granted_by_evaluator():
    from kronos_x.qualification.boundary import QualificationBoundaryError
    try:
        evaluate_qualification(QualificationInput("OBSERVED","VERIFIED","AGREEMENT",True))
    except QualificationBoundaryError:
        return
    assert False
