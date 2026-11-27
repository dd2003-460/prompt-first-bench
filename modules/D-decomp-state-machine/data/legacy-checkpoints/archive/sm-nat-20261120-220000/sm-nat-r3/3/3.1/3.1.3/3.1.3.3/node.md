# N104: 交互效应工作点：若启用请求去重（Request Coalescing），则P(miss|refill)趋近于0，折损降低至 p_invalid * f_sour

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N36

## Claim

交互效应工作点：若启用请求去重（Request Coalescing），则P(miss|refill)趋近于0，折损降低至 p_invalid * f_source_fail ≈ 0.01 * 0.0021 ≈ 0.002%。这是'高性低成'工作点，代价是增加CDN节点内存开销存储pending请求。

## Corrected Claim

交互效应工作点：若启用请求去重（Request Coalescing），则P(miss|refill)趋近于0，折损降低至 p_invalid * f_source_fail ≈ 0.01 * 0.0021 ≈ 0.002%。这是'高性低成'工作点，代价是增加CDN节点内存开销存储pending请求。

## Evidence

先验知识/题面给定，逻辑校验通过：请求去重（Coalescing）在理论上确实能消除并发重复请求导致的缓存未命中（P(miss|refill)→0），剩余损耗仅取决于源站失败率等独立因素，数值量级（0.01 * 0.0021 ≈ 0.000021 = 0.0021% ≈ 0.002%）计算正确且符合CDN优化原理。
