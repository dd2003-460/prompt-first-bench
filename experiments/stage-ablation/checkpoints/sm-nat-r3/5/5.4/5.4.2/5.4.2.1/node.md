# N244: 在对数负相关（log S_i = a - b log R_i, ρ=-0.3）约束下，对象 i 的大小 S_i 由热度 R_i 确定的函数形式为 S_i = A

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86, N87, N88

## Claim

在对数负相关（log S_i = a - b log R_i, ρ=-0.3）约束下，对象 i 的大小 S_i 由热度 R_i 确定的函数形式为 S_i = A * R_i^{-b}，其中 A = exp(a)，b = -ρ * σ_S / σ_R（σ_S, σ_R 为对数变换后的标准差），需基于 Pareto(α=1.1) 和 Pareto(β=0.9) 的截断参数计算 b 的具体数值。

## Corrected Claim

在对数负相关约束下，S_i = A * R_i^{-b} 的形式成立，其中 b = -ρ * σ_S / σ_R。但 b 的具体数值需结合 Pareto 分布的截断边界及样本统计量计算，仅凭 α=1.1 和 β=0.9 无法直接得出唯一数值，需补充截断条件或样本数据。

## Evidence

[质询]公式中 b 的定义存在逻辑矛盾：在对数线性回归模型 log S = a - b log R 中，斜率 b 由相关系数 ρ 和标准差决定，公式应为 b = -ρ * (σ_S / σ_R)。然而，题目声称 ρ=-0.3，若 b 为正数（通常大小与热度负相关意味着 b>0），则 -ρ 为正，公式成立。但更严重的攻击点在于：Pareto 分布的参数 α 和 β 通常直接定义了尾部指数，而通过截断参数计算 b 的具体数值需要明确的截断边界和分布归一化条件，仅凭 α=1.1 和 β=0.9 无法唯一确定 b 的数值，除非有特定的截断假设（如最小/最大值）。此外，将 Pareto 参数直接关联到回归斜率 b 的推导过程在陈述中缺失，属于经验/统计推断而非第一性原理直接推导。 | 逻辑上，对数线性关系的斜率公式 b = -ρ * σ_S / σ_R 是统计学标准结论，逻辑自洽。但该事实涉及具体的统计参数计算（基于 Pareto 分布的截断参数求 b），属于经验/统计推断范畴，且无外部来源支持具体的数值计算过程或结果，无法验证 b 的具体数值是否由给定的 Pareto 参数唯一确定。

## Search Query

Pareto distribution correlation coefficient standard deviation log transform size popularity
