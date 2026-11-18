# origin: ai — T53b 消融实验任务书

> CC 只跑不改。60 个 run（3 题 × 2 臂 × 10 轮），固定 seed=42，产出可发表统计量。

## 目标

固定 SM_SEED=42，跑 3 题（gpu/nat/soc）× 2 臂（formula/text）× 10 轮 = 60 个独立 run，
产出每题每臂的 coverage/depth 均值±SE + 95%CI（n=10），复现 r7 惊奇时刻（不确定性正交 L1）。

## 验收标准

1. 60 个 run 全部完成，每个 run 有 JSON 落盘（`runs-s5-sm-{qid}.json`）
2. 每个 run 有 judge 评分（coverage + depth_score），judge 用 `judge_v2_depth.py`
3. 统计汇总：每题每臂的 coverage/depth 均值±SE + 95%CI（n=10）
4. r7 复现：gpu 题 10 轮中 ≥3 轮 L1 出现独立"不确定性/随机性"维度
   （判据：L1 节点 claim 以"不确定性/随机/uncertainty/stochastic"开头，
   且 scope 说明里提到"横切/作用于其他维度"）
5. 所有 run 的 SM_SEED=42 固定，可复现
6. 统计量带口径限定：聚合口径（per-run）、tie-break 规则、judge 族
   （qwen3.8-27b ×1, non-IRR）

## 执行步骤

### 每个 run 的流程

1. 读 `tasks/T53-bus/cc-state.json`，取第一个 `done: false` 的 work_unit
2. 执行 `cmd` 字段（在 pfb 仓库根目录）
3. 等 run 完成（约 15-30 分钟，3 轮 × 每轮 5-10 分钟）
4. 确认 JSON 落盘：`experiments/stage-ablation/runs-s5-sm-{qid}.json`
   - 注意：同一题的多个 run 会覆盖同一个 JSON 文件
   - **每个 run 完成后，把 JSON 复制到 `experiments/stage-ablation/ablation-runs/{qid}_{arm}_r{NN}.json`**
5. 跑 judge：
   ```
   python3 experiments/stage-ablation/judge_v2_depth.py {qid} \
     --answer experiments/stage-ablation/ablation-runs/{qid}_{arm}_r{NN}.json \
     --output experiments/stage-ablation/ablation-runs/{qid}_{arm}_r{NN}_judge.json
   ```
6. 记录 coverage/depth 到 `experiments/stage-ablation/ablation-results.json`：
   ```json
   {
     "runs": [
       {
         "qid": "gpu", "arm": "formula", "round": 1,
         "coverage": 0.52, "depth": 0.61,
         "n_nodes": 45, "n_verified": 30, "n_degraded": 15,
         "l1_uncertainty": false,
         "run_file": "ablation-runs/gpu_formula_r01.json",
         "judge_file": "ablation-runs/gpu_formula_r01_judge.json",
         "timestamp": "2026-11-17T23:30:00+08:00"
       }
     ]
   }
   ```
7. 检查 r7 复现判据：L1 节点 claim 是否以"不确定性/随机/uncertainty/stochastic"开头
8. 更新 `cc-state.json`：把当前 work_unit 的 `done` 置 `true`
9. 写过程 note 到 `experiments/stage-ablation/ablation-notes/{qid}_{arm}_r{NN}.md`：
   ```markdown
   # {qid} {arm} r{NN}
   
   - 时间: {timestamp}
   - 节点数: {n_nodes} (verified: {n_verified}, degraded: {n_degraded})
   - coverage: {coverage}
   - depth: {depth}
   - L1 不确定性维度: {是/否}
   - 观察: {200 字以内，描述你看到的现象，不写代码、不改参数}
   ```
10. 回到步骤 1，取下一个 work_unit

### 统计汇总（所有 60 个 run 完成后）

1. 跑 `python3 experiments/stage-ablation/ablation_stats.py`
2. 输出：每题每臂的 coverage/depth 均值±SE + 95%CI（n=10）
3. 标出"特别好的轮次"（coverage 或 depth 高于均值 + 1SE 的）
4. 好轮次的 seed/参数/中间状态记录到 `experiments/stage-ablation/repro-log.md`
5. 用相同参数重跑好轮次 3 次，确认能复现（coverage 波动 < 0.05）
6. 复现失败的标 [unreproducible]，分析原因

## CC 不改的东西（硬规则）

- 不改 `s5_state_machine.py`
- 不改 `s5_pipeline.py`（prompt）
- 不改 `judge_v2_depth.py`
- 不改 `research_hook.py`
- 只跑实验、记录数据、复现好轮次
- 发现 bug → 写 `tasks/T53-bus/cc-to-lead.md` 找 Lead，不自己修

## 失败降级

- vLLM 超时 → 重试 3 次，仍失败标 [degraded] 继续
- 检索通道全挂 → `--no-verify` 模式跑（节点全 degraded），标注降级
- CC 防循环触发（8 次 block）→ 写 `tasks/T53-bus/cc-to-lead.md` 找 Lead 讨论

## 关键文件路径

| 文件 | 路径 |
|------|------|
| 状态机 | `experiments/stage-ablation/s5_state_machine.py` |
| Judge | `experiments/stage-ablation/judge_v2_depth.py` |
| 题目 | `experiments/stage-ablation/questions/{qid}.md` |
| Run 输出 | `experiments/stage-ablation/runs-s5-sm-{qid}.json` |
| 消融 run 存档 | `experiments/stage-ablation/ablation-runs/` |
| 统计结果 | `experiments/stage-ablation/ablation-results.json` |
| 过程 note | `experiments/stage-ablation/ablation-notes/` |
| CC 状态 | `tasks/T53-bus/cc-state.json` |
| CC 找 Lead | `tasks/T53-bus/cc-to-lead.md` |

## 启动命令

```bash
cd /Users/a1-6/Desktop/workspace/pfb
SM_SEED=42 python3 experiments/stage-ablation/s5_state_machine.py gpu --obj-mode=formula --synth
```

每个 run 约 15-30 分钟，60 个 run 约 15-30 小时。
