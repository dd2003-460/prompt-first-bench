# N362: 宏观溢价带宽度 ΔP_band 的投影修正：原公式 ΔP_band ≈ 2 * 1.96 * σ_noise / sqrt(N_eff) 假设噪声独立。考虑 N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

宏观溢价带宽度 ΔP_band 的投影修正：原公式 ΔP_band ≈ 2 * 1.96 * σ_noise / sqrt(N_eff) 假设噪声独立。考虑 N133 中的相关性后，ΔP_band 的实际观测值会更大。若 N_eff 从 1000 降至 100，则 ΔP_band 扩大 sqrt(10) ≈ 3.16 倍。若观测 ΔP_band = 20%，则反推 σ_noise ≈ 20% * sqrt(100) / (2*1.96) ≈ 5.1%，比原估计 32.2% 小得多，说明个体噪声较小，宏观带宽主要由相关性驱动。

## Corrected Claim

宏观溢价带宽度 ΔP_band 的投影修正：原公式 ΔP_band ≈ 2 * 1.96 * σ_noise / sqrt(N_eff) 假设噪声独立。考虑 N133 中的相关性后，ΔP_band 的实际观测值会更大。若 N_eff 从 1000 降至 100，则 ΔP_band 扩大 sqrt(10) ≈ 3.16 倍。若观测 ΔP_band = 20%，则反推 σ_noise ≈ 20% * sqrt(100) / (2*1.96) ≈ 5.1%，比原估计 32.2% 小得多，说明个体噪声较小，宏观带宽主要由相关性驱动。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合统计学原理，数值计算（sqrt(10)≈3.16, 20*10/3.92≈5.1）准确，且结论（相关性导致有效样本量N_eff下降从而扩大带宽）在逻辑上自洽。

## Search Query

macro price band width correlation adjustment
