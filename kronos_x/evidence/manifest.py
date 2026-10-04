import json
from ..models.evidence import EvidenceManifest
from ..provenance.hashing import sha256_bytes

def canonical_manifest_bytes(manifest: EvidenceManifest) -> bytes:
    payload = {
        "evidence_id": manifest.evidence_id,
        "run_id": manifest.run_id,
        "execution_id": manifest.execution_id,
        "source_commit": manifest.source_commit,
        "observation_sha256": manifest.observation_sha256,
        "status": manifest.status.value,
        "qualification": manifest.qualification,
        "authority_granted": manifest.authority_granted,
        "schema_version": manifest.schema_version,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()

def manifest_sha256(manifest: EvidenceManifest) -> str:
    return sha256_bytes(canonical_manifest_bytes(manifest))
