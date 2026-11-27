# N172: 降价后CTR衰减函数 CTR_post = CTR_base * e^(-λ_drop * ΔP/P_ref) 中衰减系数 λ_drop 的估计：需基于平台A/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

降价后CTR衰减函数 CTR_post = CTR_base * e^(-λ_drop * ΔP/P_ref) 中衰减系数 λ_drop 的估计：需基于平台A/B测试数据或自然实验数据，回归计算降价幅度 ΔP 对CTR的非线性影响；若缺乏公开数据，需给出基于损失厌恶系数 λ=2.25 推导的理论预期范围，并标注置信度 < 0.5。

## Corrected Claim

降价后CTR衰减函数 CTR_post = CTR_base * e^(-λ_drop * ΔP/P_ref) 中衰减系数 λ_drop 的估计：需基于平台A/B测试数据或自然实验数据，回归计算降价幅度 ΔP 对CTR的非线性影响；若缺乏公开数据，需给出基于行为经济学理论（如损失厌恶）推导的理论预期范围，并标注置信度 < 0.5。

## Evidence

[质询]该陈述将CTR衰减建模为指数函数并直接关联损失厌恶系数λ=2.25，缺乏明确的理论推导路径或实证支持，属于经验性假设而非第一性原理可推导事实。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

price reduction click-through rate decay function second hand marketplace empirical study
