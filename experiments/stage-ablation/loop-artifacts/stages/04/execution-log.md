# V3 Benchmark Hardening — 阶段 04 执行日志 (execution-log.md)

> origin: ai · 2026-11-06 · 任务卡: tasks/v3-hardening.md @ 6720a29
> 执行通道: 本地 Python (arena 会话不可用, 按任务卡"纯本地 Python, 无 arena 依赖"条款降级本地执行, conf-0.2)

## 执行回执

| 项 | 状态 | 证据 |
|----|------|------|
| A1 Bootstrap 95% CI per-arm Total (B=10k, seed=42) | done | runs-r293/stats-v3.json → bootstrap_ci (S0/S1/S5/Arena/S8A-F) |
| A2 Paired sign test S5-S0 / S1-S0 / S5-S1 (paired by qid+rep) | done | stats-v3.json → paired_deltas: S5-S0 p=0.00098**, S1-S0 p=1.0 ns, S5-S1 p=0.00001** |
| A3 Per-metric bootstrap CIs (M1-M6) | done | RESULTS-FINAL.md "Per-Metric CIs" 表 (S0/S1/S5 × M1-M6) |
| B1 Same-family judge 局限记录 | done | RESULTS-FINAL.md header caveat + Limitations L1 (conf-0.2 on absolute values) |
| B2 异族 judge 量化 | blocked-on-external | T23-hetero-judge-blocker.md; 标注 conf-0.2, future work, 不阻塞其余项 |
| B3 数字标注 judge family = qwen3.8-27b | done | RESULTS-FINAL.md Method + 每表注记 |
| C1 合并 scores-v3.json (45) + scores-v3-secondary.json (16) | done | RESULTS-FINAL.md Main Arms + Secondary Arms 单表 |
| C2 CI 列 + 显著性标记 | done | 主表带 95% CI 列; delta 表带 **/* /ns |
| C3 RESULTS-FINAL.md | done | experiments/stage-ablation/RESULTS-FINAL.md (commit f876e1e) |
| D1 S8D non-reproducible 标注 | done | Secondary Arms 表 Note 列 + Limitations L3 |
| D2 异族 judge future work | done | Limitations L1 mitigation |
| D3 n=15 power limited + effect sizes | done | Limitations L2 + mean_delta 数值报告 |

## 验收自检

- [x] RESULTS-FINAL.md 存在且含完整表格
- [x] 所有 Total 分数带 95% CI
- [x] Arm delta 带 p 值
- [x] Judge family caveat 出现在每个数字旁边 (header + Method + L1)
- [x] commit (f876e1e + 6720a29), push 待验证

## 核心结果

- S5 (memory hook) = 0.805 [0.762, 0.841], 显著高于 S0 (0.615) 和 S1 (0.630)
- S5-S0 Δ=+0.190 (p=0.001**), S5-S1 Δ=+0.176 (p=0.0001**), S1-S0 Δ=+0.014 (ns)
- Arena (n=3) = 0.713 [0.500, 0.909] — 探索性, CI 宽
- 效应驱动指标: M5 anchoring (0.01→0.29), M6 sourcing (0.00→1.00)
