# r293 V3 重评分笔记 (2026-11-06)

## 背景
V2 评分使用旧版 judge prompt（gold[:6000] 截断 + 无 gold_type 检测）。
本轮用当前 score.py（judge v2: gold_type auto-detect + 完整断言提取）对 45 runs 全量重评。

## 方法
- 45 runs (S0/S1/S5 × Q1-Q5 × n=3)，本地 27B judge，temp=0
- 4 并发，总耗时 409s
- multi_n=1（验证了 temp=0 下 judge 完全确定性：同一输入 5 次调用 spread=0.0）

## 结果 (per-run mean, n=15/arm)

| Arm | Total | M1    | M2    | M3    | M4    | M5    |
|-----|-------|-------|-------|-------|-------|-------|
| S0  | 0.615 | 0.904 | 0.520 | 0.844 | 0.830 | 0.010 |
| S1  | 0.630 | 0.863 | 0.580 | 0.933 | 0.793 | 0.000 |
| S5  | 0.805 | 0.968 | 0.598 | 0.956 | 0.890 | 0.289 |

Δ(S1-S0) = +0.014 Total, Δ(S5-S1) = +0.176 Total

## V2 → V3 变化分析

### 系统性偏移 (+0.06~+0.18 Total)
原因：V2 用旧 judge（截断 6000 字符、无 gold_type 区分），大量断言被漏判或误判 mismatch。
V3 的 judge 正确识别 methodology 型 gold（Q5）和 data 型 gold（Q1-Q4），断言提取更完整。

### Q4 修复验证 ✅
所有 9 个 Q4 runs M1 ≥ 0.933（V2 中 S1/S5 全部 = 0.000）。
题面-gold 不一致问题已消除。

### 唯一负向偏移
S1-Q5-r1: M1 0.571 → 0.000
原因：V3 judge 将 Q5 识别为 methodology 型，要求对照公开知识判 correct/incorrect。
该 run 的定量断言（C_error 估计区间等）全部被判 uncertain（不计入分母），导致 total_decidable=0 → M1=0。
V2 judge 用 data 型逻辑（对照 gold 文本），能匹配到部分断言。
**这是 judge 行为差异，不是模型输出退化。** Q5 是方法论型问题，M1 权重已降半（0.125），影响有限。

### Judge 确定性验证
temp=0 下同一输入连续 5 次调用：spread = 0.0（完全确定）。
--multi N 参数保留作为保险，但当前 judge 在 temp=0 下无需多采样。

## 结论
1. V3 分数比 V2 高 0.06-0.18，原因是 judge 改进（非模型改进）
2. 臂间排序不变：S5 > S1 > S0（V2: S5>S1>S0, V3: S5>S1>S0）
3. Δ(S5-S0) 从 +0.111(V2) 扩大到 +0.190(V3) — 因为 S0 的 M1 提升幅度小于 S5
4. Q4 设计缺陷修复确认有效
5. 建议：论文/报告引用 V3 分数，标注 judge 版本 + conf cap 0.7 + per-run 口径
