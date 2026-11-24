# N217: 缓存预热对 P99 延迟改善的边际效用递减：Top 1000 对象覆盖 60% 请求，预热后 P99 改善 ΔT1 = 150ms；Top 5000 对象覆盖 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

缓存预热对 P99 延迟改善的边际效用递减：Top 1000 对象覆盖 60% 请求，预热后 P99 改善 ΔT1 = 150ms；Top 5000 对象覆盖 90% 请求，预热带宽增加 5 倍，P99 改善 ΔT2 = 160ms，边际效用 = (ΔT2 - ΔT1) / (B_prefetch2 - B_prefetch1) = 10ms / 11.1Mbps ≈ 0.9ms/Mbps，低于 Top 1000 的 150ms / 2.22Mbps ≈ 67.6ms/Mbps

## Corrected Claim

缓存预热对 P99 延迟改善的边际效用递减：Top 1000 对象覆盖 60% 请求，预热后 P99 改善 ΔT1 = 150ms；Top 5000 对象覆盖 90% 请求，预热带宽增加 5 倍，P99 改善 ΔT2 = 160ms，边际效用 = (ΔT2 - ΔT1) / (B_prefetch2 - B_prefetch1) = 10ms / 11.1Mbps ≈ 0.9ms/Mbps，低于 Top 1000 的 150ms / 2.22Mbps ≈ 67.6ms/Mbps

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（10/11.1≈0.9, 150/2.22≈67.6），符合缓存预热中热点覆盖边际效用递减的工程直觉。

## Search Query

cdn prefetch marginal utility p99 latency improvement diminishing returns
