# Isolated Worker Boundary

Kronos-X does not execute arbitrary repository code in the control plane.

The reference worker establishes the required policy boundary:

- network: DENIED by default
- secrets: NONE
- host filesystem: DENIED
- privileged operations: DENIED

The reference implementation returns BLOCKED. It is not an execution result and must not be represented as one.

A future worker implementation must be separately measured for isolation, resource limits, source pinning, cleanup, network enforcement, secret denial, stdout/stderr capture, exit-code capture, and worker destruction.

Worker implementation evidence must be separate from the laboratory conclusion it helps produce.
