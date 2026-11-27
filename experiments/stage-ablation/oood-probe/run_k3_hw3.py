import sys, os, json, time
S1 = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/s1"
AB = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation"
sys.path.insert(0, S1)          # s1 副本最先解析
sys.path.insert(0, AB)
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts")
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/A-eval-infra/scripts")
os.chdir(AB)
import research_hook
research_hook._WEBLLM_BROKEN["flag"] = True   # 三臂统一关 webllm（与 S0/K2 口径一致）
from ablation_harness import call_llm
q = open(f"{AB}/questions/Q9-agi-pure.txt").read().strip()
log = []

# ---- 臂 B: 裸基线单发（同 S0 气象基线 prompt 模板，max_tokens=8000）----
t0 = time.time()
prompt = "直接回答下面的问题。要求：识别所有贡献因子，每个因子给量化依据（数值/公式/可检索事实），标 conf，给出最优路径分解。\n\n【问题】\n" + q
out_b, _ = call_llm(prompt, max_tokens=8000, temperature=0.7, retries=2)
open(f"{AB}/oood-probe/k3-baseline-hw.txt", "w").write(out_b or "")
log.append({"arm": "B", "chars": len(out_b or ""), "sec": round(time.time()-t0, 1)})
print("B arm done:", log[-1], flush=True)

# ---- 臂 S0: 生产 SM（注意: 此刻 sys.path[0]=S1, 需临时挪到 S0）----
def run_sm(tag, path0):
    sp = [p for p in sys.path if p != S1]
    sys.path[:] = [path0] + sp
    import importlib
    for m in ("s5_state_machine", "prompts"):
        if m in sys.modules: del sys.modules[m]
    import s5_state_machine, prompts
    print(f"[{tag}] SM={s5_state_machine.__file__}", flush=True)
    from s5_state_machine import DecompStateMachine, ObjectiveConfig
    sm = DecompStateMachine(q, qid=f"k3-{tag}", cfg=ObjectiveConfig(max_nodes=40, max_depth=4))
    t0 = time.time()
    res = sm.run()
    out = {"qid": f"k3-{tag}", "arm": tag, "wall_sec": round(time.time()-t0, 1),
           "final_state": res.final_state, "n_nodes": len(res.nodes),
           "nodes": [{"id": n.id, "claim": n.claim, "level": n.level, "source": n.source,
                      "status": n.status, "edge_type": n.edge_type, "parent_ids": n.parent_ids}
                     for n in res.nodes],
           "rounds_log": res.rounds_log[-20:]}
    fn = f"{AB}/oood-probe/k3-{tag.lower()}-hw.json"
    json.dump(out, open(fn, "w"), ensure_ascii=False, indent=1)
    print(f"{tag} arm done:", out["n_nodes"], "nodes,", out["wall_sec"], "s, state =", out["final_state"], flush=True)
    return out

run_sm("S0", AB)          # 生产核
run_sm("S1", S1)          # 剥离核
json.dump(log, open(f"{AB}/oood-probe/k3-baseline-hw.json", "w"))
print("ALL K3 DONE", flush=True)
