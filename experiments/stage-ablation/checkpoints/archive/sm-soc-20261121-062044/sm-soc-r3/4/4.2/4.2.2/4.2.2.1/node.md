# N201: 高解释力工作点：当 Var(P_markup | λ) / Var(P_markup_total) > 0.8 时，损失厌恶主导，置信度 0.85；需验证残差分

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

高解释力工作点：当 Var(P_markup | λ) / Var(P_markup_total) > 0.8 时，损失厌恶主导，置信度 0.85；需验证残差分布是否正态（Shapiro-Wilk p > 0.05），若非正态，则改用非参数 bootstrap 估计置信区间，置信度上限降至 0.75，因正态假设失效。

## Corrected Claim

高解释力工作点：当 Var(P_markup | λ) / Var(P_markup_total) > 0.8 时，损失厌恶主导，置信度 0.85；需验证残差分布是否正态（Shapiro-Wilk p > 0.05），若非正态，则改用非参数 bootstrap 估计置信区间，置信度上限降至 0.75，因正态假设失效。

## Evidence

先验知识/题面给定，逻辑校验通过：方差解释率阈值0.8符合高解释力工作点定义，Shapiro-Wilk检验用于正态性判断，非正态时改用非参数bootstrap并降低置信度上限符合统计推断规范。
