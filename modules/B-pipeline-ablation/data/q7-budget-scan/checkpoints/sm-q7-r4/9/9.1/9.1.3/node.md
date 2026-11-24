# N276: 共享基础设施 P_Shared_Infra 量化：HDD+SSD 混合阵列的控制器需同时管理两种介质，功耗略高于纯 HDD，约为 40-50W；背板混合供电损耗

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

共享基础设施 P_Shared_Infra 量化：HDD+SSD 混合阵列的控制器需同时管理两种介质，功耗略高于纯 HDD，约为 40-50W；背板混合供电损耗约为 30W；散热风扇因总热量低（~200W IT 负载），P_fan ≈ 15-20W。合计 P_Shared_Infra ≈ 85-100W

## Corrected Claim

共享基础设施 P_Shared_Infra 量化：HDD+SSD 混合阵列的控制器需同时管理两种介质，功耗略高于纯 HDD，约为 40-50W；背板混合供电损耗约为 30W；散热风扇因总热量低（~200W IT 负载），P_fan ≈ 15-20W。合计 P_Shared_Infra ≈ 85-100W

## Evidence

父节点级核验未通过：非正交（子节点之间存在逻辑包含关系而非正交并列关系。'P_Shared_Infra_Final' 是其他三个物理组件功耗的算术求和，不应作为一个独立的、与物理组件平行的子节点存在。这种结构违反了 MECE（相互独立，完全穷尽）原则中的独立性要求，因为第4个子节点的内容完全依赖于前3个子节点，且导致了信息重复（如数值再次出现）。）

## Search Query

hybrid hdd ssd storage array controller power consumption
