# N529: N172 工作点下，若 H_self 维持在 70%（因公有云 H_cloud 降至 85% 导致差距缩小），回源流量 ΔTraffic = 2TB * (85

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N172

## Claim

N172 工作点下，若 H_self 维持在 70%（因公有云 H_cloud 降至 85% 导致差距缩小），回源流量 ΔTraffic = 2TB * (85%-70%) = 300GB/日，与 N171 相同，但存储成本更高，需计算边际收益是否为负，即 ΔC_storage > ΔC_bw_saved 时该优化无效。

## Corrected Claim

N172 工作点下，若 H_self 维持在 70%（因公有云 H_cloud 降至 85% 导致差距缩小），回源流量 ΔTraffic = 2TB * (85%-70%) = 300GB/日，与 N171 相同，但存储成本更高，需计算边际收益是否为负，即 ΔC_storage > ΔC_bw_saved 时该优化无效。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB * 15% = 300GB 计算正确，边际收益判断逻辑自洽
