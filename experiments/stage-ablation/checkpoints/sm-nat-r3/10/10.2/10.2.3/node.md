# N184: LFU 频率统计滞后项：LFU 维护的频率计数器需要时间收敛到真实热度。定义收敛时间常数 τ_conv = 1/λ_avg，其中 λ_avg 是对象的平均访问率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

LFU 频率统计滞后项：LFU 维护的频率计数器需要时间收敛到真实热度。定义收敛时间常数 τ_conv = 1/λ_avg，其中 λ_avg 是对象的平均访问率。当漂移速率 δ > 1/τ_conv 时，LFU 性能衰减显著。量化滞后误差 ΔH_lag ≈ δ * τ_conv * (H_target - H_current)。

## Corrected Claim

LFU 频率统计滞后项：LFU 维护的频率计数器需要时间收敛到真实热度。定义收敛时间常数 τ_conv = 1/λ_avg，其中 λ_avg 是对象的平均访问率。当漂移速率 δ > 1/τ_conv 时，LFU 性能衰减显著。量化滞后误差 ΔH_lag ≈ δ * τ_conv * (H_target - H_current)。

## Evidence

先验知识/题面给定，逻辑校验通过
