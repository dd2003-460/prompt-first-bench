# N170: 若 w3 > 0.4，则高价快销商品在排序中的得分提升幅度 ΔScore/Score_base ≈ (w3 * ΔVelocity) / (w1*Recency

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49, N50, N51

## Claim

若 w3 > 0.4，则高价快销商品在排序中的得分提升幅度 ΔScore/Score_base ≈ (w3 * ΔVelocity) / (w1*Recency + w2*Price + w3*Velocity)，其中 ΔVelocity 为成交速度提升带来的加分，需量化 ΔVelocity 的具体数值（如每缩短 1 天成交周期，Velocity 增加 0.1 分）。

## Corrected Claim

若 w3 > 0.4，则高价快销商品在排序中的得分提升幅度 ΔScore/Score_base ≈ (w3 * ΔVelocity) / (w1*Recency + w2*Price + w3*Velocity)，其中 ΔVelocity 为成交速度提升带来的加分，需量化 ΔVelocity 的具体数值（如每缩短 1 天成交周期，Velocity 增加 0.1 分）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

ranking score improvement velocity metric e-commerce
