from ..models import EvidenceManifest
from ..provenance.hashing import sha256_bytes
from .manifest import manifest_sha256

def verify_manifest(manifest: EvidenceManifest, expected_sha256: str) -> bool:
    return manifest_sha256(manifest) == expected_sha256

def verify_observation_bytes(observation: bytes, expected_sha256: str) -> bool:
    return sha256_bytes(observation) == expected_sha256
