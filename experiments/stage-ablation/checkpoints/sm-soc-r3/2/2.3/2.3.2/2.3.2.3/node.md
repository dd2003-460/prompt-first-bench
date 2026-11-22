# N166: 曝光量差异倍数 ΔE_sort 的精确计算式：ΔE_sort = (CTR_time * Imp_time) / (CTR_price * Imp_price)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

曝光量差异倍数 ΔE_sort 的精确计算式：ΔE_sort = (CTR_time * Imp_time) / (CTR_price * Imp_price)，其中 Imp 为展示次数，CTR 为点击率；需引入点击率差异项，因为高价商品在 Price-based 模式下不仅展示少，且因位置靠后 CTR 可能进一步降低 20%-30%，导致总曝光差异可能超过 8 倍。

## Corrected Claim

曝光量差异倍数 ΔE_sort 的精确计算式：ΔE_sort = (CTR_time * Imp_time) / (CTR_price * Imp_price)，其中 Imp 为展示次数，CTR 为点击率；需引入点击率差异项，因为高价商品在 Price-based 模式下不仅展示少，且因位置靠后 CTR 可能进一步降低 20%-30%，导致总曝光差异可能超过 8 倍。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

click-through rate position bias e-commerce search results page price sorting impact
