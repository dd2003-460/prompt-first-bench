# N291: 在均匀更新工作点下，D_update ≈ 1 - λ_update * T_res_avg，其中 T_res_avg 由 N100 给出，若 T_res_avg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

在均匀更新工作点下，D_update ≈ 1 - λ_update * T_res_avg，其中 T_res_avg 由 N100 给出，若 T_res_avg = 1h，则 D_update ≈ 0.99959，量化了均匀失效场景下的命中率折损下界。

## Corrected Claim

在均匀更新工作点下，D_update ≈ 1 - λ_update * T_res_avg，其中 T_res_avg 由 N100 给出，若 T_res_avg = 1h，则 D_update ≈ 0.99959，量化了均匀失效场景下的命中率折损下界。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 D = 1 - λT 符合均匀分布下存活概率/命中率的标准定义，数值计算 1 - 0.00041 = 0.99959 准确，量纲与逻辑自洽。
