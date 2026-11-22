# N371: 损失厌恶系数 λ 的估计模型设定：采用固定效应回归模型 P_ask - P_min = α + λ * (P_ref - P_min) + γ * X_cont

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125, N126, N127

## Claim

损失厌恶系数 λ 的估计模型设定：采用固定效应回归模型 P_ask - P_min = α + λ * (P_ref - P_min) + γ * X_controls + ε，其中 X_controls 包含卖家历史成交率、商品成色评分、挂牌时长；需明确该模型中 λ 的系数解释为边际损失厌恶敏感度，且需验证残差 ε 是否服从正态分布（Shapiro-Wilk 检验 p > 0.05）。

## Corrected Claim

损失厌恶系数 λ 的估计模型设定：采用固定效应回归模型 P_ask - P_min = α + λ * (P_ref - P_min) + γ * X_controls + ε，其中 X_controls 包含卖家历史成交率、商品成色评分、挂牌时长；需明确该模型中 λ 的系数解释为边际损失厌恶敏感度，且需验证残差 ε 是否服从正态分布（Shapiro-Wilk 检验 p > 0.05）。

## Evidence

先验知识/题面给定，逻辑校验通过：模型设定符合计量经济学规范，Shapiro-Wilk检验用于正态性假设验证逻辑正确，系数解释与损失厌恶理论一致。
