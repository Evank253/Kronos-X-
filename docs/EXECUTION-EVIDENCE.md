# Execution and Evidence Boundary

Kronos-X binds execution records to an exact SourcePin. Execution and evidence are separate records so that an observation can be traced to the execution that produced it.

The EvidenceManifest records the observation identity and explicitly carries qualification NOT_CLAIMED and authority_granted=false by default.

The current safe runner remains BLOCKED because no independently controlled arbitrary-code worker is connected.

A future worker must produce new execution evidence; it must not retrofit a historical record.
