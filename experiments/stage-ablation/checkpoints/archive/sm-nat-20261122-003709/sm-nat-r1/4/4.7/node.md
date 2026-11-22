# N22: 对象更新率1%/天对LRU命中率的折扣因子D_update = 1 / (1 + λ_update * T_cold)，其中λ_update = 0.01/da

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

对象更新率1%/天对LRU命中率的折扣因子D_update = 1 / (1 + λ_update * T_cold)，其中λ_update = 0.01/day，T_cold为对象在缓存中的平均驻留时间（由请求频率决定）；该折扣因子导致有效命中率H_eff = H_LRU * D_update，具体数值需结合T_cold的分布计算。

## Corrected Claim

对象更新率1%/天对LRU命中率的折扣因子D_update = 1 / (1 + λ_update * T_cold)，其中λ_update = 0.01/day，T_cold为对象在缓存中的平均驻留时间（由请求频率决定）；该折扣因子导致有效命中率H_eff = H_LRU * D_update，具体数值需结合T_cold的分布计算。

## Evidence

先验知识/题面给定，逻辑校验通过
