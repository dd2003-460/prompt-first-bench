# N316: 噪声对 P99 延迟的尾部风险贡献：P99 延迟中由噪声引起的分量 L_p99_noise ≈ 1.28 * σ_L，其中 σ_L 为延迟分布的标准差，σ_L 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N103

## Claim

噪声对 P99 延迟的尾部风险贡献：P99 延迟中由噪声引起的分量 L_p99_noise ≈ 1.28 * σ_L，其中 σ_L 为延迟分布的标准差，σ_L ≈ L_backhaul * σ_H / H_steady（线性近似）；若 L_backhaul=100ms, H_steady=0.85, σ_H=0.03，则 σ_L ≈ 3.5ms，L_p99_noise ≈ 4.5ms，需从总 P99 预算中扣除。

## Corrected Claim

噪声对 P99 延迟的尾部风险贡献：P99 延迟中由噪声引起的分量 L_p99_noise ≈ 1.28 * σ_L，其中 σ_L 为延迟分布的标准差，σ_L ≈ L_backhaul * σ_H / H_steady（线性近似）；若 L_backhaul=100ms, H_steady=0.85, σ_H=0.03，则 σ_L ≈ 3.5ms，L_p99_noise ≈ 4.5ms，需从总 P99 预算中扣除。

## Evidence

先验知识/题面给定，逻辑校验通过：1.28为P99对应的Z分数（正态分布近似），数值计算1.28*3.5≈4.48与4.5一致，线性近似公式量纲合理。

## Search Query

p99 latency contribution from gaussian noise standard deviation
