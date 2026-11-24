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

父节点级核验通过：正交+完备+无冗余（子节点分别关注成本计算和延迟性能两个不同维度，内容正交且无重复；父节点中的存储配置（80/20比例）已作为参数隐含在C_hybrid的计算中，未单独列出子节点，符合分解逻辑；两个子节点完整覆盖了父节点提到的成本和延迟两个关键方面。）

## Search Query

hybrid SSD HDD storage cost per GB monthly data center
