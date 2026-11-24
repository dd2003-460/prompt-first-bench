# N216: 工作点B（成本敏感/混合存储）：采用 80% NVMe SSD + 20% HDD 分层存储，加权单位成本 C_hybrid = 0.8 * 1.2 + 0.2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

工作点B（成本敏感/混合存储）：采用 80% NVMe SSD + 20% HDD 分层存储，加权单位成本 C_hybrid = 0.8 * 1.2 + 0.2 * 0.2 = ¥1.0/GB/月；若 N_storage = 3.6TB，月度存储成本 C_storage_total = 3600GB * 1.0 = ¥3,600/月；热数据 P99 延迟 < 15ms，冷数据回源延迟增加但占比低。

## Corrected Claim

工作点B（成本敏感/混合存储）：采用 80% NVMe SSD + 20% HDD 分层存储，加权单位成本 C_hybrid = 0.8 * 1.2 + 0.2 * 0.2 = ¥1.0/GB/月；若 N_storage = 3.6TB，月度存储成本 C_storage_total = 3600GB * 1.0 = ¥3,600/月；热数据 P99 延迟 < 15ms，冷数据回源延迟增加但占比低。

## Evidence

先验知识/题面给定，逻辑校验通过：加权成本计算 0.8*1.2 + 0.2*0.2 = 0.96 + 0.04 = 1.0 正确；总成本 3600 * 1.0 = 3600 正确；混合存储架构下热数据由SSD承载满足低延迟，冷数据由HDD承载符合分层存储逻辑。

## Search Query

hybrid SSD HDD storage cost per GB monthly data center
