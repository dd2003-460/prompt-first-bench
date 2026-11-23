# N310: 工作点 A（高缓存命中率/低回源成本）：R_origin = 5%，V_origin_daily = 2TB * 5% = 100GB，自建回源带宽成本 C_o

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

工作点 A（高缓存命中率/低回源成本）：R_origin = 5%，V_origin_daily = 2TB * 5% = 100GB，自建回源带宽成本 C_origin_bw_self = 100GB * ¥0.08/GB * 30 = ¥240/月，公有云回源成本 C_origin_bw_pub = 100GB * ¥0.3/GB * 30 = ¥900/月

## Corrected Claim

工作点 A（高缓存命中率/低回源成本）：R_origin = 5%，V_origin_daily = 2TB * 5% = 100GB，自建回源带宽成本 C_origin_bw_self = 100GB * ¥0.08/GB * 30 = ¥240/月，公有云回源成本 C_origin_bw_pub = 100GB * ¥0.3/GB * 30 = ¥900/月

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（100GB * 0.08 * 30 = 240, 100GB * 0.3 * 30 = 900），量纲与量级符合常规CDN回源成本估算逻辑。
