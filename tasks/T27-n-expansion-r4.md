# T27 · n-expansion-r4：S0/S1/S5 × Q1-Q5 补跑 r4-r6（n=30/arm）

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

## 目标
把 S0/S1/S5 三臂从 n=15 扩到 n=30（每题 6 reps），重算 per-arm mean ± sd 和 Δ。

## 执行
- harness: `experiments/stage-ablation/ablation_harness.py`，arms=S0,S1,S5，qs=Q1-Q5，reps=r4,r5,r6（共 45 runs）
- RUNS_DIR 必须指向 `runs-r293/`（不是默认 runs/——历史事故：目录错位导致 r4-r6 落到别处）
- 模型端点 http://127.0.0.1:8787/v1（本地 27b vLLM），temp 与 r1-r3 一致
- 每个 run JSON 必含 arm/qid/rep/model/output_text/sources/wall_s/tokens

## 评分
- `python3 -u score.py aggregate --runs-dir runs-r293 --multi 1`
- 注意：runs-r293/ 里 scores-v3.json 是 list 格式，score.py 已有 dict-guard（commit 7d1e806），勿删
- Q4fix-S0-Q4-r1.json 是 Q4 题面修复前的旧 run，**不计入统计**（已在 scoring.md 标注剔除）

## 验收
- [ ] 45 个新 run JSON 落盘 runs-r293/（S0/S1/S5 各 30）
- [ ] scoring.md 更新：per-arm mean/sd + Δ 表 + judge 族标注（同源 27b, conf cap 0.7）
- [ ] commit + push main

## 背景
- n=15 基线（V3 rescore @ 826d5fb）：S0=0.615 / S1=0.630 / S5=0.805，Δ(S1-S0)=+0.014
- 预期：样本翻倍后 Δ 方向不变（分解臂≈无效假设的检验）
- 跨版本口径：S1 = v1（代数判据），vN 约定见 tasks/T26-prompt-style-research.md