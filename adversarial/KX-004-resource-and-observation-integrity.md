# KX-004 Resource and Observation Integrity

Adversarial evaluation shall test timeout enforcement, CPU limits, memory limits, output limits, cleanup after failure, raw output integrity, exit-code integrity, timestamp integrity, worker identity, and stale-process reuse.

A configured limit is not evidence that enforcement occurred. Each enforcement property requires an observation from the actual worker.
