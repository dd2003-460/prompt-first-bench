# N129: 三线及以下城市公有云CDN回源延迟P99（150-250ms）的加权贡献验证：公式为 (1 - HitRate) * RTT_Origin。HitRate=90

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

三线及以下城市公有云CDN回源延迟P99（150-250ms）的加权贡献验证：公式为 (1 - HitRate) * RTT_Origin。HitRate=90%，RTT_Origin（三线到源站）≈150-250ms，加权贡献 = 0.10 * 200ms ≈ 20ms，与声称的15-25ms区间吻合，需确认源站是否对三线用户进行地理优化或存在多级回源

## Corrected Claim

三线及以下城市公有云CDN回源延迟P99（150-250ms）的加权贡献验证：公式为 (1 - HitRate) * RTT_Origin。HitRate=90%，RTT_Origin（三线到源站）≈150-250ms，加权贡献 = 0.10 * 200ms ≈ 20ms，与声称的15-25ms区间吻合，需确认源站是否对三线用户进行地理优化或存在多级回源

## Evidence

先验知识/题面给定，逻辑校验通过：公式 (1-0.9)*200ms=20ms 计算正确，且 20ms 落在 15-25ms 区间内，量级与逻辑自洽。
