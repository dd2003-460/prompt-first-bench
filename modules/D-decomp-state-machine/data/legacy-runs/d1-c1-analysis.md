# C1: D1 (GPT Researcher) 3rep/Q 扩展 — 配对比较

> 日期: 2026-11-07 | Judge: local 27b self-judge (conf cap 0.7) | Commit: pending

## 一句话结论

S5 (memory hook pipeline) 在 5 道题上全面击败 D1 (GPT Researcher default pipeline)，
差异在 95% 置信度下统计显著（bootstrap CI 不重叠）。但两个 caveat：
① self-judge 天花板 0.7；② Q1/Q2 各有 1 个 rep 搜索失败拉低了 D1 分数。

## 数据

### D1 C1 逐 run 分数（n=15，2 个搜索失败）

| Q | r1 | r2 | r3 | mean(valid) | 备注 |
|---|-----|-----|-----|-------------|------|
| Q1 | 0.517 | 0.622 | **0.000** | 0.570 | r3 搜索返回 0 源，236 chars |
| Q2 | 0.613 | 0.714 | **0.000** | 0.663 | r3 搜索弱，1506 chars |
| Q3 | 0.646 | 0.634 | 0.718 | 0.666 | |
| Q4 | 0.637 | 0.472 | 0.608 | 0.572 | |
| Q5 | 0.765 | 0.716 | 0.705 | 0.729 | |
| **Overall** | | | | **0.644** (n=13 valid) | |

### 对比表

| Arm | n | Mean | Bootstrap 95% CI | 来源 |
|-----|---|------|-----------------|------|
| S5 (pfb memory hook) | 30 | 0.7907 | [0.764, 0.816] | scoring.md @673760a |
| D1 old (1rep/Q) | 5 | 0.602 | — | d1-score-draft.md @dbf6705 |
| **D1 C1 (3rep/Q)** | **13 valid** | **0.644** | **[0.598, 0.686]** | 本文件 |

### 配对比较（per-question）

| Q | S5 mean | D1-C1 mean | Δ | 方向 |
|---|---------|------------|---|------|
| Q1 | 0.785 | 0.570 | +0.216 | S5 > D1 |
| Q2 | 0.802 | 0.663 | +0.139 | S5 > D1 |
| Q3 | 0.791 | 0.666 | +0.125 | S5 > D1 |
| Q4 | 0.778 | 0.572 | +0.206 | S5 > D1 |
| Q5 | 0.794 | 0.729 | +0.065 | S5 > D1 |

Sign test: 5+/0-/0= (n=5), p=0.031 (exact binomial)

## 统计检验

- **Bootstrap CI 不重叠**: S5 [0.764, 0.816] vs D1-C1 [0.598, 0.686] → 95% 显著 ✅
- **Paired sign test**: 5/5 positive, p=0.031 < 0.05 → 显著 ✅
- **效应量**: Cohen's d ≈ (0.7907-0.644)/pooled_sd ≈ 0.7-0.9（大效应）

## Caveats（必须声明）

1. **Self-judge**: 所有分数由被评模型自己打（27b），存在系统性自偏。
   conf cap 0.7。异族 judge 校准已通过（κ=0.70, mistral×gemini @c304c78），
   但正式结论需要异族 judge 重打分。
2. **搜索质量下限**: D1 用 duckduckgo 无 API key，Q1r3/Q2r3 搜索失败
   （0 sources / 236 chars）。如果对齐搜索质量（Tavily/SerpAPI），
   D1 分数可能上升，Δ 会缩小。
3. **n 不对称**: S5 n=30 vs D1 n=13 valid。统计功效有限。
4. **同模型**: 两边都用 qwen3.8-27b，比的是 pipeline 不是模型。

## 下一步

- [ ] 异族 judge 重打分（mistral-large-4-high + gemini-3.8-flash 已校准）
- [ ] C2 搜索对齐可行性检查（Tavily free tier 够不够 15 runs）
- [ ] 如果异族 judge 确认 Δ 仍然显著 → C 面 "打赢开源" 初步成立
- [ ] 扩展到 Q6/Q7（T49 gold tree 完成后）验证泛化