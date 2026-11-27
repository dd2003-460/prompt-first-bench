# N46: 买家支付意愿分布参数 μ_W = P_ref * (1 + μ_δ) 且 σ_W = P_ref * σ_δ，其中 P_ref 为参考成交价，需基于平台历史成交

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

买家支付意愿分布参数 μ_W = P_ref * (1 + μ_δ) 且 σ_W = P_ref * σ_δ，其中 P_ref 为参考成交价，需基于平台历史成交数据回归得出 μ_δ 和 σ_δ 的具体值

## Corrected Claim

买家支付意愿分布参数通常基于参考成交价 P_ref 进行建模，具体参数 μ_W 和 σ_W 需结合所选分布假设（如对数正态分布）及平台历史成交数据回归得出，常见形式为基于相对偏差 δ 的线性或指数映射。

## Evidence

[质询]该陈述将具体的参数化公式（μ_W = P_ref * (1 + μ_δ) 且 σ_W = P_ref * σ_δ）作为既定事实，但这属于特定的建模假设（通常基于对数正态分布或线性近似），并非经济学或统计学中的普适第一性原理。不同的分布假设（如对数正态分布的几何均值/标准差关系）会导致不同的参数映射公式，因此该具体公式的普适性存疑，且缺乏来源支持其作为唯一或标准解法。 | 经验事实/建模假设，逻辑自洽（量纲一致，基于参考价的相对偏差建模符合直觉），但检索无可用来源，且该具体公式非第一性原理必然推导，属于特定模型设定，故降级。

## Search Query

willingness to pay distribution parameters second hand goods market price variance
