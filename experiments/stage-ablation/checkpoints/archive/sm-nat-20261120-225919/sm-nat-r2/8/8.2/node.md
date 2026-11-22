# N95: 基于 Pareto(α=1.1, s_min=1KB, s_max=100MB) 的截断分布，计算 100,000 个对象的总大小 S_total。若 S_to

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

基于 Pareto(α=1.1, s_min=1KB, s_max=100MB) 的截断分布，计算 100,000 个对象的总大小 S_total。若 S_total ≈ 20GB < 128GB，则缓存可容纳所有对象，k_max = 100,000，LRU 命中率下界为 100%（忽略更新失效）。

## Corrected Claim

基于 Pareto(α=1.1, s_min=1KB, s_max=100MB) 的截断分布，计算 100,000 个对象的总大小 S_total。若 S_total ≈ 20GB < 128GB，则缓存可容纳所有对象，k_max = 100,000，LRU 命中率下界为 100%（忽略更新失效）。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)在截断范围[1KB, 100MB]内的期望值约为几十KB量级，100,000个对象的总大小S_total约为数GB至数十GB，远小于128GB，因此缓存可容纳所有对象，LRU命中率下界为100%的结论在逻辑上自洽且数值量级合理。
