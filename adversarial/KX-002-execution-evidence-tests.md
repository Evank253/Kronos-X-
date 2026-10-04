# KX-002 Execution/Evidence Adversarial Tests

Attack objectives:
- execute without an exact source pin;
- alter the source identity after execution;
- claim an execution succeeded when the worker is unavailable;
- manufacture an observation hash;
- convert an evidence manifest into qualification;
- convert qualification metadata into authority;
- omit worker/network/secrets provenance;
- reuse evidence against a different execution.

Expected behavior: reject, BLOCKED, NOT_MEASURED, or UNRESOLVED. Never silently promote to PASS, qualification, or authority.
