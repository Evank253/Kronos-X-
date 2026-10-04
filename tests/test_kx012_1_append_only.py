import pytest
from dataclasses import FrozenInstanceError
from kronos_x.lineage.ledger import *

def build():
    ledger=RunLedger("RUN-1")
    for n,stage in enumerate(REQUIRED_STAGES,1):
        ledger=ledger.append(f"E-{n}",stage)
    return ledger

def test_append_produces_new_ledger_and_preserves_history():
    a=RunLedger("RUN-1").append("E-1","DISCOVER")
    b=a.append("E-2","INDEX")
    assert len(a.events)==1
    assert len(b.events)==2
    assert b.events[1].predecessor_event_id=="E-1"

def test_complete_chain_is_tamper_evident():
    assert build().verify().status is LedgerStatus.COMPLETE

def test_existing_event_cannot_be_mutated():
    e=build().events[0]
    with pytest.raises(FrozenInstanceError):
        e.stage="EVIL"

def test_existing_event_cannot_be_replaced_by_append():
    a=RunLedger("RUN-1").append("E-1","DISCOVER")
    with pytest.raises(LedgerBoundaryError):
        a.append("E-1","EVIL")

def test_hash_mutation_is_detected():
    events=list(build().events)
    e=events[0]
    events[0]=LedgerEvent(e.sequence,e.event_id,e.run_id,e.stage,e.predecessor_event_id,"0"*64)
    assert validate_ledger(tuple(events),"RUN-1").status is LedgerStatus.INVALID

def test_content_mutation_is_detected():
    events=list(build().events)
    e=events[0]
    events[0]=LedgerEvent(e.sequence,e.event_id,e.run_id,"EVIL",e.predecessor_event_id,e.event_hash)
    assert validate_ledger(tuple(events),"RUN-1").status is LedgerStatus.INVALID

def test_predecessor_mutation_is_detected():
    events=list(build().events)
    e=events[1]
    events[1]=LedgerEvent(e.sequence,e.event_id,e.run_id,e.stage,"E-999",e.event_hash)
    assert validate_ledger(tuple(events),"RUN-1").status is LedgerStatus.INVALID

def test_run_identity_mismatch_is_detected():
    events=list(build().events)
    e=events[0]
    events[0]=LedgerEvent(e.sequence,e.event_id,"RUN-X",e.stage,e.predecessor_event_id,e.event_hash)
    assert validate_ledger(tuple(events),"RUN-1").status is LedgerStatus.INVALID

def test_sequence_reuse_is_detected():
    events=list(build().events)
    e=events[-1]
    events[-1]=LedgerEvent(1,e.event_id,e.run_id,e.stage,e.predecessor_event_id,e.event_hash)
    assert validate_ledger(tuple(events),"RUN-1").status is LedgerStatus.INVALID

def test_truncation_remains_incomplete():
    ledger=build()
    partial=RunLedger("RUN-1")
    for e in ledger.events[:-1]:
        partial=partial.append(e.event_id,e.stage)
    assert partial.verify().status is LedgerStatus.OPEN

def test_ledger_integrity_does_not_grant_authority():
    assert not hasattr(build(), "authority")
