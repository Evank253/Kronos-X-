from dataclasses import dataclass
from enum import Enum

class ReproducibilityStatus(str, Enum):
    REPRODUCIBLE="REPRODUCIBLE"
    DIFFERENT_RESULT="DIFFERENT_RESULT"
    NONDETERMINISTIC="NONDETERMINISTIC"
    NOT_REPRODUCED="NOT_REPRODUCED"

class ReproducibilityBoundaryError(PermissionError):
    pass

@dataclass(frozen=True, slots=True)
class ExperimentIdentity:
    source_commit: str
    tree_hash: str
    environment_hash: str
    dependency_hash: str
    command: str
    input_hash: str

@dataclass(frozen=True, slots=True)
class RunObservation:
    identity: ExperimentIdentity
    result_hash: str

@dataclass(frozen=True, slots=True)
class ReproducibilityResult:
    status: ReproducibilityStatus
    same_identity: bool
    same_result: bool
    reason: str

def compare_runs(baseline: RunObservation, rerun: RunObservation) -> ReproducibilityResult:
    same_identity = baseline.identity == rerun.identity
    if not same_identity:
        return ReproducibilityResult(ReproducibilityStatus.NOT_REPRODUCED,False,False,"source, environment, dependency, command, or input identity differs")
    if baseline.result_hash == rerun.result_hash:
        return ReproducibilityResult(ReproducibilityStatus.REPRODUCIBLE,True,True,"exact experimental identity produced the same result")
    return ReproducibilityResult(ReproducibilityStatus.NONDETERMINISTIC,True,False,"exact experimental identity produced a different result; nondeterminism must be investigated")
