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

父节点级核验未通过：非正交（子节点3直接指出并修正了父节点中关于总token消耗的错误计算（从12.4k修正为8.9k），这与父节点的核心陈述存在逻辑上的矛盾/冲突，违反了正交性中‘不矛盾’的要求。此外，子节点1关注微观构成，子节点3关注宏观期望值，虽然层级不同，但子节点3的存在本身是对父节点前提的否定，导致分解结构不稳定。）
