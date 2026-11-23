# N149: 混合策略中跨域同步/回源成本 C_sync_cross = (1-θ) * V_daily * p_sync + C_origin_load，其中 (1-θ)≈

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

混合策略中跨域同步/回源成本 C_sync_cross = (1-θ) * V_daily * p_sync + C_origin_load，其中 (1-θ)≈0.28，V_daily=2TB，p_sync≈¥0.1-0.3/GB（跨域骨干网传输成本），C_origin_load≈¥5k-10k/月（源站额外负载分摊），故 C_sync_cross ≈ ¥16k-168k/月

## Corrected Claim

混合策略中跨域同步/回源成本 C_sync_cross = (1-θ) * V_daily * p_sync + C_origin_load，其中 (1-θ)≈0.28，V_daily=2TB，p_sync≈¥0.1-0.3/GB（跨域骨干网传输成本），C_origin_load≈¥5k-10k/月（源站额外负载分摊），故 C_sync_cross ≈ ¥16k-168k/月

## Search Query

CDN cross-region origin pull bandwidth cost per GB China 2024
