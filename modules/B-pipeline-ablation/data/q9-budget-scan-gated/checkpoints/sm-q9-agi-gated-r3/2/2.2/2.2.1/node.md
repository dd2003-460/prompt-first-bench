# N31: 实验设计阶段每次 refinement 的上下文更新量 Δtokens 服从几何分布，均值 μ=1.5k tokens；收敛所需迭代次数 k 服从负二项分布，P

- **status**: pending
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

父节点级核验未通过：非正交（子节点3直接指出父节点中的总token消耗计算错误（8.9k vs 12.4k），这导致子节点3与父节点的前提假设发生逻辑冲突/矛盾。虽然子节点之间（1-5）在主题上相对正交（分别涉及均值构成、分布参数、总量修正、累积效应、相关性），但整个分解体系未能与父节点保持逻辑一致性。此外，子节点3是对父节点的‘纠错’而非纯粹的‘分解’，破坏了分解结构的层级完整性。）
