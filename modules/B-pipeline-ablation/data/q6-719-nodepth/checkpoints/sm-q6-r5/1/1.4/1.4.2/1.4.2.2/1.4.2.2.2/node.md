# N472: 回源带宽冗余配置公式：B_redundant = B_base * (1/U_target - 1)，其中 U_target = 0.6 为安全利用率阈值，若 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N151

## Claim

回源带宽冗余配置公式：B_redundant = B_base * (1/U_target - 1)，其中 U_target = 0.6 为安全利用率阈值，若 B_base = 10Gbps，则 B_redundant = 10 * (1/0.6 - 1) ≈ 6.67Gbps，总带宽需求 B_total = 16.67Gbps，额外成本 ΔC_bw = 6.67 * P_bw ≈ ¥3335/月（按 ¥500/Gbps/月计）。

## Corrected Claim

回源带宽冗余配置公式：B_redundant = B_base * (1/U_target - 1)，其中 U_target = 0.6 为安全利用率阈值，若 B_base = 10Gbps，则 B_redundant = 10 * (1/0.6 - 1) ≈ 6.67Gbps，总带宽需求 B_total = 16.67Gbps，额外成本 ΔC_bw = 6.67 * P_bw ≈ ¥3335/月（按 ¥500/Gbps/月计）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确（10*(1/0.6-1)=6.67），成本计算正确（6.67*500=3335），量纲与数值量级合理。
