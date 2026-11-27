import sys, os, json, time
S1 = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/s1"
AB = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation"
# s1 副本必须最先解析（shadow 生产 s5_state_machine/prompts）
# 注意: insert(0,...) 后插的先解析，故 S1 必须最后插入（任务卡原序会让 AB 抢先，干跑 assert 已证）
sys.path.insert(0, AB)
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts")
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/A-eval-infra/scripts")
sys.path.insert(0, S1)
os.chdir(AB)
import s5_state_machine, prompts
assert s5_state_machine.__file__.startswith(S1), f"WRONG SM: {s5_state_machine.__file__}"
assert prompts.__file__.startswith(S1), f"WRONG prompts: {prompts.__file__}"
# 统一关 webllm（与 S0 实际口径对齐；进程内 flag，不碰源码）
import research_hook
research_hook._WEBLLM_BROKEN["flag"] = True
from s5_state_machine import DecompStateMachine, ObjectiveConfig
q = open(f"{AB}/questions/Q10-oood-cyclone.txt").read().strip()
sm = DecompStateMachine(q, qid="oood-s1-cyclone", cfg=ObjectiveConfig(max_nodes=40, max_depth=4))
t0 = time.time()
res = sm.run()
out = {"qid": "oood-s1-cyclone", "arm": "S1-stripped", "wall_sec": round(time.time()-t0, 1),
       "final_state": res.final_state, "n_nodes": len(res.nodes),
       "nodes": [{"id": n.id, "claim": n.claim, "level": n.level, "source": n.source,
                  "status": n.status, "edge_type": n.edge_type, "parent_ids": n.parent_ids}
                 for n in res.nodes],
       "rounds_log": res.rounds_log[-20:]}
json.dump(out, open(f"{AB}/oood-probe/s1-sm-arm.json", "w"), ensure_ascii=False, indent=1)
print("S1 arm done:", out["n_nodes"], "nodes,", out["wall_sec"], "s, state =", out["final_state"])
