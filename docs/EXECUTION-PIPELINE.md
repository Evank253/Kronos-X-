# Execution Pipeline

The pipeline binds a RunRecord to an execution adapter and then creates an EvidenceManifest from the resulting execution record.

The adapter is the boundary where an independently controlled worker will eventually be connected. The current boundary implementation remains BLOCKED.

The pipeline cannot convert BLOCKED or NOT_MEASURED into a positive experimental conclusion.
