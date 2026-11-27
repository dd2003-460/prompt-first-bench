# N271: 点击率数据的独立性假设检验：计算相邻两次点击事件的自相关系数ρ_1 = Cov(x_t, x_{t-1})/Var(x)，若|ρ_1| > 0.2则违反独立性假

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

点击率数据的独立性假设检验：计算相邻两次点击事件的自相关系数ρ_1 = Cov(x_t, x_{t-1})/Var(x)，若|ρ_1| > 0.2则违反独立性假设，Beta分布拟合无效，需改用AR(1)误差模型修正

## Corrected Claim

点击率数据的独立性假设检验：计算相邻两次点击事件的自相关系数ρ_1 = Cov(x_t, x_{t-1})/Var(x)，若|ρ_1| > 0.2则违反独立性假设，Beta分布拟合无效，需改用AR(1)误差模型修正

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

click stream autocorrelation test independence assumption beta distribution
