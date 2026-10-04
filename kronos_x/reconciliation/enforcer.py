from dataclasses import dataclass
from enum import Enum
from typing import Optional

class ReconciliationStatus(str, Enum):
    AGREEMENT='AGREEMENT'
    MISMATCH='MISMATCH'
    INCONCLUSIVE='INCONCLUSIVE'
    NOT_MEASURED='NOT_MEASURED'

@dataclass(frozen=True, slots=True)
class ReconciliationInput:
    index_repository: str
    index_commit_sha: Optional[str]
    execution_repository: str
    execution_commit_sha: Optional[str]

@dataclass(frozen=True, slots=True)
class ReconciliationResult:
    status: ReconciliationStatus
    qualification_path_allowed: bool
    reason: str

def reconcile(i: ReconciliationInput) -> ReconciliationResult:
    if not i.index_commit_sha or not i.execution_commit_sha:
        return ReconciliationResult(ReconciliationStatus.NOT_MEASURED, False, 'exact source identity missing')
    if i.index_repository != i.execution_repository or i.index_commit_sha != i.execution_commit_sha:
        return ReconciliationResult(ReconciliationStatus.MISMATCH, False, 'index and execution source identities disagree')
    return ReconciliationResult(ReconciliationStatus.AGREEMENT, True, 'source identities agree')
