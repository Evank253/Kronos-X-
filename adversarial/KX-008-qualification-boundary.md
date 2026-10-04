# KX-008 Qualification Boundary

Qualification is not an automatic consequence of evidence, verification, or reconciliation.

Attack paths:
- OBSERVED evidence → automatic qualification
- VERIFIED evidence → automatic qualification
- reconciliation mismatch → qualification
- NOT_MEASURED → qualification
- BLOCKED → PASS/qualification
- qualification evaluator → authority
- internal consensus → qualification

Expected behavior: NOT_CLAIMED or REVIEW_REQUIRED, explicit human review where applicable, and authority remains false/external.
