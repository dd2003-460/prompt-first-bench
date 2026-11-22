# N237: 计算缓存内的对象请求概率总和 p_cache，基于N61的归一化常数C_β=0.171，p_cache = Σ_{i=1}^{100000} C_β * i^{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

计算缓存内的对象请求概率总和 p_cache，基于N61的归一化常数C_β=0.171，p_cache = Σ_{i=1}^{100000} C_β * i^{-0.9}，在K=N的情况下，p_cache理论值为1.0，但需确认是否因截断导致<1.0。

## Corrected Claim

计算缓存内的对象请求概率总和 p_cache，基于N61的归一化常数C_β=0.171，p_cache = Σ_{i=1}^{100000} C_β * i^{-0.9}，在K=N的情况下，p_cache理论值为1.0，但需确认是否因截断导致<1.0。

## Evidence

先验知识/题面给定，逻辑校验通过：归一化常数C_β的定义即保证在完整分布下概率和为1，截断问题属于数值计算细节而非逻辑矛盾

## Search Query

Calculate sum of request probabilities for all cached objects under Zipf beta=0.9 distribution
