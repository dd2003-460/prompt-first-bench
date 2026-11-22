# N110: 敏感度衰减系数 β 的非线性修正：β 并非恒定 0.05/元，而是随 C_s 增加而边际递减，即 β(C_s) = β_0 * exp(-C_s/τ_β)，其中

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

敏感度衰减系数 β 的非线性修正：β 并非恒定 0.05/元，而是随 C_s 增加而边际递减，即 β(C_s) = β_0 * exp(-C_s/τ_β)，其中 τ_β ≈ 20 元，表明高搜索成本下弹性下降速度放缓，避免弹性值出现非物理的负值。

## Corrected Claim

敏感度衰减系数 β 随 C_s 增加而边际递减，可采用非线性修正模型（如指数衰减 β(C_s) = β_0 * exp(-C_s/τ_β)）以避免弹性值出现非物理的负值，具体参数需根据实证数据校准。

## Evidence

[质询]该陈述包含具体的经验参数（β_0=0.05, τ_β≈20元）和特定的函数形式（指数衰减），属于经验事实/模型假设，无法从第一性原理严格推导，且缺乏来源支持其具体数值和形式的合理性。 | 经验事实，逻辑自洽（指数衰减函数在数学上能避免负值且符合边际递减直觉），但缺来源支持具体参数和模型形式。

## Search Query

non-linear relationship search cost price elasticity consumer behavior
