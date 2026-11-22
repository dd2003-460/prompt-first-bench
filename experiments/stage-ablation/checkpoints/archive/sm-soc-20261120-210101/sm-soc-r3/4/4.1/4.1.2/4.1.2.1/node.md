# N270: 线性公式失效阈值 D_threshold 的确切数值：通过分段线性回归确定，当 D ∈ [0, 20%] 时斜率为 -k1，当 D ∈ (20%, 40%] 时

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

线性公式失效阈值 D_threshold 的确切数值：通过分段线性回归确定，当 D ∈ [0, 20%] 时斜率为 -k1，当 D ∈ (20%, 40%] 时斜率转为 -k2 或正值。需输出 k1, k2 的具体数值及转折点 D* 的 95% 置信区间。

## Corrected Claim

线性公式失效阈值 D_threshold 的具体数值（k1, k2 及 D* 的置信区间）需通过针对特定数据集的分段线性回归确定，不存在通用的确切数值。

## Evidence

[质询]该陈述声称存在一个确切的、普适的数值阈值（D*）及具体的斜率参数（k1, k2），这属于特定的经验事实或模型拟合结果。在没有具体数据集、模型定义或上下文的情况下，断言存在一个通用的“确切数值”是不成立的，且检索无来源支持其具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值无法从第一性原理推出）

## Search Query

price deviation CTR non-linearity threshold second hand market regression
