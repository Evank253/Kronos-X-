from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class FindingType(str,Enum):
 BUG="BUG"; REGRESSION="REGRESSION"; CONFIGURATION_ERROR="CONFIGURATION_ERROR"; ENVIRONMENT_FAILURE="ENVIRONMENT_FAILURE"; DEPENDENCY_FAILURE="DEPENDENCY_FAILURE"; TEST_DEFECT="TEST_DEFECT"; PROVENANCE_FAILURE="PROVENANCE_FAILURE"; SECURITY_FAILURE="SECURITY_FAILURE"; PERFORMANCE_BOTTLENECK="PERFORMANCE_BOTTLENECK"; ARCHITECTURAL_LIMITATION="ARCHITECTURAL_LIMITATION"; UNRESOLVED="UNRESOLVED"

@dataclass(frozen=True,slots=True)
class FindingRecord:
 finding_id:str; run_id:str; finding_type:FindingType; description:str; evidence_ids:tuple[str,...]=(); status:str="OPEN"

@dataclass(frozen=True,slots=True)
class RepairRecord:
 repair_id:str; parent_commit:str; finding_id:str; proposed_commit:Optional[str]=None; files_changed:tuple[str,...]=(); targeted_test_ids:tuple[str,...]=(); status:str="PROPOSED"

@dataclass(frozen=True,slots=True)
class ReviewRecord:
 review_id:str; subject_id:str; reviewer_identity:str; evidence_ids:tuple[str,...]=(); decision:str="NOT_MEASURED"; independent:bool=True

@dataclass(frozen=True,slots=True)
class ReproductionRecord:
 reproduction_id:str; source_run_id:str; comparison_run_id:str; status:str="NOT_MEASURED"; differences:tuple[str,...]=()

@dataclass(frozen=True,slots=True)
class QualificationReviewRecord:
 review_id:str; subject_id:str; evidence_ids:tuple[str,...]=(); decision:str="NOT_CLAIMED"; human_ratification_id:Optional[str]=None

@dataclass(frozen=True,slots=True)
class RunLedgerEntry:
 sequence:int; run_id:str; event:str; status:str; source_commit:str; evidence_id:Optional[str]=None; metadata:dict=field(default_factory=dict)
