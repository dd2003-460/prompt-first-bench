# TASK: CJ-RUBRIC-ALIGN — 判官口径对齐

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

## 目标
修改 `experiments/stage-ablation/cross_judge.py` 的 JUDGE_PROMPT，使本地 27B 判官与 arena 异源判官在 90 cell 上 M1 达到 spearman ρ≥0.6 + arm 排序一致。

## 背景（已诊断）
- 当前分歧根因 = rubric mismatch（非事实分歧）：
  - D1: 本地 "无可验证事实断言→M1=0" 把 Q4/Q5 打零（Q4 local 0.291 vs arena 0.872）
  - D2: 粒度不同（local 原子 13-40/cell vs arena 关键 4-12/cell）
  - D3: 推导是否计入未明确
- 数据：`runs/arena-judge-results.jsonl`(90行) + `scoring.md`(本地分) + `gold/Q1-Q5.md`
- 详细分解：`runs/cj-rubric-align-decomposition.md`

## 你要做的
1. **A1**: 合并两源分数 → `runs/alignment-inputs.json`（90行, 每行含 arm/q/run/local_m1/arena_m1/answer_chars）
2. **A2**: 分类 90 cell 分歧类型 → `runs/divergence-taxonomy.md`
3. **B1-B3**: 裁定 D1/D2/D3 各选哪个值 → `runs/rubric-alignment-spec.md`（含理由+计数示例）
   - 先验最优猜测: D1(豁免zero-fact)+D2(关键断言)+D3(含可复算推导)
   - 但用数据验证：对 5 个代表 cell 手工三种粒度计数，选使 Δ 最小的
4. **C1**: 按 spec 修改 cross_judge.py JUDGE_PROMPT（git diff 可见变更）
5. **C2**: 本地 :8787 重跑 90 cell → `runs/local-rerun-aligned.jsonl`
6. **C3**: 计算对齐指标 → `runs/rubric-alignment-report.md`（ρ/τ/arm-rank 表）

## 验收
- [ ] alignment-inputs.json 90 行齐全
- [ ] divergence-taxonomy.md 90 cell 各有标签
- [ ] rubric-alignment-spec.md 三维度有选定值+理由
- [ ] cross_judge.py 已修改（diff 可见）
- [ ] local-rerun-aligned.jsonl 90 行
- [ ] rubric-alignment-report.md 含 ρ≥0.6 或如实登记失败原因
- [ ] arm 排序: S0 仍为双通道最差 + Kendall τ≥0.5

## 失败降级
arena 不可用 → 本地 :8787 走完整 loop，conf-0.2，工件照常落盘。