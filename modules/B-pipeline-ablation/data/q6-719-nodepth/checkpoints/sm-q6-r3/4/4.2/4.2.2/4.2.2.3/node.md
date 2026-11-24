# N339: 缓存命中率 H_pop 对P99延迟的非线性影响：当 H_pop < 0.9 时，P99延迟主要由回源链路决定（RTT_pop_origin ≈ 50-100m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

缓存命中率 H_pop 对P99延迟的非线性影响：当 H_pop < 0.9 时，P99延迟主要由回源链路决定（RTT_pop_origin ≈ 50-100ms）；当 H_pop > 0.95 时，P99延迟收敛于本地处理延迟（T_proc_pop ≈ 10-20ms），存在临界点 H_pop_critical ≈ 0.92。

## Corrected Claim

缓存命中率 H_pop 对P99延迟的非线性影响：当 H_pop < 0.9 时，P99延迟主要由回源链路决定（RTT_pop_origin ≈ 50-100ms）；当 H_pop > 0.95 时，P99延迟收敛于本地处理延迟（T_proc_pop ≈ 10-20ms），存在临界点 H_pop_critical ≈ 0.92。

## Evidence

先验知识/题面给定，逻辑校验通过
