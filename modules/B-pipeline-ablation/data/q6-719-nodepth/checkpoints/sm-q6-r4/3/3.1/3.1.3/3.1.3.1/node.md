# N213: 工作点A（高缓存命中率/高存储投入）：Hot_Data_Size 设为日均下载量的 40%（800GB/天），保留 3 天热数据即 2.4TB；Hot_Spil

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

工作点A（高缓存命中率/高存储投入）：Hot_Data_Size 设为日均下载量的 40%（800GB/天），保留 3 天热数据即 2.4TB；Hot_Spillover_Ratio 取 1.5 以应对突发热点；N_storage = (2.4TB + 0) * 1.5 = 3.6TB/POP。此配置下缓存命中率 H 预计从基准 85% 提升至 92%，回源率降低至 8%。

## Corrected Claim

工作点A（高缓存命中率/高存储投入）：Hot_Data_Size 设为日均下载量的 40%（800GB/天），保留 3 天热数据即 2.4TB；Hot_Spillover_Ratio 取 1.5 以应对突发热点；N_storage = (2.4TB + 0) * 1.5 = 3.6TB/POP。此配置下缓存命中率 H 预计从基准 85% 提升至 92%，回源率降低至 8%。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了成本效益、性能延迟和风险应对三个独立维度，逻辑清晰且无重叠。父节点中的存储容量计算（3.6TB）作为前置条件被合理引用，未在各子节点中重复展开，符合正交性原则。）

## Search Query

CDN cache hit rate vs storage capacity relationship 90% hit rate
