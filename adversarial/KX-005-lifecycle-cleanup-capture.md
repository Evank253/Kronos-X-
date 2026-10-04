# KX-005 Lifecycle, Cleanup, and Capture

Attack and failure cases:
- worker never starts;
- worker exits unexpectedly;
- timeout leaves a process behind;
- cleanup leaves mounts/files behind;
- stale worker accepts a later execution;
- stdout/stderr are truncated or altered;
- exit status is forged;
- cleanup failure is hidden;
- lifecycle timestamps are reordered.

Expected result: explicit failure or NOT_MEASURED with evidence. Never infer destruction from a request to destroy.
