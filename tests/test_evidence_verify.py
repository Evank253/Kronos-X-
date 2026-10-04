from kronos_x.models import EvidenceManifest, EvidenceStatus
from kronos_x.evidence.verify import verify_manifest, verify_observation_bytes
from kronos_x.evidence.manifest import manifest_sha256
from kronos_x.provenance.hashing import sha256_bytes

def test_manifest_hash_verifies_exact_canonical_form():
    m=EvidenceManifest('EV-1','RUN-1','EX-1','a'*40,'b'*64,EvidenceStatus.OBSERVED)
    assert verify_manifest(m,manifest_sha256(m))

def test_observation_hash_detects_mutation():
    expected=sha256_bytes(b'original')
    assert not verify_observation_bytes(b'mutated',expected)
