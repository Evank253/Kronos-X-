# KX-009 Independent Review Boundary

The producer of a result cannot independently validate that result.

Attack paths:
- producer acts as reviewer;
- submitter acts as reviewer;
- reviewer receives only a self-authored summary;
- non-designated reviewer issues the decision;
- review decision is detached from the actual evidence.

Expected behavior: reject non-independent reviewer identity, require actual evidence bytes, bind the decision to the reviewed subject and evidence hash, and keep authority external.
