# N60: 工作点 2（中性价比最优）：混合对象场景，T_resident ≈ 10 天，P_invalidate = 1 - e^(-10/100) ≈ 9.5%，字节命

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

工作点 2（中性价比最优）：混合对象场景，T_resident ≈ 10 天，P_invalidate = 1 - e^(-10/100) ≈ 9.5%，字节命中率折损 ΔH ≈ 9.5% * (S_hot/S_total ≈ 0.5) ≈ 4.75%。

## Corrected Claim

工作点 2（中性价比最优）：混合对象场景，T_resident ≈ 10 天，P_invalidate = 1 - e^(-10/100) ≈ 9.5%，字节命中率折损 ΔH ≈ 9.5% * (S_hot/S_total ≈ 0.5) ≈ 4.75%。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布失效概率公式 P=1-e^(-t/λ) 计算正确 (1-e^-0.1≈9.5%)，加权折损逻辑自洽 (9.5%*0.5=4.75%)，数值量级合理。

## Search Query

LRU mixed object resident time invalidation probability byte hit rate loss
