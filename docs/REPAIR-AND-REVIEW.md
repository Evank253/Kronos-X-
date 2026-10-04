# Repair and Independent Review

Repair flow:
FINDING → HYPOTHESIS → PROPOSED PATCH → INDEX DIFF → DEPENDENCY IMPACT → TARGETED TESTS → REGRESSION TESTS → INDEPENDENT REVIEW

A repair cannot establish its own correctness merely by passing its own tests. Reviewers receive the evidence actually produced by the execution path.

If the cause is unknown, Kronos-X records `UNRESOLVED` rather than inventing a root cause.
