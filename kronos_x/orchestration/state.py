from dataclasses import dataclass
from ..models.records import EvidenceStatus, RunRecord, SourcePin, StageRecord

ORDER=("DISCOVER","INDEX","PIN","ISOLATE","BUILD","BASELINE","TEST","BENCHMARK","EVALUATE","DIAGNOSE","REPAIR","RE-INDEX","RETEST","INDEPENDENT_REVIEW","FULL_E2E","REPRODUCE","RECONCILE","SEAL_EVIDENCE","REPORT")

@dataclass(frozen=True, slots=True)
class LaboratoryState:
    run: RunRecord
    current_stage: str="DISCOVER"

    def stage(self, name:str)->StageRecord:
        if name not in ORDER: raise ValueError(f"unknown stage: {name}")
        return next((s for s in self.run.stages if s.name==name), StageRecord(name,name,EvidenceStatus.NOT_MEASURED))

    def advance(self, name:str, status:EvidenceStatus, reason=None):
        if name not in ORDER: raise ValueError(f"unknown stage: {name}")
        if status==EvidenceStatus.OBSERVED and not reason and name in {"ISOLATE","RECONCILE"}:
            pass
        updated=list(self.run.stages)
        rec=StageRecord(name,name,status,reason)
        updated=[s for s in updated if s.name!=name]+[rec]
        return LaboratoryState(RunRecord(self.run.run_id,self.run.source,self.run.status,tuple(updated)),name)

def new_run(run_id:str, source:SourcePin)->LaboratoryState:
    return LaboratoryState(RunRecord(run_id,source))
