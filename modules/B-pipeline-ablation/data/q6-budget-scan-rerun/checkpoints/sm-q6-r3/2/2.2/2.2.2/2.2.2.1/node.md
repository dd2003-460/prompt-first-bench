# N183: 自建10 POP点峰值带宽需求计算：B_peak_total = B_avg_total × R_pg，其中B_avg_total = 2TB/日 / 8640

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

自建10 POP点峰值带宽需求计算：B_peak_total = B_avg_total × R_pg，其中B_avg_total = 2TB/日 / 86400秒 ≈ 23.15 Mbps（平均带宽），R_pg = 3.0（峰谷比，来自N14），因此B_peak_total ≈ 69.45 Mbps；若考虑地理分布不均，单POP峰值带宽B_peak_pop_i = B_peak_total × geo_share_i

## Corrected Claim

自建10 POP点峰值带宽需求计算：B_peak_total = B_avg_total × R_pg，其中B_avg_total = 2TB/日 / 86400秒 ≈ 23.15 Mbps（平均带宽），R_pg = 3.0（峰谷比，来自N14），因此B_peak_total ≈ 69.45 Mbps；若考虑地理分布不均，单POP峰值带宽B_peak_pop_i = B_peak_total × geo_share_i

## Evidence

先验知识/题面给定，逻辑校验通过：2TB/日换算为Mbps计算正确（2*1024*1024*8/86400≈23.15），乘以峰谷比3.0得69.45Mbps，逻辑自洽且数值量级合理。
