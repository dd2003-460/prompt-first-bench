# N147: 修正后的字节命中率 H_corrected = H_independent * (1 + δ)，其中 δ 为负相关带来的修正因子，需通过数值积分 ∫∫ f(S,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

修正后的字节命中率 H_corrected = H_independent * (1 + δ)，其中 δ 为负相关带来的修正因子，需通过数值积分 ∫∫ f(S,F) * hit(S,F) dS dF 计算，hit(S,F) 为条件命中率。

## Corrected Claim

修正后的字节命中率 H_corrected = H_independent * (1 + δ)，其中 δ 为负相关带来的修正因子，需通过数值积分 ∫∫ f(S,F) * hit(S,F) dS dF 计算，hit(S,F) 为条件命中率。

## Evidence

先验知识/题面给定，逻辑校验通过
