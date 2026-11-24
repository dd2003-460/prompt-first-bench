# N343: 蒙特卡洛采样收敛性的标准误计算公式：SE_n = σ_population / sqrt(n)，其中 σ_population 为单次采样成本的标准差（需通过前

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N109

## Claim

蒙特卡洛采样收敛性的标准误计算公式：SE_n = σ_population / sqrt(n)，其中 σ_population 为单次采样成本的标准差（需通过前 100 次采样估计），n 为当前迭代次数；该公式用于量化置信区间的宽度，是判断 n=500 是否满足 1% 波动阈值的数学基础

## Corrected Claim

蒙特卡洛采样收敛性的标准误计算公式：SE_n = σ_population / sqrt(n)，其中 σ_population 为单次采样成本的标准差（需通过前 100 次采样估计），n 为当前迭代次数；该公式用于量化置信区间的宽度，是判断 n=500 是否满足 1% 波动阈值的数学基础

## Evidence

先验知识/题面给定，逻辑校验通过：该公式为统计学中样本均值标准误（Standard Error of the Mean）的标准定义，量纲与逻辑自洽，且蒙特卡洛方法中利用前若干次采样估计总体标准差以构建置信区间是标准工程实践。
