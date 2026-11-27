#!/usr/bin/env python3
"""对已归档的 SM 树重跑 synth（SM_SYNTH_FULL=1 放开压缩）。
用法: python3 synth_rerun.py <archived_run.json> <qid> <out_prefix>
不重跑 SM 状态机，只用原始节点树 + 放开后的 synth。
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["SM_SYNTH_FULL"] = "1"
from s5_state_machine import NodeRecord, synthesize_answer

run_path, qid, out_prefix = sys.argv[1], sys.argv[2], sys.argv[3]
d = json.load(open(run_path))
nodes = [NodeRecord(**{k: n.get(k) for k in
         ('id','claim','level','source','status','evidence','corrected_claim',
          'rework_count','parent_ids','objective','edge_type','search_query','retrieval_sources')
         if k in n}) for n in d['nodes']]
print(f"[rerun] {len(nodes)} nodes, qid={qid}, SM_SYNTH_FULL=1", flush=True)
t0 = time.time()
res = synthesize_answer(d['question'], nodes, qid)
out = {
    "qid": qid, "n_nodes": len(nodes), "final_state": d.get('final_state'),
    "answer": res["answer"], "judge": res.get("judge"),
    "coverage": res.get("coverage"), "depth_score": res.get("depth"),
    "source_run": run_path, "synth_full": True,
    "elapsed_s": round(time.time() - t0, 1),
}
path = f"{out_prefix}-synth-full.json"
json.dump(out, open(path, "w"), ensure_ascii=False, indent=1)
print(f"[rerun] DONE → {path} | coverage={res.get('coverage')} depth={res.get('depth')} "
      f"answer_len={len(res['answer'] or '')} {time.time()-t0:.0f}s", flush=True)
