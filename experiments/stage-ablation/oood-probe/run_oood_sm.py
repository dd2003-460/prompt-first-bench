import sys, os, json, time
for _p in ["/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation",
           "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts",
           "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/A-eval-infra/scripts"]:
    sys.path.insert(0, _p)
os.chdir("/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation")
from s5_state_machine import DecompStateMachine, ObjectiveConfig
q = open("/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/questions/Q10-oood-cyclone.txt").read().strip()
sm = DecompStateMachine(q, qid="oood-cyclone", cfg=ObjectiveConfig(max_nodes=40, max_depth=4))
t0 = time.time()
res = sm.run()
out = {"qid": "oood-cyclone", "wall_sec": round(time.time()-t0, 1),
       "final_state": res.final_state, "n_nodes": len(res.nodes),
       "nodes": [{"id": n.id, "claim": n.claim, "level": n.level, "source": n.source,
                  "status": n.status, "edge_type": n.edge_type, "parent_ids": n.parent_ids}
                 for n in res.nodes],
       "rounds_log": res.rounds_log[-20:]}
json.dump(out, open("/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/sm-arm.json", "w"), ensure_ascii=False, indent=1)
print("SM arm done:", out["n_nodes"], "nodes,", out["wall_sec"], "s, state =", out["final_state"])
