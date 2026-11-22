# N95: 在 ρ=-0.3 的负相关下，P(S < s_median | R > r_median) - P(S < s_median) 的量化值反映条件概率偏移，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

在 ρ=-0.3 的负相关下，P(S < s_median | R > r_median) - P(S < s_median) 的量化值反映条件概率偏移，其中 s_median 和 r_median 分别是大小和热度的中位数，该差值用于衡量负相关对缓存驻留策略的具体影响幅度 [knowledge: 数学推导]

## Corrected Claim

在 ρ=-0.3 的负相关下，P(S < s_median | R > r_median) - P(S < s_median) 的量化值反映条件概率偏移，其中 s_median 和 r_median 分别是大小和热度的中位数，该差值用于衡量负相关对缓存驻留策略的具体影响幅度 [knowledge: 数学推导]

## Evidence

先验知识/题面给定，逻辑校验通过：该差值在数学上严格定义为条件概率与边缘概率之差，用于量化负相关（ρ=-0.3）导致的分布偏移，逻辑自洽且量纲正确（概率差值）。
