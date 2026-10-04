from ..models.records import EvidenceStatus, ReconciliationRecord

def reconcile(reconciliation_id,run_id,index_identity,execution_identity):
    if index_identity != execution_identity:
        return ReconciliationRecord(reconciliation_id,run_id,index_identity,execution_identity,EvidenceStatus.UNRESOLVED,"identity mismatch")
    return ReconciliationRecord(reconciliation_id,run_id,index_identity,execution_identity,EvidenceStatus.VERIFIED)
