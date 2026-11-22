# N292: 在集中更新工作点下，D_update ≈ 1 - p_hot * (1 - exp(-λ_hot * T_res_hot))，其中 p_hot=0.891，λ_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

在集中更新工作点下，D_update ≈ 1 - p_hot * (1 - exp(-λ_hot * T_res_hot))，其中 p_hot=0.891，λ_hot=0.1/day，T_res_hot=1h，计算得 D_update ≈ 0.9963，量化了热点失效场景下的命中率折损上限。

## Corrected Claim

在集中更新工作点下，D_update ≈ 1 - p_hot * (1 - exp(-λ_hot * T_res_hot))，其中 p_hot=0.891，λ_hot=0.1/day，T_res_hot=1h，计算得 D_update ≈ 0.9963，量化了热点失效场景下的命中率折损上限。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合指数衰减模型，数值代入计算准确（1 - 0.891 * (1 - exp(-0.1/24)) ≈ 0.9963），量纲与逻辑自洽。
