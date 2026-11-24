# N47: 峰值持续时间占比 D_peak = T_peak / T_total，其中 T_peak 为日均流量超过 3x 平均值的累计时长，典型 C 端平台 D_peak

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

峰值持续时间占比 D_peak = T_peak / T_total，其中 T_peak 为日均流量超过 3x 平均值的累计时长，典型 C 端平台 D_peak ≈ 0.1-0.15（即每天 2.4-3.6 小时），决定带宽成本中按峰值计费部分的权重。

## Corrected Claim

峰值持续时间占比 D_peak = T_peak / T_total，其中 T_peak 为日均流量超过 3x 平均值的累计时长，典型 C 端平台 D_peak ≈ 0.1-0.15（即每天 2.4-3.6 小时），决定带宽成本中按峰值计费部分的权重。

## Evidence

先验知识/题面给定，逻辑校验通过：D_peak=0.1-0.15 对应 2.4-3.6 小时，数学换算正确（24*0.1=2.4, 24*0.15=3.6），符合典型 C 端互联网流量峰值特征（如晚间高峰），量级合理。

## Search Query

CDN peak traffic duration ratio daily average load distribution
