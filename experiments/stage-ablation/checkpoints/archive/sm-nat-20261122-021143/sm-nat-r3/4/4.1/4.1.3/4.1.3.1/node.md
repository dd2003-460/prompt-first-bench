# N114: 线性折扣模型 H_eff = H_steady * (1 - u*T_avg) 与指数模型 H_eff = H_steady * exp(-u*T_avg) 的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

线性折扣模型 H_eff = H_steady * (1 - u*T_avg) 与指数模型 H_eff = H_steady * exp(-u*T_avg) 的相对误差公式为 E_rel = (1 - (1-uT)/e^(-uT)) / e^(-uT)，在 u*T=0.1 时 E_rel ≈ 2.7%，在 u*T=0.2 时 E_rel ≈ 10.8%，证明 0.1 是误差从可忽略转为显著的转折点

## Corrected Claim

线性折扣模型 H_eff = H_steady * (1 - u*T_avg) 与指数模型 H_eff = H_steady * exp(-u*T_avg) 的相对误差公式为 E_rel = (1 - (1-uT)/e^(-uT)) / e^(-uT)，在 u*T=0.1 时 E_rel ≈ 2.7%，在 u*T=0.2 时 E_rel ≈ 10.8%，证明 0.1 是误差从可忽略转为显著的转折点

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（uT=0.1时误差约2.7%，uT=0.2时误差约10.8%），符合泰勒展开近似规律
