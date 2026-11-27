# N211: 聚集性对折损系数的修正项：δ_corrected = 1 - u * (T_residence / L_object) * (1 + ρ_update * k_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

聚集性对折损系数的修正项：δ_corrected = 1 - u * (T_residence / L_object) * (1 + ρ_update * k_cluster)，其中 k_cluster 为聚集强度系数，通常 k_cluster ≈ 1-2；当 ρ_update = 0.2, k_cluster = 1.5 时，修正因子 = 1 + 0.2 * 1.5 = 1.3，折损增加 30%；[待核验：k_cluster 的具体值需通过仿真标定]

## Corrected Claim

聚集性对折损系数的修正项：δ_corrected = 1 - u * (T_residence / L_object) * (1 + ρ_update * k_cluster)，其中 k_cluster 为聚集强度系数，通常 k_cluster ≈ 1-2；当 ρ_update = 0.2, k_cluster = 1.5 时，修正因子 = 1 + 0.2 * 1.5 = 1.3，折损增加 30%；[待核验：k_cluster 的具体值需通过仿真标定]

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构自洽，数值计算 1 + 0.2 * 1.5 = 1.3 正确，且明确标注了参数需仿真标定，符合工程模型定义规范。
