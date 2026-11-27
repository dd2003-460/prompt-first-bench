# N146: 大对象的平均驻留时间 T_res > 30 天需量化：T_res = C / (Σ_{i: S_i>1MB} λ_i S_i)，由于 λ_i 服从 Pareto

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

大对象的平均驻留时间 T_res > 30 天需量化：T_res = C / (Σ_{i: S_i>1MB} λ_i S_i)，由于 λ_i 服从 Pareto(β=0.9)，头部大对象 λ_i 极低，导致 T_res 可能 >100 天，需结合具体 λ_i 分布计算精确值，而非仅用 >30 天的定性描述。

## Corrected Claim

大对象的平均驻留时间 T_res 需通过 T_res = C / (Σ_{i: S_i>1MB} λ_i S_i) 量化。若 λ_i 服从 Pareto 分布且头部对象到达率极低，T_res 可能显著超过 30 天（具体数值如 >100 天需结合实测 λ_i 分布验证），建议结合具体分布参数计算精确值，而非仅用定性描述。

## Evidence

[质询]该陈述包含具体的经验性参数（Pareto β=0.9）和推导出的具体数值阈值（>100天），属于经验事实而非纯逻辑推导；且缺乏外部来源支持该特定参数组合下的结论。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Pareto popularity large object request rate residence time
