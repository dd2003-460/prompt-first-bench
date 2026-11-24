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

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于成本计算（Cost），子节点2聚焦于性能延迟（Latency），两者维度不同且互不重叠，符合正交性。父节点中关于存储架构（80/20混合）和具体数值（3.6TB, 1.0元/GB）均作为输入参数在两个子节点中引用或推导，未遗漏关键方面，且两个子节点分别对应不同的业务指标，不存在冗余。）

## Search Query

hybrid SSD HDD storage cost per GB monthly data center
