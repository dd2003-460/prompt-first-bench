# N311: 工作点 B（中缓存命中率/平衡成本）：R_origin = 15%，V_origin_daily = 2TB * 15% = 300GB，自建回源带宽成本 C_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

工作点 B（中缓存命中率/平衡成本）：R_origin = 15%，V_origin_daily = 2TB * 15% = 300GB，自建回源带宽成本 C_origin_bw_self = 300GB * ¥0.08/GB * 30 = ¥720/月，公有云回源成本 C_origin_bw_pub = 300GB * ¥0.3/GB * 30 = ¥2,700/月

## Corrected Claim

工作点 B（中缓存命中率/平衡成本）：R_origin = 15%，V_origin_daily = 2TB * 15% = 300GB，自建回源带宽成本 C_origin_bw_self = 300GB * ¥0.08/GB * 30 = ¥720/月，公有云回源成本 C_origin_bw_pub = 300GB * ¥0.3/GB * 30 = ¥2,700/月

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（300GB * 0.08 * 30 = 720; 300GB * 0.3 * 30 = 2700），量纲与成本逻辑自洽。
