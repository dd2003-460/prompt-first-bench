# N144: 时间局部性的量化边界条件：局部性仅在访问间隔 Δt < T_res（缓存驻留时间，约 3.3 分钟，见 N53）时才对 LRU 命中率产生正面贡献。若 Δt >

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

时间局部性的量化边界条件：局部性仅在访问间隔 Δt < T_res（缓存驻留时间，约 3.3 分钟，见 N53）时才对 LRU 命中率产生正面贡献。若 Δt > T_res，对象已被驱逐，重复访问导致 Miss。因此，有效的局部性窗口 τ_eff = min(1天, T_res)。在 τ_eff 内，P(repeat | recent) = 1 - exp(-λ_r * τ_eff)，其中 λ_r 为对象的瞬时请求率。对于 Top-100 对象，λ_r 极高，局部性效应显著；对于尾部对象，λ_r 极低，局部性效应可忽略。

## Corrected Claim

时间局部性的量化边界条件：局部性仅在访问间隔 Δt < T_res（缓存驻留时间，约 3.3 分钟，见 N53）时才对 LRU 命中率产生正面贡献。若 Δt > T_res，对象已被驱逐，重复访问导致 Miss。因此，有效的局部性窗口 τ_eff = min(1天, T_res)。在 τ_eff 内，P(repeat | recent) = 1 - exp(-λ_r * τ_eff)，其中 λ_r 为对象的瞬时请求率。对于 Top-100 对象，λ_r 极高，局部性效应显著；对于尾部对象，λ_r 极低，局部性效应可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache hit rate time locality window inter-arrival time
