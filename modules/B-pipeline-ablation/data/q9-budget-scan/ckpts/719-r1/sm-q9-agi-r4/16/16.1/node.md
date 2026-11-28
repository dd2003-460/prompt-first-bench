# N335: 贝叶斯风险最小化模型中，总期望成本函数定义为 E[C] = C_Human × P(Error | HighRisk) × N_Total × r_High +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

贝叶斯风险最小化模型中，总期望成本函数定义为 E[C] = C_Human × P(Error | HighRisk) × N_Total × r_High + C_Human × P(Error | LowRisk) × N_Total × r_Low，其中 C_Human 为单次人工审查修复成本，r 为抽查率，P(Error) 为模型在该风险等级下的基础错误率

## Corrected Claim

贝叶斯风险最小化模型中，总期望成本函数定义为 E[C] = C_Human × P(Error | HighRisk) × N_Total × r_High + C_Human × P(Error | LowRisk) × N_Total × r_Low，其中 C_Human 为单次人工审查修复成本，r 为抽查率，P(Error) 为模型在该风险等级下的基础错误率

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Bayesian risk minimization sampling inspection cost function
