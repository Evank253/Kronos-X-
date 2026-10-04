from dataclasses import dataclass
from enum import Enum

class LedgerBoundaryError(ValueError):
    pass

class LedgerStatus(str, Enum):
    OPEN="OPEN"
    COMPLETE="COMPLETE"
    INVALID="INVALID"

@dataclass(frozen=True, slots=True)
class LedgerEvent:
    sequence: int
    event_id: str
    run_id: str
    stage: str
    predecessor_event_id: str | None

@dataclass(frozen=True, slots=True)
class LedgerResult:
    status: LedgerStatus
    event_count: int
    reason: str

REQUIRED_STAGES=("DISCOVER","INDEX","PIN","ISOLATE","BUILD","BASELINE","TEST","BENCHMARK","EVALUATE","DIAGNOSE","REPAIR","RE-INDEX","RETEST","INDEPENDENT_REVIEW","FULL_E2E","REPRODUCE","RECONCILE","SEAL_EVIDENCE","REPORT")

def validate_ledger(events: tuple[LedgerEvent,...], run_id: str, required_stages: tuple[str,...]=REQUIRED_STAGES)->LedgerResult:
    if not events:
        return LedgerResult(LedgerStatus.INVALID,0,"ledger is empty")
    expected=1
    seen_ids=set()
    for event in events:
        if event.run_id != run_id:
            return LedgerResult(LedgerStatus.INVALID,len(events),"orphan event belongs to another run")
        if event.sequence != expected:
            return LedgerResult(LedgerStatus.INVALID,len(events),"missing or reordered sequence")
        if event.event_id in seen_ids:
            return LedgerResult(LedgerStatus.INVALID,len(events),"duplicate event id")
        if expected==1 and event.predecessor_event_id is not None:
            return LedgerResult(LedgerStatus.INVALID,len(events),"first event has a predecessor")
        if expected>1 and event.predecessor_event_id != events[expected-2].event_id:
            return LedgerResult(LedgerStatus.INVALID,len(events),"broken predecessor chain")
        seen_ids.add(event.event_id)
        expected+=1
    stages=tuple(e.stage for e in events)
    missing=tuple(s for s in required_stages if s not in stages)
    if missing:
        return LedgerResult(LedgerStatus.OPEN,len(events),"missing required stages: "+",".join(missing))
    return LedgerResult(LedgerStatus.COMPLETE,len(events),"continuous ordered lineage")
