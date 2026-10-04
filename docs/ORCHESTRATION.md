# Kronos-X Orchestration

The orchestrator is the control-plane implementation of the laboratory loop. It records stage outcomes in the Run Ledger and preserves explicit non-positive states when a capability is unavailable.

The orchestrator does not qualify results, grant authority, or manufacture evidence.

A future worker may replace a BLOCKED execution stage only through a new measured execution record with its own provenance.
