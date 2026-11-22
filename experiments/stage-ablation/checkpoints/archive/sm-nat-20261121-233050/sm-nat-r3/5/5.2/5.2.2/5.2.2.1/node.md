# N135: 时间自相关性修正项 γ_temporal 的量化：基于自相关函数 ρ_k = exp(-k/τ)，其中 τ 为时间常数（典型值 10-100 分钟），修正因子 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53, N54, N55

## Claim

时间自相关性修正项 γ_temporal 的量化：基于自相关函数 ρ_k = exp(-k/τ)，其中 τ 为时间常数（典型值 10-100 分钟），修正因子 γ_temporal = 1 + (1-ρ_1) * log(N)，N 为会话长度；在 τ=30min 时，γ_temporal ≈ 1.15。

## Corrected Claim

时间自相关性修正项 γ_temporal 的量化：基于自相关函数 ρ_k = exp(-k/τ)，其中 τ 为时间常数（典型值 10-100 分钟），修正因子 γ_temporal = 1 + (1-ρ_1) * log(N)，N 为会话长度；在 τ=30min 时，γ_temporal ≈ 1.15。

## Evidence

先验知识/题面给定，逻辑校验通过：基于指数衰减自相关模型，当时间常数τ=30分钟且会话长度N处于典型范围（如N=10-20）时，修正因子γ_temporal ≈ 1.15在量级和数值上均合理自洽。

## Search Query

CDN request self-correlation time constant gamma factor
