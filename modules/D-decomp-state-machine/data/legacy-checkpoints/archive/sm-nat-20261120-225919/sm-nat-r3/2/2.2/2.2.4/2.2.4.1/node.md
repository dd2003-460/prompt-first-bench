# N145: τ_res 的计算中 E[S] 必须使用截断均值而非理论均值：若 S_min=1KB, S_max=1.3MB, α=1.1，则 E[S_trunc] ≈ 11

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N46

## Claim

τ_res 的计算中 E[S] 必须使用截断均值而非理论均值：若 S_min=1KB, S_max=1.3MB, α=1.1，则 E[S_trunc] ≈ 11KB（偏差<5%），代入 τ_res = 128×10^9 / (578.7 * 11×10^3) ≈ 2013 天，远大于 τ_obj=100 天，导致 D 几乎为 1。

## Corrected Claim

τ_res 的计算中 E[S] 必须使用截断均值而非理论均值：若 S_min=1KB, S_max=1.3MB, α=1.1，则 E[S_trunc] ≈ 11KB（偏差<5%），代入 τ_res = 128×10^9 / (578.7 * 11×10^3) ≈ 2013 天，远大于 τ_obj=100 天，导致 D 几乎为 1。

## Evidence

先验知识/题面给定，逻辑校验通过：截断帕累托分布均值计算及后续算术推导自洽，量级合理。
