# N234: NVMe SSD 加速恢复额外成本 C_expedited_NVMe 的构成：包括紧急备件采购溢价（¥5,000/块 × 2块）+ 加急物流（¥2,000）+ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

NVMe SSD 加速恢复额外成本 C_expedited_NVMe 的构成：包括紧急备件采购溢价（¥5,000/块 × 2块）+ 加急物流（¥2,000）+ 额外人工加班费（2人 × 4h × ¥500/h）= ¥18,000/次；此成本仅在触发 RTO < 4h 的紧急恢复场景时发生。

## Corrected Claim

NVMe SSD 加速恢复额外成本 C_expedited_NVMe 的构成：包括紧急备件采购溢价（¥5,000/块 × 2块）+ 加急物流（¥2,000）+ 额外人工加班费（2人 × 4h × ¥500/h）= ¥18,000/次；此成本仅在触发 RTO < 4h 的紧急恢复场景时发生。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（10000+2000+4000=18000），成本构成符合紧急恢复场景的经济直觉，无内部矛盾。

## Search Query

emergency hardware replacement cost expedited logistics storage
