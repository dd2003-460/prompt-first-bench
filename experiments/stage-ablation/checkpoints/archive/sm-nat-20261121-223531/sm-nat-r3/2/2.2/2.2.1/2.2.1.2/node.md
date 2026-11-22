# N124: 若坚持使用 β=0.9 作为幂律指数（即 P(H>h) ∝ h^{-0.9}），则累积概率 F_H(h) = 1 - (h_min/h)^{0.9-1} 在 h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

若坚持使用 β=0.9 作为幂律指数（即 P(H>h) ∝ h^{-0.9}），则累积概率 F_H(h) = 1 - (h_min/h)^{0.9-1} 在 h→∞ 时不收敛到 1，表明该参数下分布未归一化或需截断。在截断上限 h_max 下，中位数 h_median 需数值求解 1 - (h_min/h_median)^{-0.1} = 0.5，即 (h_median/h_min)^{0.1} = 0.5，解得 h_median = h_min * 0.5^{10} ≈ h_min * 0.000977，这小于 h_min，矛盾。说明 β=0.9 时 Pareto 分布形状参数需重新定义或该假设下中位数无物理意义。

## Corrected Claim

若坚持使用 β=0.9 作为幂律指数（即 P(H>h) ∝ h^{-0.9}），则累积概率 F_H(h) = 1 - (h_min/h)^{0.9-1} 在 h→∞ 时不收敛到 1，表明该参数下分布未归一化或需截断。在截断上限 h_max 下，中位数 h_median 需数值求解 1 - (h_min/h_median)^{-0.1} = 0.5，即 (h_median/h_min)^{0.1} = 0.5，解得 h_median = h_min * 0.5^{10} ≈ h_min * 0.000977，这小于 h_min，矛盾。说明 β=0.9 时 Pareto 分布形状参数需重新定义或该假设下中位数无物理意义。

## Evidence

先验知识/题面给定，逻辑校验通过：幂律指数 β=0.9 < 1 导致累积分布函数在无穷远处发散，截断后中位数计算确实小于下限，证明该参数下标准 Pareto 分布定义失效或需重新定义。

## Search Query

Pareto distribution shape parameter 0.9 median calculation
