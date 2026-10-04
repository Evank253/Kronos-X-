# KX-010 Repair / Provenance Boundary

An automated repair is subordinate to its originating finding and cannot establish its own correctness.

Attack paths:
- repair detached from its finding;
- repair based on the wrong parent commit;
- repair without patch identity;
- repair producer acts as reviewer;
- repair modifies unrelated governance/authority files;
- passing repair tests treated as qualification.

Expected behavior: reject broken lineage, flag out-of-scope changes for review, require independent review, and never promote repair success into qualification or authority.
