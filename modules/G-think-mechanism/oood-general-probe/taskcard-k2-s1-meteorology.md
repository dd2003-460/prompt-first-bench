# 任务卡 K2 — S1 剥离版 SM 跑气象域（40 节点，无检索口径）
> 纯执行 sub。本卡是唯一指令来源。零改动生产文件。git commit 由你做。
> 前置: K1 已完成（`oood-probe/s1/` 副本存在且导入冒烟过）。若不存在，立即停止并汇报"K1 未完成"。

## 背景（只需知道，不需读文件）
- S0 原版 SM 已在气象域跑完（tree-only, 40 节点），但其 webllm 检索通道中途崩溃 → 实际是无检索态
- 为公平，本臂**统一关 webllm**（monkeypatch，不碰源码）
- S1 = 剥离域味的 SM 副本（s1/ 目录），控制流与 S0 完全一致，仅 prompt 域中性化

## S1 写驱动 `oood-probe/run_s1_sm.py`
```python
import sys, os, json, time
S1 = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/s1"
AB = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation"
# s1 副本必须最先解析（shadow 生产 s5_state_machine/prompts）
sys.path.insert(0, S1)
sys.path.insert(0, AB)
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts")
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/A-eval-infra/scripts")
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
```
**跑前自检**: 先 `python3 -c "import ast; ast.parse(open('oood-probe/run_s1_sm.py').read())"` 确认语法；再干跑 import 段（把 `sm.run()` 之后的行注释掉跑一次）确认两个 assert 都过、`WRONG` 不出现，再正式跑。

## S2 后台跑（防 turn 结束被回收）
```bash
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation
setsid nohup python3 oood-probe/run_s1_sm.py > oood-probe/s1-sm-arm.log 2>&1 &
echo $! > oood-probe/s1-sm-arm.pid
```
然后 process_manage wait 轮询（每次 300s），直到日志出现 `S1 arm done:` 或 `Traceback`。
**总时长预期 ~35-45min**（S0 同口径 36min）。超 60min 停并报部分状态（日志尾部 20 行 + 已建节点数）。

## S3 验证
1. `s1-sm-arm.json` 存在且 `n_nodes`>0、`arm`=="S1-stripped"
2. 日志 grep `WRONG SM\|WRONG prompts` = 0（确认跑的是 s1 副本）
3. 日志 grep `WEBLLM` = 0（确认 webllm 已关）
4. 节点 status 分布（verified/degraded/pending 各几个）

## S4 commit + 汇报
```bash
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech && git add experiments/stage-ablation/oood-probe/ && git commit -m "exp: K2 S1 剥离版 SM 气象 40节点 (无检索口径, 与 S0 对齐)"
```
汇报 ≤5 行: n_nodes/wall/state + status 分布 + 跑的是 s1 副本的证据(日志行) + json 路径 + commit hash。

## 边界
- 不碰生产 s5_state_machine.py / prompts.py / research_hook.py（monkeypatch 只在驱动进程内）
- 不碰 run_q9_gated.py / checkpoints/ 下 gated 产物
- 不做记分（P2 同款记分由后续任务做）
