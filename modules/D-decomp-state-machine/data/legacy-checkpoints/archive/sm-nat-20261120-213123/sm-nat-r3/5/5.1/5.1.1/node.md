# N59: 工作点 1（高性低成）：小对象主导场景，T_resident ≈ 1 天，P_invalidate = 1 - e^(-1/100) ≈ 0.995%，字节命中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

工作点 1（高性低成）：小对象主导场景，T_resident ≈ 1 天，P_invalidate = 1 - e^(-1/100) ≈ 0.995%，字节命中率折损 ΔH ≈ 0.995% * (S_hot/S_total ≈ 0.3) ≈ 0.3%。

## Corrected Claim

工作点 1（高性低成）：小对象主导场景，T_resident ≈ 1 天，P_invalidate = 1 - e^(-1/100) ≈ 0.995%，字节命中率折损 ΔH ≈ 0.995% * (S_hot/S_total ≈ 0.3) ≈ 0.3%。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布失效概率公式 P=1-e^(-t/λ) 计算正确，字节命中率折损逻辑自洽。

## Search Query

LRU small object resident time invalidation probability byte hit rate loss
