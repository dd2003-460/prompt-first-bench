# N283: 工作点 2（中位放大因子）：当 S_hot/S_cold 比值为 2（典型 Web 负载常见值）时，A_ρ = 1 + 0.3 * (2 - 1) = 1.3，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98, N100, N102

## Claim

工作点 2（中位放大因子）：当 S_hot/S_cold 比值为 2（典型 Web 负载常见值）时，A_ρ = 1 + 0.3 * (2 - 1) = 1.3，LFU 的优势仅放大 30%，ΔH 约为 +0.5% 至 +1.5%，此时 LFU 与 LRU 差异较小，主要取决于缓存容量是否足以覆盖头部对象。

## Corrected Claim

工作点 2（中位放大因子）：当 S_hot/S_cold 比值为 2（典型 Web 负载常见值）时，A_ρ = 1 + 0.3 * (2 - 1) = 1.3，LFU 的优势仅放大 30%，ΔH 约为 +0.5% 至 +1.5%，此时 LFU 与 LRU 差异较小，主要取决于缓存容量是否足以覆盖头部对象。

## Evidence

先验知识/题面给定，逻辑校验通过：公式计算 1 + 0.3*(2-1) = 1.3 正确，且 LFU 在热点比值为 2 时优势有限符合缓存理论直觉。

## Search Query

LFU LRU cache performance comparison moderate skewness web workload
