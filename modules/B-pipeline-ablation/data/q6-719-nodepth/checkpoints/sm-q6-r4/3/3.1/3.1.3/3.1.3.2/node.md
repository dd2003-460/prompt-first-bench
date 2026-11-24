# N214: 工作点B（低成本/低缓存命中率）：Hot_Data_Size 设为日均下载量的 15%（300GB/天），保留 3 天热数据即 0.9TB；Hot_Spillo

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

工作点B（低成本/低缓存命中率）：Hot_Data_Size 设为日均下载量的 15%（300GB/天），保留 3 天热数据即 0.9TB；Hot_Spillover_Ratio 取 1.2 以最小化存储开销；N_storage = (0.9TB + 0) * 1.2 = 1.08TB/POP。此配置下缓存命中率 H 预计降至 75%，回源率增加至 25%，但单 POP 存储成本降低约 70%。

## Corrected Claim

工作点B（低成本/低缓存命中率）：Hot_Data_Size 设为日均下载量的 15%（300GB/天），保留 3 天热数据即 0.9TB；Hot_Spillover_Ratio 取 1.2 以最小化存储开销；N_storage = (0.9TB + 0) * 1.2 = 1.08TB/POP。此配置下缓存命中率 H 预计降至 75%，回源率增加至 25%，但单 POP 存储成本降低约 70%。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 813)

## Search Query

CDN cache hit rate vs storage capacity relationship 75% hit rate
