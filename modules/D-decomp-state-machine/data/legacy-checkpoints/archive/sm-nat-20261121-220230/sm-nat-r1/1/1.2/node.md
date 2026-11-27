# N7: LRU缓存驻留对象集合C的确定规则：按请求频率λ_i降序排列，选取前K个对象，使得Σ_{i=1}^{K} s_i ≤ 128GB且Σ_{i=1}^{K+1} s

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

LRU缓存驻留对象集合C的确定规则：按请求频率λ_i降序排列，选取前K个对象，使得Σ_{i=1}^{K} s_i ≤ 128GB且Σ_{i=1}^{K+1} s_i > 128GB，K为最大可容纳对象数。

## Corrected Claim

LRU缓存驻留对象集合C的确定规则：按请求频率λ_i降序排列，选取前K个对象，使得Σ_{i=1}^{K} s_i ≤ 128GB且Σ_{i=1}^{K+1} s_i > 128GB，K为最大可容纳对象数。

## Evidence

先验知识/题面给定，逻辑校验通过
