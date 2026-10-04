import re
from ..models import SourcePin

_SHA40=re.compile(r"^[0-9a-fA-F]{40}$")
_SHA64=re.compile(r"^[0-9a-fA-F]{64}$")

def validate_source_pin(source: SourcePin) -> None:
    if not source.repository.strip():
        raise ValueError("repository is required")
    if not (_SHA40.fullmatch(source.commit_sha) or _SHA64.fullmatch(source.commit_sha)):
        raise ValueError("commit_sha must be a full SHA-1 or SHA-256 identity")
    if source.tree_sha is not None and not (_SHA40.fullmatch(source.tree_sha) or _SHA64.fullmatch(source.tree_sha)):
        raise ValueError("tree_sha must be a full SHA-1 or SHA-256 identity")
