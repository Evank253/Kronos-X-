# Status Semantics

`PASS` is not a universal state in Kronos-X. Stages must distinguish observation, verification, qualification, and authority.

`NOT_MEASURED`: the experiment has not been performed or measurement is unavailable.

`BLOCKED`: a required boundary or dependency prevented execution.

`INCONCLUSIVE`: execution occurred but did not support a determinate conclusion.

`OBSERVED`: an observation was captured.

`VERIFIED`: the defined verification relation was established.

`UNRESOLVED`: conflicting or insufficient evidence remains.

`NOT_CLAIMED`: no qualification or stronger conclusion is being asserted.

No status in this list grants human authority.
