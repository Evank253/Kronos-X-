# Index Machine Interface

Kronos-X consumes Index Machine lineage; it does not own or rewrite historical lineage.

The interface intentionally separates `index()` and `lineage()` from execution. Reconciliation compares their independent identities.
