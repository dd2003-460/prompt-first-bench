# N240: 锚定效应效应量 d 对收敛速度的修正项：若 d_platform > 0.8（强锚定），则需引入修正因子 f(d) = 1 + (d - 0.5) * k_co

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79, N80, N81

## Claim

锚定效应效应量 d 对收敛速度的修正项：若 d_platform > 0.8（强锚定），则需引入修正因子 f(d) = 1 + (d - 0.5) * k_correction，其中 k_correction 为锚定强度对惰性放大的系数（估计 k_correction ≈ 0.5-1.0）；该修正项导致 λ_transparency 降低，从而延长收敛时间，需量化 d 每增加 0.1 对 T_convergence 的边际影响。

## Corrected Claim

锚定效应效应量 d 对收敛速度的修正项：若 d_platform > 0.8（强锚定），需引入修正因子 f(d) 以反映锚定强度对惰性的放大作用；该修正项导致 λ_transparency 降低，从而延长收敛时间，需量化 d 对 T_convergence 的边际影响。

## Evidence

[质询]该陈述包含具体的经验参数（k_correction ≈ 0.5-1.0）和特定的函数形式（线性修正），这些属于行为经济学/心理学中的经验事实或模型假设，无法从第一性原理严格推导，且缺乏来源支持其具体数值范围。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

anchoring effect strength correction factor price adjustment
