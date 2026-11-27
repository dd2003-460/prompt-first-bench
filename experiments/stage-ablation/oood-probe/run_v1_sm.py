# -*- coding: utf-8 -*-
"""M3 v1 runner：与 run_s1_sm.py 相同，但指向 v1/ 目录（s1 副本 + 2 处思考触发注入）。

用法: python3 run_v1_sm.py <arm> <domain> <rep> [--max-nodes N]
  arm:    v1 | s1   （v1 → oood-probe/v1/，s1 → oood-probe/s1/）
  domain: cyclone | mining | hw
  rep:    1..N（冒烟用 smoke）
产物: oood-probe/m3-ckpt/m3-<arm>-<domain>-r<rep>.json（存在则跳过，幂等）
冒烟: --max-nodes 1（1 个父节点分解，验证 JSON 契约 + 无 crash）
"""
import sys, os, json, time, argparse

AB = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation"
HERE = os.path.join(AB, "oood-probe")
CKPT_DIR = os.path.join(HERE, "m3-ckpt")
DOMAIN_Q = {
    "cyclone": "Q10-oood-cyclone.txt",
    "mining":  "Q11-oood-trap-aluminum.txt",
    "hw":      "Q9-agi-pure.txt",
}

ap = argparse.ArgumentParser()
ap.add_argument("arm", choices=["v1", "s1"])
ap.add_argument("domain", choices=list(DOMAIN_Q))
ap.add_argument("rep")
ap.add_argument("--max-nodes", type=int, default=40)
args = ap.parse_args()

out_fn = os.path.join(CKPT_DIR, f"m3-{args.arm}-{args.domain}-r{args.rep}.json")
if os.path.exists(out_fn):
    print(f"SKIP (ckpt exists): {out_fn}", flush=True)
    sys.exit(0)

ARM_DIR = os.path.join(HERE, args.arm)
# s1/v1 副本必须最先解析（shadow 生产 s5_state_machine/prompts）
# 注意: insert(0,...) 后插的先解析，故 ARM_DIR 必须最后插入（run_s1_sm.py 同序，干跑 assert 已证）
sys.path.insert(0, AB)
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts")
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/A-eval-infra/scripts")
sys.path.insert(0, ARM_DIR)
os.chdir(AB)
import s5_state_machine, prompts
assert s5_state_machine.__file__.startswith(ARM_DIR), f"WRONG SM: {s5_state_machine.__file__}"
assert prompts.__file__.startswith(ARM_DIR), f"WRONG prompts: {prompts.__file__}"
# 统一关 webllm（与 S0/K2/K3 实际口径对齐；进程内 flag，不碰源码）
import research_hook
research_hook._WEBLLM_BROKEN["flag"] = True
from s5_state_machine import DecompStateMachine, ObjectiveConfig

qid = f"m3-{args.arm}-{args.domain}-r{args.rep}"
q = open(os.path.join(AB, "questions", DOMAIN_Q[args.domain])).read().strip()
cfg = ObjectiveConfig(max_nodes=args.max_nodes, max_depth=4)
sm = DecompStateMachine(q, qid=qid, cfg=cfg)
t0 = time.time()
res = sm.run()
nodes = [{"id": n.id, "claim": n.claim, "level": n.level, "source": n.source,
          "status": n.status, "edge_type": n.edge_type, "parent_ids": n.parent_ids}
         for n in res.nodes]
req = {"id", "claim", "level", "source", "status", "edge_type", "parent_ids"}
fields_ok = all(req <= set(n.keys()) for n in nodes)
out = {"qid": qid, "arm": args.arm, "domain": args.domain, "rep": args.rep,
       "max_nodes": args.max_nodes, "wall_sec": round(time.time() - t0, 1),
       "final_state": res.final_state, "n_nodes": len(res.nodes),
       "fields_ok": fields_ok, "nodes": nodes,
       "rounds_log": res.rounds_log[-20:]}
os.makedirs(CKPT_DIR, exist_ok=True)
json.dump(out, open(out_fn, "w"), ensure_ascii=False, indent=1)
print(f"{qid} done: {out['n_nodes']} nodes, {out['wall_sec']} s, state={out['final_state']}, fields_ok={fields_ok} -> {out_fn}", flush=True)
