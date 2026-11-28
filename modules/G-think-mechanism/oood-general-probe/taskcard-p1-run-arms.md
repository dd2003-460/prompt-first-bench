# P1 任务卡 — OOD 探针双臂执行（SM 臂 + 裸基线臂）
> 你是纯执行 sub。本卡是唯一指令来源，不要读其他规划文件。产出 = 两臂 run 产物 + 1 行摘要。

## 环境
- workdir: /Users/a1-6/Desktop/workspace/pfb-thinkmech
- SM 模块: experiments/stage-ablation/s5_state_machine.py（class DecompStateMachine / ObjectiveConfig）
- LLM: 本地 8787（27b），经 experiments/stage-ablation/ablation_harness.py 的 call_llm 调用
- 题面: experiments/stage-ablation/questions/Q10-oood-cyclone.txt（热带气旋登陆减弱，气象域——本 SM 从未测过的域）
- 输出目录: experiments/stage-ablation/oood-probe/（mkdir -p 自建）

## 步骤 0（先验接口，~40 行，防返工）
- `sed -n '1218,1260p' experiments/stage-ablation/s5_state_machine.py` 确认 run() 开头行为
- `sed -n '1590,1598p' experiments/stage-ablation/s5_state_machine.py` 确认 run() 结尾 return 什么
- 确认 `from ablation_harness import call_llm` 签名（call_llm(prompt, max_tokens=..., temperature=..., retries=...)）

## 步骤 1 — SM 臂（生产核，零改动）
写 oood-probe/run_oood_sm.py（write_file 落盘，不手打进输出流）：
```python
import sys, os, json, time
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation")
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
```
后台跑：`nohup python3 run_oood_sm.py > oood-probe/sm-arm.log 2>&1 &`，记下 PID。
预期 15-40min（40 节点预算）。若 >45min 未完：kill，读 checkpoints/ 最新 ckpt 把 nodes 抢救进 sm-arm.json，标 "partial": true。

## 步骤 2 — 裸基线臂（单发，无分解无核验）
写 oood-probe/run_baseline.py：
```python
import sys, time
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation")
from ablation_harness import call_llm
q = open("/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/questions/Q10-oood-cyclone.txt").read().strip()
prompt = "直接回答下面的问题。要求：识别所有物理机制，每个机制给量化影响（数值/公式），指出主导机制，列出黑盒表。\n\n【问题】\n" + q
t0 = time.time()
out, _ = call_llm(prompt, max_tokens=8000, temperature=0.7, retries=2)
open("/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/baseline-arm.txt", "w").write(out or "")
print("baseline done:", len(out or ""), "chars,", round(time.time()-t0, 1), "s")
```
前台跑（~2-5min）。

## 步骤 3 — commit
`git add experiments/stage-ablation/oood-probe/ && git commit -m "exp: OOD general probe 双臂产物 (SM 40节点气象域 + 裸基线单发)"`

## 边界（硬）
- 生产代码（s5_state_machine.py / s5_pipeline.py / prompts.py / ablation_harness.py）零改动
- 不碰 run_q9_gated.py 进程（PID 95936）及 checkpoints/ 里 q9-agi-gated 相关文件
- 脚本一律 write_file 落盘，输出流只放命令 + 1 行摘要

## 回执
1 行：`SM臂: N节点/Ms/状态X; 基线臂: K字符; commit: <hash>`（SM 臂超时则标 partial）
