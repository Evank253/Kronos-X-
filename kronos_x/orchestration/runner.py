from dataclasses import dataclass
from ..models.records import EvidenceStatus, RunRecord, StageRecord
from ..models.lifecycle import RunLedgerEntry
from .ledger import RunLedger

@dataclass(frozen=True, slots=True)
class OrchestrationResult:
    run: RunRecord
    ledger: RunLedger

class LaboratoryOrchestrator:
    """Evidence-first orchestration skeleton. Unavailable machinery stays explicit."""
    def __init__(self, run:RunRecord):
        self.run=run
        self.ledger=RunLedger()

    def record(self,event:str,status:EvidenceStatus,reason=None):
        seq=len(self.ledger.entries)+1
        entry=RunLedgerEntry(seq,self.run.run_id,event,status.value,self.run.source.commit_sha,metadata={"reason":reason} if reason else {})
        self.ledger=self.ledger.append(entry)
        stages=list(self.run.stages)
        stages=[s for s in stages if s.name!=event]
        stages.append(StageRecord(event,event,status,reason))
        self.run=RunRecord(self.run.run_id,self.run.source,self.run.status,tuple(stages))
        return self

    def blocked(self,event:str,reason:str):
        return self.record(event,EvidenceStatus.BLOCKED,reason)

    def not_measured(self,event:str,reason:str):
        return self.record(event,EvidenceStatus.NOT_MEASURED,reason)

    def snapshot(self):
        return OrchestrationResult(self.run,self.ledger)
