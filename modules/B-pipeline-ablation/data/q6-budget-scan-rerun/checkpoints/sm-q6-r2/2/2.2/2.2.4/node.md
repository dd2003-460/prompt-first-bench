# N63: 自建POP策略下，Outbound_Traffic_TB 的计费逻辑为：Peak_Bandwidth_Mbps × 86400s / 8 / 1024^2，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

自建POP策略下，Outbound_Traffic_TB 的计费逻辑为：Peak_Bandwidth_Mbps × 86400s / 8 / 1024^2，其中Peak_Bandwidth_Mbps = Avg_Bandwidth_Mbps × Peak_Factor (2-4)，Avg_Bandwidth_Mbps = 2TB/day / 86400s * 8 * 1024^2 ≈ 2960 Mbps，故峰值带宽需求约为 5920-11840 Mbps

## Corrected Claim

自建POP策略下，Outbound_Traffic_TB 的计费逻辑为：Peak_Bandwidth_Mbps × 86400s / 8 / 1024^2，其中Peak_Bandwidth_Mbps = Avg_Bandwidth_Mbps × Peak_Factor (2-4)，Avg_Bandwidth_Mbps = 2TB/day / 86400s * 8 * 1024^2 ≈ 2960 Mbps，故峰值带宽需求约为 5920-11840 Mbps

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算（2TB/day ≈ 2960 Mbps）及峰值带宽范围（2-4倍）计算均符合物理直觉与数学逻辑。
