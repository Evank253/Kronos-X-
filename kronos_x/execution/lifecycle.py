from dataclasses import dataclass
from enum import Enum

class WorkerLifecycle(str, Enum):
    CREATED="CREATED"; STARTED="STARTED"; RUNNING="RUNNING"; TIMED_OUT="TIMED_OUT"; FAILED="FAILED"; COMPLETED="COMPLETED"; CLEANUP_STARTED="CLEANUP_STARTED"; DESTROYED="DESTROYED"; CLEANUP_FAILED="CLEANUP_FAILED"

@dataclass(frozen=True, slots=True)
class LifecycleEvent:
    execution_id:str
    state:WorkerLifecycle
    timestamp:str
    worker_identity:str
    detail:str=""

@dataclass(frozen=True, slots=True)
class CleanupResult:
    execution_id:str
    worker_identity:str
    destroyed:bool
    residual_processes:int
    residual_mounts:int
    detail:str=""
