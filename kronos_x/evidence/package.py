from dataclasses import dataclass
from typing import Any
import json
from ..provenance.hashing import sha256_bytes

@dataclass(frozen=True, slots=True)
class EvidencePackage:
    manifest: dict[str,Any]
    manifest_sha256: str

def seal_manifest(manifest:dict[str,Any])->EvidencePackage:
    raw=json.dumps(manifest,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    return EvidencePackage(dict(manifest),sha256_bytes(raw))
