# S8G 泛化验证 + S7V 基线补跑

> origin: ai · 2026-11-06 · 前置: pfb-v3-gold-gap PASS @5a7f375
> 约束: 无答案泄漏; S8G prompt 不得因新题修改 (只允许修 harness/hook bug)

## 目标

验证 S8G patch (A1-A4) 在 Q1/Q4 上的泛化性, 并补跑 S7V/S7F 基线作为严格参照物。

## 任务表

| # | 任务 | 产出 | 验收 |
|---|------|------|------|
| G1 | S8G × Q1 × 2rep (hook on) | runs-r293/S8G-Q1-r{1,2}.json + scores | Total 均值 ≥ 0.70 (Q1 是方法论域, 预期比 Q5 好) |
| G2 | S8G × Q4 × 2rep (hook on) | runs-r293/S8G-Q4-r{1,2}.json + scores | Total 均值 ≥ 0.65 (Q4 是工程域, arXiv 召回可能差) |
| G3 | S7V × Q1/Q4/Q5 × 1rep | runs-r293/S7V-*.json + scores | 基线数据落盘 (不要求分数, 只要求跑通) |
| G4 | S7F × Q1/Q4/Q5 × 1rep | runs-r293/S7F-*.json + scores | 同上 |
| G5 | 汇总对比表 | loop-artifacts/stages/04/generalization-report.md | S8G vs S7V vs S7F vs S5 vs Arena 五臂对比, 含 M1-M6 逐项 |

## 失败降级

- Q4 域 arXiv 召回 <2 条 → 标 [RESEARCH-GAP], 该题 M5/M6 不计入主分析
- S7V/S7F 脚本不存在或报错 → 先修 harness, 修不动则标 blocked-on-tooling
- S8G 在某题 Total < 0.5 → 记录失败模式, 不回改 prompt (归入下一 goal 的 prompt v2)