# KX-003 Worker Boundary Adversarial Plan

Required attacks include:

1. short or ambiguous source identity;
2. source substitution after pinning;
3. network escape;
4. host filesystem escape;
5. secret exposure;
6. privileged operation;
7. stale worker reuse;
8. worker identity spoofing;
9. forged stdout/stderr or exit status;
10. evidence reuse against a different source.

No attack may be classified PASS merely because the reference worker returned BLOCKED. Actual isolation remains NOT_MEASURED until a real worker is executed and independently tested.
