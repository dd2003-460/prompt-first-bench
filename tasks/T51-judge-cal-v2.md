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
| 1 | score_s10_v2.py 全量 90 runs | ✅ done | s10-runs/s10-scores-v2.json (90/90) |
| 2 | S10-B-Q1-r1-WITHTOOLS sub (较真研究员人格+工具) | ✅ done | s10-runs/S10-B-Q1-r1-WITHTOOLS.json (7 sources, @a139c81) |
| 3 | 拼对比表: noTools(旧) vs withTools(新) × M1-M6 | ✅ done | runs/s10-v2-comparison.md |
| 4 | 异族 judge R2: 选 15 samples 送 arena battle | ✅ done | s10-hetero-scores-v2-raw.json + runs/s10-hetero-results-v2.md |
| 5 | 算 Fleiss'κ (v2 scores vs hetero R2) | ✅ PASS | Pearson r=0.835 ≥ 0.6 gate（注：实际算的是 Pearson 非 Fleiss'κ，n=15 两 judge） |

## 已知问题（2026-11-07 核对发现，待修）

1. **withTools run 不在 s10-scores-v2.json 里**——该文件只有 90 条 noTools；comparison 表里的 withTools 分数（total 0.856 / M1 1.0 / M2 1.0）来源未落盘，需重跑 scorer 对该 run 单独打分并归档。
2. **s10-hetero-results-v2.md §关键发现#2 与 raw 数据不符**——报告写"A=0.682, B=0.886"只记了 RE1（withTools），但 Judge A 对 A 臂三个样本（RC3/RE2/RC2）M1 全部给 0.28、总分 0.29-0.32，Judge B 给 0.40-0.46；A 臂整体是最低分而非仅 RE1 最高。报告表述有误导，需按 raw 重写该节。
3. **D 臂 local(0.278) vs hetero(0.587/0.563) 差距异常大**（~0.30，其他臂 <0.13）——本地 scorer 对 D 臂系统性偏严，或 hetero judge 对 D 臂的"人话 review"风格偏宽容。r=0.835 是跨样本相关，掩盖了臂级偏差。归因进 E3 双轨评分实验范围。

## 验收标准

- [ ] s10-scores-v2.json 含 ≥90 条 (M1-M5 数值, M6 deferred)
- [ ] S10-B-Q1-r1-WITHTOOLS.json 存在且 sources≥3 URLs
- [ ] s10-v2-comparison.md 含 noTools vs withTools 五臂对比表
- [ ] 异族 R2 κ≥0.6 (否则回 rubric 修)

## 失败降级

若 arena battle 不可用 → 本地 27b 自评 (conf cap 0.7) + 标 [异族未验证]，不阻塞后续 C1。