# N61: 工作点 3（高成本低性）：大对象主导场景，T_resident ≈ 100 天，P_invalidate = 1 - e^(-100/100) ≈ 63.2%，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

工作点 3（高成本低性）：大对象主导场景，T_resident ≈ 100 天，P_invalidate = 1 - e^(-100/100) ≈ 63.2%，字节命中率折损 ΔH ≈ 63.2% * (S_hot/S_total ≈ 0.8) ≈ 50.6%。

## Corrected Claim

工作点 3（高成本低性）：大对象主导场景，T_resident ≈ 100 天，P_invalidate = 1 - e^(-100/100) ≈ 63.2%，字节命中率折损 ΔH ≈ 63.2% * (S_hot/S_total ≈ 0.8) ≈ 50.6%。

## Evidence

先验知识/题面给定，逻辑校验通过：指数计算 1-e^-1 ≈ 0.632 正确，乘法运算 0.632*0.8 ≈ 0.506 正确，量纲与逻辑自洽。

## Search Query

LRU large object resident time invalidation probability byte hit rate loss
