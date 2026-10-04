from dataclasses import dataclass
from ..models.records import EvidenceStatus

@dataclass(frozen=True, slots=True)
class RunnerCapabilities:
    arbitrary_code_execution: bool=False
    network: bool=False
    secrets: bool=False

class SafeNotConnectedRunner:
    capabilities=RunnerCapabilities()
    def run(self, source_pin, command):
        return {"status":EvidenceStatus.BLOCKED.value,"reason":"isolated runner not connected","source_commit":source_pin.commit_sha,"command":command}
