from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True, slots=True)
class SourceIdentity:
    repository: str
    commit_sha: str
    tree_sha: Optional[str] = None
    working_tree_state: str = "UNKNOWN"
    dependency_lock_hash: Optional[str] = None
    runtime_version: Optional[str] = None
    runner_version: Optional[str] = None
