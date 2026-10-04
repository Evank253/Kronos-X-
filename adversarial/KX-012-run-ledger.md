# KX-012 Run Ledger / Lineage Boundary

Every significant laboratory action must remain attributable to one run and one ordered predecessor chain.

Attack paths:
- missing stage;
- reordered events;
- duplicate event identity;
- orphan event from another run;
- broken predecessor chain;
- empty ledger.

Expected behavior: invalid or incomplete lineage is never silently treated as a complete experiment.
