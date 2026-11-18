#!/usr/bin/env python3
"""跑 pfb 状态机（带 Q2/Q4 质检门）× 3 题，结果落盘 runs-qc-compare/。"""
import json, time, os, sys
from s5_state_machine import DecompStateMachine, ObjectiveConfig
from s8b_pilot import QUESTIONS, judge
from judge_v2_depth import score_run

qid = sys.argv[1] if len(sys.argv) > 1 else "nat"
resume_from = None
max_nodes = None
verify_only = False
for k, v in enumerate(sys.argv):
    if v == "--resume" and k + 1 < len(sys.argv):
        resume_from = sys.argv[k+1]
    elif v.startswith("--resume="):
        resume_from = v.split("=", 1)[1]
    elif v == "--max-nodes" and k + 1 < len(sys.argv):
        max_nodes = int(sys.argv[k+1])
    elif v.startswith("--max-nodes="):
        max_nodes = int(v.split("=", 1)[1])
    elif v == "--verify-only":
        verify_only = True
os.makedirs("runs-qc-compare", exist_ok=True)
cfg = ObjectiveConfig()
if max_nodes:
    cfg.max_nodes = max_nodes
q = QUESTIONS[qid]

print(f"=== {qid} start ===", flush=True)
t0 = time.time()
sm = DecompStateMachine(q, qid=qid, cfg=cfg)
if resume_from:
    import json as _json
    meta, ck_nodes = sm._load_checkpoint(resume_from)
    from s5_state_machine import NodeRecord
    for nd in ck_nodes:
        sm.nodes.append(NodeRecord(**nd))
    _max_nid = max((int(str(n.id).lstrip("N")) for n in sm.nodes if str(n.id).lstrip("N").isdigit()), default=0)
    sm._nid = max(getattr(sm, "_nid", 0), _max_nid)
    sm.ckpt_round = meta.get("round", 0)
    sm.dropped_redundant = meta.get("dropped_redundant", 0)
    sm.leak_hits_total = meta.get("leak_hits_total", 0)
    sm.network_degraded = meta.get("network_degraded", False)
    sm.objective = meta.get("objective")
    sm.objective_mode = meta.get("objective_mode", "formula")
    sm.challenge_log = meta.get("challenge_log", [])
    sm.rework_events = meta.get("rework_events", [])
    sm.contradiction_events = meta.get("contradiction_events", [])
    print(f"[SM] resumed from {resume_from}: {len(sm.nodes)} nodes @ r{sm.ckpt_round}", flush=True)
result = sm.run(skip_l1=bool(resume_from), verify_only=verify_only)
wall = round(time.time() - t0, 1)

n_nodes = len(result.nodes)
n_verified = sum(1 for n in result.nodes if n.status == "verified")
n_ortho = sum(r.get("n_orthogonal_dropped", 0) for r in result.rounds_log)
n_comp = sum(r.get("n_compression_dropped", 0) for r in result.rounds_log)
n_contra = sum(r.get("contradictions_found", 0) for r in result.rounds_log)

# 综合 + 打分
table = "\n".join(
    f"{n.id}: {n.corrected_claim}  [status={n.status}]"
    for n in result.nodes if n.status in ("verified", "degraded")
)
from s5_pipeline import P4_SYNTHESIZE, _perturb
from ablation_harness import call_llm
prompt = P4_SYNTHESIZE.format(question=q, fact_table=table) + _perturb()
answer, _ = call_llm(prompt, max_tokens=8000, temperature=0.7, top_p=0.95)

j = judge(qid, answer or "")
cov = round(j.get("coverage") or 0, 3)
try:
    dv = score_run(qid, answer or "")
    depth = dv.get("overall")
except Exception:
    depth = None

out = {
    "qid": qid, "arm": "pfb-sm-qc",
    "n_nodes": n_nodes, "n_verified": n_verified,
    "verified_rate": round(n_verified / max(n_nodes, 1), 3),
    "n_orthogonal_dropped": n_ortho,
    "n_compression_dropped": n_comp,
    "n_contradictions": n_contra,
    "wall_s": wall,
    "rounds": len(result.rounds_log),
    "final_state": result.final_state,
    "coverage": cov,
    "depth_score": depth,
    "answer_len": len(answer or ""),
}
path = f"runs-qc-compare/{qid}-pfb-sm-qc.json"
with open(path, "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(f"=== {qid} done: cov={cov} depth={depth} nodes={n_nodes} ver={n_verified} ortho={n_ortho} comp={n_comp} contra={n_contra} wall={wall}s ===", flush=True)
