from typing import Protocol

class IndexMachine(Protocol):
    def index(self, repository:str, commit_sha:str): ...
    def lineage(self, repository:str, commit_sha:str): ...

# Kronos-X depends on this interface but does not own or rewrite Index Machine history.
