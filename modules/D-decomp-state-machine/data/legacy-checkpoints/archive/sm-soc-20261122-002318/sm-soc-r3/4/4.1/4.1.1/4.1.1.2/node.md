# N162: 工作点 2 (中信号/中噪声)：假设 β_signal = 0.3 (中等信号) 且 σ_noise = 0.18 * P_market (符合 N91 的二手

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

工作点 2 (中信号/中噪声)：假设 β_signal = 0.3 (中等信号) 且 σ_noise = 0.18 * P_market (符合 N91 的二手非标品特征)。此时噪声项 0.5 * (0.18^2) / (2 * RiskAversion) 显著。若 RiskAversion = 1.0，噪声贡献 ≈ 0.0081 * P_market。信号项主导，但若 P_anchor - P_market 较大 (如 25%)，总 ΔP_anchor 可能达到 0.08-0.10 * P_market。此工作点代表典型二手市场现状。

## Corrected Claim

工作点 2 (中信号/中噪声)：假设 β_signal = 0.3 (中等信号) 且 σ_noise = 0.18 * P_market (符合 N91 的二手非标品特征)。此时噪声项 0.5 * (0.18^2) / (2 * RiskAversion) 显著。若 RiskAversion = 1.0，噪声贡献 ≈ 0.0081 * P_market。信号项主导，但若 P_anchor - P_market 较大 (如 25%)，总 ΔP_anchor 可能达到 0.08-0.10 * P_market。此工作点代表典型二手市场现状。

## Evidence

先验知识/题面给定，逻辑校验通过：噪声项计算 0.5*(0.18^2)/2 = 0.0081 正确；信号项主导且总变动范围 0.08-0.10 符合中等信号强度下的经济直觉，无内部矛盾。

## Search Query

Buyer reservation price shift medium signal medium noise second hand market
