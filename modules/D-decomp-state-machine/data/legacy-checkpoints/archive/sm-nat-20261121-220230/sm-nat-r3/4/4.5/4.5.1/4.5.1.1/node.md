# N211: 独立性基线量化：在 u 与 H 独立假设下，LFU 与 LRU 的失效概率差值 ΔP_invalid = 0，因此 LFU 相对 LRU 的额外命中率增益 ΔD

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N73

## Claim

独立性基线量化：在 u 与 H 独立假设下，LFU 与 LRU 的失效概率差值 ΔP_invalid = 0，因此 LFU 相对 LRU 的额外命中率增益 ΔDiscount_LFU_indep = H_steady * 0 = 0 百分点

## Corrected Claim

独立性基线量化：在 u 与 H 独立假设下，LFU 与 LRU 的失效概率差值 ΔP_invalid = 0，因此 LFU 相对 LRU 的额外命中率增益 ΔDiscount_LFU_indep = H_steady * 0 = 0 百分点

## Evidence

先验知识/题面给定，逻辑校验通过：在独立性假设下，访问频率与历史无关，LFU与LRU策略等价，差值为0符合逻辑推导。
