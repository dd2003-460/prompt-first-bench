# N136: 观察变量方差 Var(T_deal_observed) 的分解：计算总方差并分解为模型解释部分和残差部分；若 Var(Residual) / Var(T_dea

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

观察变量方差 Var(T_deal_observed) 的分解：计算总方差并分解为模型解释部分和残差部分；若 Var(Residual) / Var(T_deal_observed) > 0.4（即 R² < 0.6），则需检查是否遗漏关键混淆变量（如卖家信用分、商品成色），并引入控制变量重新拟合模型。

## Corrected Claim

观察变量方差 Var(T_deal_observed) 的分解：计算总方差并分解为模型解释部分和残差部分；若 Var(Residual) / Var(T_deal_observed) > 0.4（即 R² < 0.6），则需检查是否遗漏关键混淆变量（如卖家信用分、商品成色），并引入控制变量重新拟合模型。

## Evidence

先验知识/题面给定，逻辑校验通过：方差分解公式 Var(Y) = Var(Ŷ) + Var(ε) 在经典线性模型假设下成立，R² 定义为 1 - Var(Residual)/Var(Y)，阈值 0.4 对应 R² < 0.6 的逻辑推导正确，且检查混淆变量是标准的模型诊断步骤。

## Search Query

variance decomposition regression model misspecification check
