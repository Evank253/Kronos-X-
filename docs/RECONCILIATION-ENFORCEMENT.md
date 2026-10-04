# Reconciliation Enforcement

Kronos-X treats Index Machine lineage and execution identity as independently produced records.

A qualification path is permitted only when exact repository and commit identities agree. A mismatch produces `MISMATCH` and blocks the qualification path. Missing identities produce `NOT_MEASURED` and also block the path.

Reconciliation does not repair disagreements and does not grant qualification or authority. Disagreement is retained as evidence requiring review.
