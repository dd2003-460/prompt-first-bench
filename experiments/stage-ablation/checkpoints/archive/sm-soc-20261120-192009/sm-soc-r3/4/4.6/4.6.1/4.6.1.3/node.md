# N272: 蒙特卡洛模拟收敛性检验：记录每次迭代的 U_platform 序列，计算自相关系数 ρ_k；若 ρ_k > 0.5 且 k < 10，则模拟未收敛，需增加迭代次

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

蒙特卡洛模拟收敛性检验：记录每次迭代的 U_platform 序列，计算自相关系数 ρ_k；若 ρ_k > 0.5 且 k < 10，则模拟未收敛，需增加迭代次数至 N=50,000 或使用方差缩减技术（如控制变量法）以降低标准误。

## Corrected Claim

蒙特卡洛模拟收敛性检验：记录每次迭代的 U_platform 序列，计算自相关系数 ρ_k；若 ρ_k > 0.5 且 k < 10，则模拟未收敛，需增加迭代次数至 N=50,000 或使用方差缩减技术（如控制变量法）以降低标准误。

## Evidence

先验知识/题面给定，逻辑校验通过
