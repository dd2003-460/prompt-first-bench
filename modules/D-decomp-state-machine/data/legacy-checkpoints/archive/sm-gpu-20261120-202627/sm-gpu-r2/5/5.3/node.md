# N27: 性价比指标 (Performance/Cost) 计算公式：Cost_Efficiency = (Throughput_tokens_per_s / Total

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

性价比指标 (Performance/Cost) 计算公式：Cost_Efficiency = (Throughput_tokens_per_s / Total_TCO_3yr)。其中 Total_TCO_3yr = CapEx + OpEx_energy_3yr。需对比工作点 A 和工作点 B 的该比值，确定在 3 年持有期内的最优解。

## Corrected Claim

性价比指标 (Performance/Cost) 计算公式：Cost_Efficiency = (Throughput_tokens_per_s / Total_TCO_3yr)。其中 Total_TCO_3yr = CapEx + OpEx_energy_3yr。需对比工作点 A 和工作点 B 的该比值，确定在 3 年持有期内的最优解。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式的分子修正、分母细化及最终计算结论，逻辑层级清晰，无内容重叠或矛盾。分子修正关注质量因子，分母计算关注运维成本，最终对比基于前两者得出，符合正交性原则。完备性上，涵盖了父节点定义的所有关键变量（吞吐量、质量、CapEx、OpEx_energy、OpEx_maintenance）及最终决策逻辑。无冗余，因为每个子节点承担不同的定义或计算步骤，不可合并为单一参数。）

## Search Query

GPU TCO calculation formula performance per dollar inference
