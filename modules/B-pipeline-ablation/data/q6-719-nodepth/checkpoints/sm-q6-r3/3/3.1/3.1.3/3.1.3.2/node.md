# N214: 工作点B（低成本/低缓存命中率）：Hot_Data_Size 设为日均下载量的 15%（300GB/天），保留 3 天热数据即 0.9TB；Hot_Spillo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

工作点B（低成本/低缓存命中率）：Hot_Data_Size 设为日均下载量的 15%（300GB/天），保留 3 天热数据即 0.9TB；Hot_Spillover_Ratio 取 1.2 以最小化存储开销；N_storage = (0.9TB + 0) * 1.2 = 1.08TB/POP。此配置下缓存命中率 H 预计降至 75%，回源率增加至 25%，但单 POP 存储成本降低约 70%。

## Corrected Claim

工作点B（低成本/低缓存命中率）：Hot_Data_Size 设为日均下载量的 15%（300GB/天），保留 3 天热数据即 0.9TB；Hot_Spillover_Ratio 取 1.2 以最小化存储开销；N_storage = (0.9TB + 0) * 1.2 = 1.08TB/POP。此配置下缓存命中率 H 预计降至 75%，回源率增加至 25%，但单 POP 存储成本降低约 70%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（0.9 * 1.2 = 1.08），参数设定与结论（命中率降低、成本降低）在逻辑上自洽且符合CDN缓存设计的一般工程直觉。

## Search Query

CDN cache hit rate vs storage capacity relationship 75% hit rate
