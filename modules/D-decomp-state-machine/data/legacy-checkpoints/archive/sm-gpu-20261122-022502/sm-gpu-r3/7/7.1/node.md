# N83: 非典型方案 (Apple M3 Ultra) 的 TCO_per_token 计算公式：TCO_M3U = (CapEx_M3U * Depreciation_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

非典型方案 (Apple M3 Ultra) 的 TCO_per_token 计算公式：TCO_M3U = (CapEx_M3U * Depreciation_Factor + OpEx_M3U) / Total_Tokens_Generated，其中 CapEx_M3U ≈ $5,000-$8,000 (Mac Studio 配置)，OpEx_M3U ≈ $0.05/hour (低功耗 ~100W)，Total_Tokens_Generated = Throughput_M3U * Uptime_Hours * 3 Years。

## Corrected Claim

非典型方案 (Apple M3 Ultra) 的 TCO_per_token 计算公式：TCO_M3U = (CapEx_M3U * Depreciation_Factor + OpEx_M3U) / Total_Tokens_Generated，其中 CapEx_M3U ≈ $5,000-$8,000 (Mac Studio 配置)，OpEx_M3U ≈ $0.05/hour (低功耗 ~100W)，Total_Tokens_Generated = Throughput_M3U * Uptime_Hours * 3 Years。

## Evidence

父节点级核验通过：正交+完备+无冗余（两个子节点分别对应 BF16 和 INT8 两种不同的量化/精度场景，属于同一硬件平台下的不同工作点，彼此正交且无矛盾；父节点公式中的 CapEx、OpEx 和 Total_Tokens 在两个子节点中均通过具体数值体现，覆盖了关键方面；虽然结构相似，但代表不同参数配置下的独立结论，不构成冗余。）

## Search Query

Mac Studio M3 Ultra price TCO calculation
