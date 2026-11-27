# N97: h_min 的理论下界约束：h_min ≥ 1/(N_days * N_obj) = 1/(1 * 100000) = 0.00001 次/天，若 h_min 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

h_min 的理论下界约束：h_min ≥ 1/(N_days * N_obj) = 1/(1 * 100000) = 0.00001 次/天，若 h_min < 0.00001 则违反离散时间粒度定义。

## Corrected Claim

h_min 的理论下界约束：h_min ≥ 1/(N_days * N_obj) = 1/(1 * 100000) = 0.00001 次/天，若 h_min < 0.00001 则违反离散时间粒度定义。

## Evidence

先验知识/题面给定，逻辑校验通过：在离散时间模型中，最小非零频率由时间分辨率（1天）和样本量（N_obj）决定，1/(1*100000) = 1e-5 符合离散粒度定义。
