# N39: LFU 相比 LRU 提升的理论最大值：在理想情况下，若 LRU 完全失效（缓存全部为冷对象），而 LFU 完美保留热对象，则 ΔH_max = H_LFU -

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LFU 相比 LRU 提升的理论最大值：在理想情况下，若 LRU 完全失效（缓存全部为冷对象），而 LFU 完美保留热对象，则 ΔH_max = H_LFU - 0 = H_LFU。但实际中 LRU 不会完全失效，因此 ΔH_max 的实际值远小于 H_LFU。量化上界：ΔH_max ≤ H_opt - H_LRU_min，其中 H_LRU_min 为 LRU 在最差情况下的命中率。

## Corrected Claim

LFU 相比 LRU 提升的理论最大值：在理想情况下，若 LRU 完全失效（缓存全部为冷对象），而 LFU 完美保留热对象，则 ΔH_max = H_LFU - 0 = H_LFU。但实际中 LRU 不会完全失效，因此 ΔH_max 的实际值远小于 H_LFU。量化上界：ΔH_max ≤ H_opt - H_LRU_min，其中 H_LRU_min 为 LRU 在最差情况下的命中率。

## Evidence

先验知识/题面给定，逻辑校验通过
