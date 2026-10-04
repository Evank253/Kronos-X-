from typing import Protocol
from ..models.execution import ExecutionRecord
from ..models.records import SourcePin

class IsolatedExecutionAdapter(Protocol):
    def execute(self, execution_id: str, run_id: str, source: SourcePin, command: tuple[str,...]) -> ExecutionRecord:
        """Execute only inside an independently controlled worker boundary."""
