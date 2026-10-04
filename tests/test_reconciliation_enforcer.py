from kronos_x.reconciliation.enforcer import ReconciliationInput, ReconciliationStatus, reconcile

def test_matching_source_states_agree():
    r=reconcile(ReconciliationInput('repo','a'*40,'repo','a'*40))
    assert r.status is ReconciliationStatus.AGREEMENT
    assert r.qualification_path_allowed is True

def test_source_mismatch_blocks_qualification_path():
    r=reconcile(ReconciliationInput('repo','a'*40,'repo','b'*40))
    assert r.status is ReconciliationStatus.MISMATCH
    assert r.qualification_path_allowed is False

def test_missing_identity_is_not_measured():
    r=reconcile(ReconciliationInput('repo',None,'repo','a'*40))
    assert r.status is ReconciliationStatus.NOT_MEASURED
    assert r.qualification_path_allowed is False
