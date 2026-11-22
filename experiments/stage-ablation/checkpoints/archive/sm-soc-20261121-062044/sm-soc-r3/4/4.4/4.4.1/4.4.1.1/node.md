# N216: CTR 回归模型的特征工程定义：标准化系数 β_high 需基于 Logit 回归模型 P(click) = σ(β_0 + β_high * (P_list/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

CTR 回归模型的特征工程定义：标准化系数 β_high 需基于 Logit 回归模型 P(click) = σ(β_0 + β_high * (P_list/P_avg - 1) + Σβ_k * X_k)，其中 X_k 为控制变量（类目 One-hot 编码、卖家信誉分标准化值），β_high 的估计需通过 MLE 求解，且需检查多重共线性 VIF < 5。

## Corrected Claim

CTR 回归模型的特征工程定义：标准化系数 β_high 需基于 Logit 回归模型 P(click) = σ(β_0 + β_high * (P_list/P_avg - 1) + Σβ_k * X_k)，其中 X_k 为控制变量（类目 One-hot 编码、卖家信誉分标准化值），β_high 的估计需通过 MLE 求解，且需检查多重共线性 VIF < 5。

## Evidence

先验知识/题面给定，逻辑校验通过：Logit回归模型定义、MLE估计方法、VIF<5的多重共线性检查标准均符合统计学与机器学习工程规范，无逻辑矛盾。

## Search Query

CTR model logit regression standardized coefficient markup premium feature engineering
