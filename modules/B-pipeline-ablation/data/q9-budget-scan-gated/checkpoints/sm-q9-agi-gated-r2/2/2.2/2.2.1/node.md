# N31: 实验设计阶段每次 refinement 的上下文更新量 Δtokens 服从几何分布，均值 μ=1.5k tokens；收敛所需迭代次数 k 服从负二项分布，P

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

实验设计阶段每次 refinement 的上下文更新量 Δtokens 服从几何分布，均值 μ=1.5k tokens；收敛所需迭代次数 k 服从负二项分布，P(k≥5) ≈ 0.35，导致总 token 消耗 E[Total] = 2k * (1 + 0.35*4 + 0.65*5) ≈ 12.4k tokens，为初始 prompt 的 6.2 倍

## Corrected Claim

实验设计阶段每次 refinement 的上下文更新量 Δtokens 均值约为 1.5k tokens；收敛所需迭代次数 k 服从负二项分布，P(k≥5) ≈ 0.35。基于特定假设（如初始 prompt 为 2k tokens 且后续迭代成本结构符合特定线性模型），估算总 token 消耗约为 12.4k tokens，约为初始 prompt 的 6.2 倍。

## Evidence

[质询]公式逻辑不自洽：E[Total]的计算公式中混合了常数项与概率加权项，且'2k'中的k指代不明（是固定值还是随机变量？），导致数学推导无法复现12.4k的结果；此外，'6.2倍'隐含初始prompt为2k tokens，但这未在陈述中明确定义，属于隐含假设。 | 先验知识/题面给定，但逻辑校验发现公式推导存在内部矛盾（常数与随机变量混用，计算过程不透明），无法从第一性原理严格推出该具体数值，故降级。
