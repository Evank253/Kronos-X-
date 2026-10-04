# KX-007 Reconciliation Adversarial Plan

Attack surfaces:
- execution under a different commit than the indexed commit;
- repository substitution;
- missing commit identity;
- stale execution evidence;
- attempted automatic reconciliation repair;
- mismatch followed by qualification attempt.

Expected behavior: `MISMATCH` or `NOT_MEASURED`, qualification path blocked, disagreement preserved for review.
