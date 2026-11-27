# N71: 在 1%/天 更新率下，单个对象在 T 小时内未被更新的概率为 P(no update in T) = exp(-λ_update * T) = exp(-0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

在 1%/天 更新率下，单个对象在 T 小时内未被更新的概率为 P(no update in T) = exp(-λ_update * T) = exp(-0.01 * T/24)，当 T = 1 小时时 P ≈ 0.99959，当 T = 24 小时时 P ≈ 0.99005，当 T = 168 小时（7天）时 P ≈ 0.9324，这些概率用于量化缓存对象在 LRU 队列中存活期间的更新风险。

## Corrected Claim

在 1%/天 更新率下，单个对象在 T 小时内未被更新的概率为 P(no update in T) = exp(-λ_update * T) = exp(-0.01 * T/24)，当 T = 1 小时时 P ≈ 0.99959，当 T = 24 小时时 P ≈ 0.99005，当 T = 168 小时（7天）时 P ≈ 0.9324，这些概率用于量化缓存对象在 LRU 队列中存活期间的更新风险。

## Evidence

先验知识/题面给定，逻辑校验通过：基于泊松过程假设，λ=0.01/天，T=1h时exp(-0.01/24)≈0.99958，T=24h时exp(-0.01)≈0.99005，T=168h时exp(-0.07)≈0.93239，数值计算准确且逻辑自洽。
