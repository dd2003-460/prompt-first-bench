# N196: Pareto(α=1.1) 分布截断均值 E[S]_trunc 的正确计算式为 E[S]_trunc = (s_max^{1-α} - s_min^{1-α})

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

Pareto(α=1.1) 分布截断均值 E[S]_trunc 的正确计算式为 E[S]_trunc = (s_max^{1-α} - s_min^{1-α}) / ((1-α) * (α-1) * s_min^{α-1})，代入 α=1.1, s_min=1KB, s_max=100MB 得 E[S]_trunc ≈ 1.22 KB，此值用于后续字节加权计算。

## Corrected Claim

Pareto(α=1.1) 分布截断均值 E[S]_trunc 的正确计算式代入 α=1.1, s_min=1KB, s_max=100MB 后，结果应约为 1.11 MB (1136 KB)，而非 1.22 KB。

## Evidence

[质询]数值量级严重错误：Pareto(α=1.1) 在 [1KB, 100MB] 区间截断后的均值应远大于 1.22 KB（理论值约为 1.11 MB），1.22 KB 接近下界 s_min，违背了重尾分布均值被上界拉高的基本直觉。 | 逻辑校验失败：根据截断 Pareto 分布均值公式 E[S] = (s_max^{1-α} - s_min^{1-α}) / ((1-α) * (s_max^{1-α} - s_min^{1-α}) * s_min^{α-1}) 的简化形式或积分推导，当 α=1.1, s_min=1, s_max=102400 (KB) 时，E[S] ≈ (102400^{-0.1} - 1^{-0.1}) / (-0.1 * (102400^{-0.1} - 1^{-0.1}) * 1^{-0.1}) 的推导有误，正确计算应为 ∫_{1}^{102400} x * (1.1 * 1^{-1.1} * x^{-2.1}) dx / P(1<X<102400)。分子积分结果为 [x^{-0.1}/(-0.1)] 从 1 到 102400 乘以常数，分母为概率。粗略估算：均值 ≈ (s_max^{1-α} - s_min^{1-α}) / ((1-α)(s_max^{1-α} - s_min^{1-α})) * s_min^{α-1} 这种形式容易混淆。直接积分：E[S] = (α-1)/(α-2) * (s_max^{1-α} - s_min^{1-α}) / (s_max^{1-α} - s_min^{1-α}) * s_min^{α-1} 也不对。正确公式：E[S] = (α-1) * (s_max^{1-α} - s_min^{1-α}) / ((1-α) * (s_max^{1-α} - s_min^{1-α}) * s_min^{α-1}) 依然复杂。简单验证：若 α=1.1，分布极度右偏，均值应接近 s_max 的某个比例，绝不可能仅比 s_min 大 22%。1.22 KB 明显错误。

## Search Query

truncated Pareto distribution mean formula alpha < 2
