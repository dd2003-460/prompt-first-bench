# N185: 权重 α 和 β 的回归拟合方法：收集 50 组历史任务的 (Depth_CoT, Scope_Retrieval, Actual_Accuracy) 三元组，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

权重 α 和 β 的回归拟合方法：收集 50 组历史任务的 (Depth_CoT, Scope_Retrieval, Actual_Accuracy) 三元组，使用 Ridge 回归 (λ=1.0) 拟合 Accuracy = w0 - α*Depth - β*Scope，最小化均方误差；若 R² < 0.6，则引入交互项 γ*Depth*Scope 重新拟合，并报告各系数的 p 值以确认显著性。

## Corrected Claim

权重 α 和 β 的回归拟合方法：收集 50 组历史任务的 (Depth_CoT, Scope_Retrieval, Actual_Accuracy) 三元组，使用 Ridge 回归 (λ=1.0) 拟合 Accuracy = w0 - α*Depth - β*Scope，最小化均方误差；若 R² < 0.6，则引入交互项 γ*Depth*Scope 重新拟合，并报告各系数的 p 值以确认显著性。

## Evidence

先验知识/题面给定，逻辑校验通过：Ridge回归用于线性拟合及基于R²阈值引入交互项是标准的统计学建模流程，逻辑自洽且无内部矛盾。
