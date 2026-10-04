from .lifecycle import WorkerLifecycle, LifecycleEvent, CleanupResult

class ReferenceLifecycle:
    """Lifecycle state model only; no host process control is performed."""
    def events(self, execution_id, worker_identity="REFERENCE_NOT_CONNECTED"):
        return (LifecycleEvent(execution_id,WorkerLifecycle.CREATED,"NOT_MEASURED",worker_identity,"worker not connected"),)

    def cleanup(self, execution_id, worker_identity="REFERENCE_NOT_CONNECTED"):
        return CleanupResult(execution_id,worker_identity,False,0,0,"NOT_MEASURED: no worker exists to destroy")
