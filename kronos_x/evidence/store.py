from dataclasses import dataclass
from pathlib import Path
from ..provenance.hashing import sha256_bytes

@dataclass(frozen=True, slots=True)
class StoredEvidence:
    sha256:str
    path:str

class EvidenceStore:
    """Content-addressed reference store. Qualification is deliberately outside this class."""
    def __init__(self, root:str|Path): self.root=Path(root); self.root.mkdir(parents=True,exist_ok=True)
    def put(self,data:bytes)->StoredEvidence:
        digest=sha256_bytes(data); p=self.root/digest; p.write_bytes(data); return StoredEvidence(digest,str(p))
    def get(self,digest:str)->bytes:
        data=(self.root/digest).read_bytes()
        if sha256_bytes(data)!=digest: raise ValueError("evidence integrity mismatch")
        return data
