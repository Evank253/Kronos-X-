import pytest
from kronos_x.models import SourcePin
from kronos_x.execution.source_validation import validate_source_pin

def test_full_commit_identity_is_required():
    validate_source_pin(SourcePin("repo","a"*40))
    validate_source_pin(SourcePin("repo","b"*64))

def test_short_commit_is_rejected():
    with pytest.raises(ValueError):
        validate_source_pin(SourcePin("repo","6167544"))
