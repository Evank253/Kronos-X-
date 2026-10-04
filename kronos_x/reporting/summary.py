def summarize(run):
    return {"run_id":run.run_id,"status":run.status.value,"source_commit":run.source.commit_sha,"stages":[{"name":s.name,"status":s.status.value,"reason":s.reason} for s in run.stages]}
