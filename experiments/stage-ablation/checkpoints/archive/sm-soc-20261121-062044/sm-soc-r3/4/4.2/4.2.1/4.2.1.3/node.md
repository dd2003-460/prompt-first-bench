# N200: 高成本低性工作点：完全行为模型拟合，使用 MLE 同时估计 λ, γ, α_ref，目标函数为最小化 RSS = Σ(U_observed - U_model(

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

高成本低性工作点：完全行为模型拟合，使用 MLE 同时估计 λ, γ, α_ref，目标函数为最小化 RSS = Σ(U_observed - U_model(λ, γ, α_ref))²；若模型收敛且 AIC 比简化模型低 > 10，则接受复杂模型；否则回退至 λ=1.25 并标注置信度 0.4，因参数不可辨识。

## Corrected Claim

高成本低性工作点：完全行为模型拟合，使用 MLE 估计参数，若模型收敛且 AIC 显著优于简化模型（如差值超过常见阈值），则接受复杂模型；否则回退至预设默认参数并标注低置信度，因参数不可辨识。

## Evidence

[质询]该陈述包含具体的经验性阈值（AIC差值>10）和特定的回退参数（λ=1.25, 置信度0.4），这些属于特定模型或领域的经验设定，无法从第一性原理严格推导，且缺乏来源支持其具体数值的合理性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

maximum likelihood estimation prospect theory parameters lambda gamma reference point AIC comparison
