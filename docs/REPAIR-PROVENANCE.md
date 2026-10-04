# Repair and Provenance Boundary

Every automated repair must identify its originating finding, parent source state, patch identity, changed paths, producer, and independent reviewer.

A repair that changes paths outside its declared scope is not silently accepted; it becomes a review finding. A repair producer cannot validate its own repair.

Passing repair tests establish only measured test results. They do not establish qualification or human authority.
