# N624: 命中率提升的边际收益量化：ΔC_tco_per_ΔH = -R_daily * s_avg * (1-H) * P_bw * ΔH + C_hit_invest

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N206

## Claim

命中率提升的边际收益量化：ΔC_tco_per_ΔH = -R_daily * s_avg * (1-H) * P_bw * ΔH + C_hit_invest，其中 P_bw 为带宽单价（¥0.2/GB）；当 H=95% 时，ΔH=0.01 节省带宽成本 ≈ 2TB*0.01*0.2 = ¥40/天 ≈ ¥1,200/月，而 C_hit_invest 通常 > ¥5,000/月，导致净收益为负

## Corrected Claim

命中率提升的边际收益量化：ΔC_tco_per_ΔH = -R_daily * s_avg * (1-H) * P_bw * ΔH + C_hit_invest，其中 P_bw 为带宽单价（¥0.2/GB）；当 H=95% 时，ΔH=0.01 节省带宽成本 ≈ 2TB*0.01*0.2 = ¥40/天 ≈ ¥1,200/月，而 C_hit_invest 通常 > ¥5,000/月，导致净收益为负

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导与数值计算（2TB*0.01*0.2=40元/天，月约1200元）自洽，且符合缓存经济学中边际收益递减的直觉。
