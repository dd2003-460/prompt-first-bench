# N228: 信号被噪声掩盖的临界阈值公式推导：信号清晰度 SNR = (ΔP% * P_market) / (√2 * σ_noise)，当 SNR < 1 时，买家无法在

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

信号被噪声掩盖的临界阈值公式推导：信号清晰度 SNR = (ΔP% * P_market) / (√2 * σ_noise)，当 SNR < 1 时，买家无法在统计上区分高挂价是否为质量信号；代入 σ_noise = 0.10 * P_market，解得临界溢价率 ΔP_crit = √2 * 0.10 * 100% ≈ 14.14%。

## Corrected Claim

信号被噪声掩盖的临界阈值公式推导：信号清晰度 SNR = (ΔP% * P_market) / (√2 * σ_noise)，当 SNR < 1 时，买家无法在统计上区分高挂价是否为质量信号；代入 σ_noise = 0.10 * P_market，解得临界溢价率 ΔP_crit = √2 * 0.10 * 100% ≈ 14.14%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合代数逻辑，数值计算 √2 * 0.10 * 100% ≈ 14.14% 准确无误。
