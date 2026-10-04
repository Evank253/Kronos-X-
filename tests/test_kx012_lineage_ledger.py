from kronos_x.lineage.ledger import *

def ev(n,stage,pred=None,eid=None):
    return LedgerEvent(n,eid or f"E-{n}", "RUN-1", stage, pred)

def complete_events():
    out=[]
    pred=None
    for n,stage in enumerate(REQUIRED_STAGES,1):
        e=ev(n,stage,pred)
        out.append(e); pred=e.event_id
    return tuple(out)

def test_complete_ordered_chain_is_complete():
    d=validate_ledger(complete_events(),"RUN-1")
    assert d.status is LedgerStatus.COMPLETE

def test_missing_event_is_invalid():
    events=list(complete_events()); events.pop(5)
    events=[LedgerEvent(i+1,e.event_id,e.run_id,e.stage,(events[i-1].event_id if i else None)) for i,e in enumerate(events)]
    assert validate_ledger(tuple(events),"RUN-1").status is LedgerStatus.OPEN

def test_reordered_event_is_invalid():
    events=list(complete_events()); events[2],events[3]=events[3],events[2]
    assert validate_ledger(tuple(events),"RUN-1").status is LedgerStatus.INVALID

def test_duplicate_event_is_invalid():
    events=list(complete_events()); events[3]=events[2]
    assert validate_ledger(tuple(events),"RUN-1").status is LedgerStatus.INVALID

def test_orphan_run_is_invalid():
    events=list(complete_events()); events[4]=LedgerEvent(events[4].sequence,events[4].event_id,"RUN-X",events[4].stage,events[4].predecessor_event_id)
    assert validate_ledger(tuple(events),"RUN-1").status is LedgerStatus.INVALID

def test_broken_predecessor_chain_is_invalid():
    events=list(complete_events()); events[5]=LedgerEvent(6,"E-6","RUN-1","BASELINE","E-1")
    assert validate_ledger(tuple(events),"RUN-1").status is LedgerStatus.INVALID

def test_empty_ledger_is_invalid():
    assert validate_ledger(tuple(),"RUN-1").status is LedgerStatus.INVALID
