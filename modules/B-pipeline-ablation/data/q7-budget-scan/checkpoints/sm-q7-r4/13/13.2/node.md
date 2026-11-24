# N294: 温数据迁移至SSD层的触发阈值与成本：当冷数据占比上升导致温数据绝对量变化（例如从100TB变为50TB或更多），SSD层是否需要缩减或扩容取决于IOPS密度；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N137

## Claim

温数据迁移至SSD层的触发阈值与成本：当冷数据占比上升导致温数据绝对量变化（例如从100TB变为50TB或更多），SSD层是否需要缩减或扩容取决于IOPS密度；若温数据量减少，SSD层闲置容量造成的浪费成本 = 闲置TB数 × ¥3,000/TB × (1/5年) × 5年 = 闲置TB数 × ¥3,000。

## Corrected Claim

温数据迁移至SSD层的触发阈值与成本：当冷数据占比上升导致温数据绝对量变化（例如从100TB变为50TB或更多），SSD层是否需要缩减或扩容取决于IOPS密度；若温数据量减少，SSD层闲置容量造成的浪费成本 = 闲置TB数 × ¥3,000/TB × (1/5年) × 5年 = 闲置TB数 × ¥3,000。

## Evidence

先验知识/题面给定，逻辑校验通过：成本计算公式中时间因子 (1/5年) * 5年 相互抵消，数学推导正确，符合会计折旧逻辑。

## Search Query

SSD idle capacity cost optimization tiered storage
