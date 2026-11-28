# N135: ROC 曲线离散化的平滑处理：由于样本量 n=200 较小，直接计算 F1-score 最大化点可能导致过拟合。采用 Logistic Regression 拟

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

ROC 曲线离散化的平滑处理：由于样本量 n=200 较小，直接计算 F1-score 最大化点可能导致过拟合。采用 Logistic Regression 拟合 ROC 曲线，使用 Leave-One-Out Cross-Validation (LOOCV) 评估阈值 τ_opt 的泛化误差，标准误 SE_τ = sqrt(Var(τ)/n)。

## Corrected Claim

ROC 曲线离散化的平滑处理：由于样本量 n=200 较小，直接计算 F1-score 最大化点可能导致过拟合。采用 Logistic Regression 拟合 ROC 曲线，使用 Leave-One-Out Cross-Validation (LOOCV) 评估阈值 τ_opt 的泛化误差，标准误 SE_τ = sqrt(Var(τ)/n)。

## Evidence

先验知识/题面给定，逻辑校验通过：ROC曲线平滑处理及LOOCV评估阈值泛化误差的方法论在统计学上是自洽的，标准误公式符合大数定律下的抽样分布近似。

## Search Query

ROC curve smoothing logistic regression LOOCV small sample threshold optimization
