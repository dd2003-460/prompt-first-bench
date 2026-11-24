# N16: 冷数据（80%）存储策略成本影响：云存储中80%数据转入IA/Archive层，成本降低约50-70%；本地存储中冷数据仍占用NVMe/HDD容量，无额外成本但

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

冷数据（80%）存储策略成本影响：云存储中80%数据转入IA/Archive层，成本降低约50-70%；本地存储中冷数据仍占用NVMe/HDD容量，无额外成本但需考虑HDD机械磨损

## Corrected Claim

冷数据（80%）存储策略成本影响：云存储中80%数据转入IA/Archive层，成本降低约50-70%；本地存储中冷数据仍占用NVMe/HDD容量，无额外成本但需考虑HDD机械磨损

## Evidence

先验知识/题面给定，逻辑校验通过：云存储IA/Archive层单价通常为标准存储的30%-50%，80%数据迁移后整体成本降低50%-70%符合线性加权逻辑；本地存储冷数据占用容量无额外直接费用但存在机械磨损风险，符合物理与经济直觉。

## Search Query

cloud storage lifecycle policy cold data cost reduction
