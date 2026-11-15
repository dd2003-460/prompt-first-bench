【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

# V3 Benchmark Hardening — 本地执行任务卡

## 目标
对 runs-r293 的 61 条评分数据做统计严谨性加固 + 最终汇总。

## 执行项（纯本地 Python，无 arena 依赖）

### A. 统计计算
- A1: Bootstrap 95% CI for per-arm Total (n=15, 10k resamples, seed=42)
- A2: Paired sign test on S5-S0 / S1-S0 / S5-S1 deltas (per-run paired by qid+rep)
- A3: Per-metric bootstrap CIs (M1-M6)

### B. R-06 文档
- B1: 在 RESULTS-FINAL.md 中记录 same-family judge 局限
- B3: 所有数字标注 judge family = qwen3.8-27b (same-family as evaluated model)

### C. 最终汇总
- C1: 合并 scores-v3.json (45) + scores-v3-secondary.json (16) → 单表
- C2: 加 CI 列 + 显著性标记 (* p<0.05, ** p<0.01)
- C3: 写 experiments/stage-ablation/RESULTS-FINAL.md

### D. 已知局限
- D1: S8D prompt 不可复现 → 标注 "non-reproducible"
- D2: 异族 judge 不可用 → future work
- D3: n=15/arm → power limited, report effect sizes

## 验收
- [ ] RESULTS-FINAL.md 存在且含完整表格
- [ ] 所有 Total 分数带 95% CI
- [ ] Arm delta 带 p 值
- [ ] Judge family caveat 出现在每个数字旁边
- [ ] commit + push

## 失败降级
B2 (异族 judge 量化) 无法执行 → 标注 conf-0.2 + blocked-on-external，不阻塞其余项。