# N204: s_avg 对带宽成本的影响：C_bw = Q_total * s_avg * P_bw，若 s_avg 增加 27%（2.4MB→3.05MB），带宽成本同比

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

s_avg 对带宽成本的影响：C_bw = Q_total * s_avg * P_bw，若 s_avg 增加 27%（2.4MB→3.05MB），带宽成本同比例增加 27%，对于日均 2TB 下载量，月带宽成本从 ¥13,200 增至 ¥16,764（阿里云价格）。

## Corrected Claim

s_avg 对带宽成本的影响：C_bw = Q_total * s_avg * P_bw，若 s_avg 增加 27%（2.4MB→3.05MB），带宽成本同比例增加 27%，对于日均 2TB 下载量，月带宽成本从 ¥13,200 增至 ¥16,764（阿里云价格）。

## Evidence

先验知识/题面给定，逻辑校验通过：数学关系 C_bw ∝ s_avg 成立，27% 增幅对应成本同比例增加，数值计算 (13200 * 1.27 ≈ 16764) 准确，量级合理。
