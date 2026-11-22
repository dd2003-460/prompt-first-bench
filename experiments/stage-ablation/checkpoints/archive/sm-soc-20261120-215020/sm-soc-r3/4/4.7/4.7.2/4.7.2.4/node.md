# N204: P_evo 的微观基础分解：w_profit 和 w_risk 并非独立参数，而是受卖家流动性约束 L_constraint 影响：w_risk = w_ris

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N69, N70, N71

## Claim

P_evo 的微观基础分解：w_profit 和 w_risk 并非独立参数，而是受卖家流动性约束 L_constraint 影响：w_risk = w_risk_base * (1 + γ * L_constraint)，其中 γ 为流动性惩罚系数（估计值 0.5-1.5）；需量化 L_constraint 在二手平台高溢价卖家群体中的分布均值。

## Corrected Claim

P_evo 的微观基础分解中，w_profit 和 w_risk 可能受卖家流动性约束 L_constraint 影响，具体函数形式及系数需通过实证数据量化，而非直接设定固定估计值。

## Evidence

[质询]该陈述包含具体的经验参数（γ 估计值 0.5-1.5）和特定的微观机制假设（w_risk 与 L_constraint 的线性关系），属于经验事实而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

seller liquidity constraint risk aversion coefficient second-hand market empirical estimate
