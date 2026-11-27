# 任务卡 K3 — 硬件域内三臂（S0/S1/B × 40 节点，无检索口径）
> 纯执行 sub。本卡是唯一指令来源。零改动生产文件。git commit 由你做。
> 前置: K1 完成（s1/ 副本存在）+ K2 完成（s1-sm-arm.json 存在）。缺一即停并汇报缺哪项。
> 目的: 2×2 矩阵的域内列——同口径(无检索)下 S0 vs S1 vs B 在硬件域的表现，判"域味=功能配置还是负资产"。

## 题面
`questions/Q9-agi-pure.txt`（硬件域原题，与历史 run 同源，保证域内可比）。

## S1 写驱动 `oood-probe/run_k3_hw3.py`（三臂串行，一次跑完）
```python
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
```
**跑前自检（必须）**:
1. `ast.parse` 语法过
2. 干跑 import 段验证两次 shadow 切换: 先确认 `sys.path[0]=S1` 时 import 得到 s1 副本; 再模拟 run_sm("S0", AB) 的 path 重排后 import 得到生产版（打印 `__file__` 核对，不跑 sm.run）
3. 确认 `k3-*.json` 文件名不与现有文件冲突（ls oood-probe/）

## S2 后台跑
```bash
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation
setsid nohup python3 oood-probe/run_k3_hw3.py > oood-probe/k3-hw3.log 2>&1 &
echo $! > oood-probe/k3-hw3.pid
```
process_manage wait 轮询（300s/次）直到日志出现 `ALL K3 DONE` 或 `Traceback`。
**预期 ~80-110min**（B ~1min + S0 ~36min + S1 ~36min）。超 150min 停并报进度（哪个臂完成 + 日志尾 20 行）。
**中断恢复**: 若某臂 Traceback，看日志定位; S0/S1 臂失败可单独重跑（把 run_sm 调用改成只跑失败臂的新驱动），B 臂失败重跑 B 段即可。已完成的臂产物保留不覆盖。

## S3 验证
1. 三个产物存在: `k3-baseline-hw.txt` + `k3-s0-hw.json` + `k3-s1-hw.json`
2. 日志 grep `[S0] SM=` 行指向生产路径、`[S1] SM=` 行指向 s1/ 路径（shadow 切换正确性的铁证）
3. 日志 grep `WEBLLM` = 0
4. 每臂 n_nodes>0 + status 分布

## S4 commit + 汇报
```bash
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech && git add experiments/stage-ablation/oood-probe/ && git commit -m "exp: K3 硬件域内三臂 S0/S1/B 40节点 (无检索口径, 2x2 域内列)"
```
汇报 ≤6 行: 三臂 n_nodes/wall/state + SM 路径证据(两行日志) + 三产物路径 + commit hash + 偏差。

## 边界
- 生产文件零改动（shadow 只在进程内 sys.path 操作）
- 不碰 run_q9_gated.py / 其 checkpoints（qid 不同: k3-s0/k3-s1, checkpoint 目录名不同, 不冲突）
- 不做记分（K4 判断-Lead 做）
