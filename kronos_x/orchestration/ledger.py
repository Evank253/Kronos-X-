from dataclasses import dataclass
from ..models.lifecycle import RunLedgerEntry

@dataclass(frozen=True,slots=True)
class RunLedger:
 entries:tuple[RunLedgerEntry,...]=()

 def append(self,entry:RunLedgerEntry):
  if entry.sequence != len(self.entries)+1: raise ValueError("ledger sequence must be contiguous")
  return RunLedger(self.entries+(entry,))
