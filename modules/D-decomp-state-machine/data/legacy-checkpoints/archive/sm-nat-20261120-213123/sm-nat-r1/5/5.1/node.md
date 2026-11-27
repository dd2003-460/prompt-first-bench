# N20: 动态更新惩罚基线：对象更新率 u=1%/天 意味着每个对象平均寿命 T_obj = 1/u = 100 天。对于LRU，若缓存驻留时间 T_resident >

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

动态更新惩罚基线：对象更新率 u=1%/天 意味着每个对象平均寿命 T_obj = 1/u = 100 天。对于LRU，若缓存驻留时间 T_resident > T_obj，则更新导致的失效概率 P_invalidate = 1 - e^(-T_resident/T_obj)。

## Corrected Claim

动态更新惩罚基线：对象更新率 u=1%/天 意味着每个对象平均寿命 T_obj = 1/u = 100 天。对于LRU，若缓存驻留时间 T_resident > T_obj，则更新导致的失效概率 P_invalidate = 1 - e^(-T_resident/T_obj)。

## Evidence

先验知识/题面给定，逻辑校验通过：对象更新率 u 与平均寿命 T_obj=1/u 互为倒数符合指数分布定义；LRU 缓存中对象在驻留时间 T_resident 内未被更新（即未被淘汰/失效）的概率遵循指数衰减模型 P=1-e^(-t/τ)，此处 τ=T_obj，公式推导自洽且量纲正确。

## Search Query

cache invalidation probability object update rate exponential distribution
