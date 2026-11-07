# T51: Judge Calibration v2 — Rubric-v2 全量重评 + withTools pilot

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

## 目标

用 rubric-v2 hardened scorer (score_s10_v2.py) 对 S10 全部 90 runs + S10-withTools 新 runs 重新评分，
然后送异族 judge (arena battle) 做 R2 打分，验证 κ≥0.6。

## 执行步骤（Lead 本地执行，非 arena）

| # | 动作 | 状态 | 产出 |
|---|------|------|------|
| 1 | score_s10_v2.py 全量 90 runs | 🔄 后台跑中 | s10-runs/s10-scores-v2.json |
| 2 | S10-B-Q1-r1-WITHTOOLS sub (较真研究员人格+工具) | 🔄 sub 跑中 | s10-runs/S10-B-Q1-r1-WITHTOOLS.json |
| 3 | 拼对比表: noTools(旧) vs withTools(新) × M1-M6 | ⏳ 等 1+2 | runs/s10-v2-comparison.md |
| 4 | 异族 judge R2: 选 15 samples 送 arena battle | ⏳ 等 3 | s10-hetero-scores-v2-raw.json |
| 5 | 算 Fleiss'κ (v2 scores vs hetero R2) | ⏳ 等 4 | κ≥0.6 才过 gate |

## 验收标准

- [ ] s10-scores-v2.json 含 ≥90 条 (M1-M5 数值, M6 deferred)
- [ ] S10-B-Q1-r1-WITHTOOLS.json 存在且 sources≥3 URLs
- [ ] s10-v2-comparison.md 含 noTools vs withTools 五臂对比表
- [ ] 异族 R2 κ≥0.6 (否则回 rubric 修)

## 失败降级

若 arena battle 不可用 → 本地 27b 自评 (conf cap 0.7) + 标 [异族未验证]，不阻塞后续 C1。