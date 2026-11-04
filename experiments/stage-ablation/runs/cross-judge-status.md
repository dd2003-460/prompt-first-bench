# Cross-Judge 状态 (2026-11-04)

## 进度
- 已评: 5/120 (S0-Q1-r1/r2/r3, S1-Q1-r1/r3)
- 待评: 115 (S1-Q1-r2 + S2-S5 全部)
- 阻塞: Perplexity 免费额度耗尽 (QUOTA_EXHAUSTED, resume8 确认)

## 初步 Δ (n=5, 仅 Q1)
| tag | local_m1 | perplexity_m1 | Δ |
|-----|----------|---------------|---|
| S0-Q1-r1 | 0.62 | 0.368 | 0.252 |
| S0-Q1-r2 | 0.56 | 0.580 | 0.020 |
| S0-Q1-r3 | 0.62 | 0.425 | 0.195 |
| S1-Q1-r1 | 0.50 | 0.375 | 0.125 |
| S1-Q1-r3 | 0.50 | 0.525 | 0.025 |

mean Δ = 0.124 (n=5, 仅 Q1 单题，不具统计意义)
方向: perplexity 系统性偏低 (4/5 低于 local)，但 n 太小不下结论。

## 下一步
1. 等 Perplexity 额度重置 (滚动窗口, 时间不确定) → `python cross_judge.py` 断点续跑
2. 或换异源 judge 通道 (arena agent 盲判 / ego ChatGPT) — 需成璐决策
3. 120 条全评完后出 κ + 分 arm Δ 报告
