"""KX-012.1 append-only, tamper-evident run ledger."""
from dataclasses import dataclass
from enum import Enum
import hashlib, json

class LedgerBoundaryError(ValueError): pass
class LedgerStatus(str, Enum):
    OPEN="OPEN"; COMPLETE="COMPLETE"; INVALID="INVALID"

@dataclass(frozen=True, slots=True)
class LedgerEvent:
    sequence:int; event_id:str; run_id:str; stage:str; predecessor_event_id:str|None; event_hash:str=""
    def canonical_bytes(self)->bytes:
        return json.dumps({"sequence":self.sequence,"event_id":self.event_id,"run_id":self.run_id,"stage":self.stage,"predecessor_event_id":self.predecessor_event_id},sort_keys=True,separators=(",",":")).encode()
    def computed_hash(self)->str: return hashlib.sha256(self.canonical_bytes()).hexdigest()
    def with_hash(self): return LedgerEvent(self.sequence,self.event_id,self.run_id,self.stage,self.predecessor_event_id,self.computed_hash())

@dataclass(frozen=True, slots=True)
class LedgerResult:
    status:LedgerStatus; event_count:int; reason:str

REQUIRED_STAGES=("DISCOVER","INDEX","PIN","ISOLATE","BUILD","BASELINE","TEST","BENCHMARK","EVALUATE","DIAGNOSE","REPAIR","RE-INDEX","RETEST","INDEPENDENT_REVIEW","FULL_E2E","REPRODUCE","RECONCILE","SEAL_EVIDENCE","REPORT")

class RunLedger:
    __slots__=("_run_id","_events")
    def __init__(self,run_id):
        if not run_id: raise LedgerBoundaryError("run_id is required")
        object.__setattr__(self,"_run_id",run_id); object.__setattr__(self,"_events",())
    @property
    def run_id(self): return self._run_id
    @property
    def events(self): return self._events
    def append(self,event_id,stage):
        if not event_id or not stage: raise LedgerBoundaryError("event_id and stage are required")
        if any(e.event_id==event_id for e in self._events): raise LedgerBoundaryError("event_id already exists")
        n=len(self._events)+1; pred=self._events[-1].event_id if self._events else None
        event=LedgerEvent(n,event_id,self._run_id,stage,pred).with_hash()
        new=object.__new__(RunLedger); object.__setattr__(new,"_run_id",self._run_id); object.__setattr__(new,"_events",self._events+(event,))
        return new
    def verify(self,required_stages=REQUIRED_STAGES): return validate_ledger(self._events,self._run_id,required_stages)

def validate_ledger(events,run_id,required_stages=REQUIRED_STAGES):
    if not events: return LedgerResult(LedgerStatus.INVALID,0,"ledger is empty")
    seen=set()
    for expected,event in enumerate(events,1):
        if event.run_id!=run_id: return LedgerResult(LedgerStatus.INVALID,len(events),"orphan event belongs to another run")
        if event.sequence!=expected: return LedgerResult(LedgerStatus.INVALID,len(events),"missing or reordered sequence")
        if event.event_id in seen: return LedgerResult(LedgerStatus.INVALID,len(events),"duplicate event id")
        if (expected==1 and event.predecessor_event_id is not None) or (expected>1 and event.predecessor_event_id!=events[expected-2].event_id):
            return LedgerResult(LedgerStatus.INVALID,len(events),"broken predecessor chain")
        if event.event_hash!=event.computed_hash(): return LedgerResult(LedgerStatus.INVALID,len(events),"event hash mismatch")
        seen.add(event.event_id)
    missing=tuple(s for s in required_stages if s not in tuple(e.stage for e in events))
    if missing: return LedgerResult(LedgerStatus.OPEN,len(events),"missing required stages: "+",".join(missing))
    return LedgerResult(LedgerStatus.COMPLETE,len(events),"continuous ordered tamper-evident lineage")
