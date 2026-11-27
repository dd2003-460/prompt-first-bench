# N119: 工作点2（负相关修正）：在 ρ=-0.3 下，高频对象倾向于小尺寸，导致 r_i * s_i 的协方差为负。总字节流量 Total_Bytes_correcte

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37, N38, N39

## Claim

工作点2（负相关修正）：在 ρ=-0.3 下，高频对象倾向于小尺寸，导致 r_i * s_i 的协方差为负。总字节流量 Total_Bytes_corrected = Total_Bytes_independent * (1 + ρ * σ_r * σ_s / (E[r] * E[s]))。由于 Pareto 分布的高方差，修正项幅度可达 -10% 至 -20%，即 Total_Bytes ≈ 1.2 - 1.3 * 10^9 GB/day。此修正直接影响命中率分母，进而影响 H_byte 的计算。

## Corrected Claim

工作点2（负相关修正）：在 ρ=-0.3 下，高频对象倾向于小尺寸，导致 r_i * s_i 的协方差为负。总字节流量 Total_Bytes_corrected = Total_Bytes_independent * (1 + ρ * σ_r * σ_s / (E[r] * E[s]))。由于 Pareto 分布的高方差，修正项幅度通常为负值（具体幅度取决于分布参数，例如可能在 -10% 至 -20% 之间），从而降低总字节流量。此修正直接影响命中率分母，进而影响 H_byte 的计算。

## Evidence

[质询]修正项幅度 -10% 至 -20% 属于经验性数值估计，缺乏具体分布参数（如 Pareto 的 alpha 值）支持，且不同工作负载下该幅度可能显著不同，存在过度泛化风险。 | 逻辑推导成立（协方差修正公式正确），但具体数值幅度（-10%~-20%）及最终流量范围（1.2-1.3 * 10^9 GB/day）为经验事实，无来源支持，且检索失败，故降级。

## Search Query

covariance size frequency negative correlation pareto distribution total byte volume
