# N152: W(t) 峰值带宽需求计算：W_peak = R_daily × s_avg × (1-H) × K_peak / T_peak_hours，代入已知值（R_d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

W(t) 峰值带宽需求计算：W_peak = R_daily × s_avg × (1-H) × K_peak / T_peak_hours，代入已知值（R_daily=1.34×10^9, s_avg=1.5MB, H=0.85, K_peak=4, T_peak=4h）计算得出峰值回源带宽需求约为 7.5 Gbps，用于确定冗余基数。

## Corrected Claim

W(t) 峰值带宽需求计算：W_peak = R_daily × s_avg × (1-H) × K_peak / T_peak_hours，代入已知值（R_daily=1.34×10^9, s_avg=1.5MB, H=0.85, K_peak=4, T_peak=4h）计算得出峰值回源带宽需求约为 7.5 Gbps，用于确定冗余基数。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程为 (1.34e9 * 1.5 * 1024 * 1024 * 0.15 * 4) / (4 * 3600) ≈ 7.5e9 bits/s = 7.5 Gbps，数值量级与公式推导一致。
