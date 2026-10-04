# Worker Lifecycle and Evidence Capture

A real worker must expose a lifecycle from creation through destruction. Cleanup is an independently observable property, not an assumption.

Required lifecycle:
CREATED → STARTED → RUNNING → COMPLETED/FAILED/TIMED_OUT → CLEANUP_STARTED → DESTROYED

A cleanup failure is itself evidence and must produce CLEANUP_FAILED; it must never be silently converted to success.

Raw stdout/stderr are captured before evidence hashing. Hashes identify captured bytes; they do not prove that the worker enforced isolation.

The reference lifecycle is a state model only and remains NOT_MEASURED.
