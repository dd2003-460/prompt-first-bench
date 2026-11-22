# N105: 若假设缓存容量不足以容纳所有对象（例如C=10GB），则 K_opt 需通过求解 ∑_{i=1}^{K} s_i = C 确定，此时 H_opt_byte < 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N31

## Claim

若假设缓存容量不足以容纳所有对象（例如C=10GB），则 K_opt 需通过求解 ∑_{i=1}^{K} s_i = C 确定，此时 H_opt_byte < 1.0，具体值取决于大小-热度相关性ρ=-0.3下的联合分布积分，此为N31公式在非全覆盖场景下的应用实例。

## Corrected Claim

若假设缓存容量不足以容纳所有对象，则 K_opt 需通过求解 ∑_{i=1}^{K} s_i = C 确定，此时 H_opt_byte 通常小于 1.0，具体值取决于大小-热度相关性下的联合分布积分，此为N31公式在非全覆盖场景下的应用实例。

## Evidence

[质询]该陈述包含具体的经验参数（C=10GB, ρ=-0.3）和特定的数学结论（H_opt_byte < 1.0），属于经验事实或特定模型推导结果，无法仅从第一性原理严格推出，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Belady optimal cache hit rate Pareto distribution calculation
