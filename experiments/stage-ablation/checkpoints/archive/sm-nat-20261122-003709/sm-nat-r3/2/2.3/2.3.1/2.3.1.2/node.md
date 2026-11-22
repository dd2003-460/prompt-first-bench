# N145: 验证 D_LFU 公式的有效性边界：原公式 D_LFU ≈ (1 - λ_update) * (1 - β) * 5% 在 λ_update * T_resid

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N47

## Claim

验证 D_LFU 公式的有效性边界：原公式 D_LFU ≈ (1 - λ_update) * (1 - β) * 5% 在 λ_update * T_resident < 0.1 时近似成立。当 T_age (100 days) 远大于对象平均驻留时间 T_resident (约 1-2 days，基于 N89) 时，LFU 计数器在对象被驱逐前无法收敛，导致 D_LFU 实际接近 1.0（无退化），而非公式预测的低值。需修正公式为 D_LFU = 1 - exp(-T_resident / T_age)。

## Corrected Claim

在缺乏具体系统参数验证的情况下，D_LFU 的退化程度取决于 LFU 计数器收敛时间与对象驻留时间的比值；当驻留时间远小于老化时间时，LFU 可能无法准确反映访问频率，导致退化行为，具体量化需依赖实测数据或特定模型验证。

## Evidence

[质询]该陈述包含具体的经验参数（T_age=100 days, T_resident=1-2 days）和特定的数学修正公式（D_LFU = 1 - exp(-T_resident / T_age)），这些属于经验事实或特定模型假设，无法仅从第一性原理严格推导，且缺乏外部来源支持其具体数值和公式形式的正确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

LFU frequency counter convergence time vs cache residency time mismatch
