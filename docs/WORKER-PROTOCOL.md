# Isolated Worker Protocol

The worker boundary receives an exact source identity and explicit resource limits. The control plane must not infer successful execution from worker creation or request acceptance.

Required execution evidence includes source identity, worker identity, command, start/end timestamps, exit status, raw stdout/stderr, resource policy, network policy, secret policy, and cleanup outcome.

The protocol defines the interface; it does not establish that a particular worker is isolated. Isolation remains a separately measured property.
