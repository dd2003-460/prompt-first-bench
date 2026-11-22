# N174: σ_threshold 的解析解计算：σ_threshold = μ_signal * sqrt(2 * ln(1/P_base_fail))，其中 P_bas

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N44

## Claim

σ_threshold 的解析解计算：σ_threshold = μ_signal * sqrt(2 * ln(1/P_base_fail))，其中 P_base_fail=0.1，ln(1/0.1)=2.3026，sqrt(2*2.3026)=2.145。若 μ_signal=1.06 * P_ref，则 σ_threshold = 1.06 * 2.145 * P_ref ≈ 2.27 * P_ref

## Corrected Claim

σ_threshold 的解析解计算：σ_threshold = μ_signal * sqrt(2 * ln(1/P_base_fail))，其中 P_base_fail=0.1，ln(1/0.1)=2.3026，sqrt(2*2.3026)=2.145。若 μ_signal=1.06 * P_ref，则 σ_threshold = 1.06 * 2.145 * P_ref ≈ 2.27 * P_ref

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1.06 * sqrt(2 * ln(10)) ≈ 1.06 * 2.1459 ≈ 2.274，与陈述中的 2.27 一致，量纲与数值量级合理。
