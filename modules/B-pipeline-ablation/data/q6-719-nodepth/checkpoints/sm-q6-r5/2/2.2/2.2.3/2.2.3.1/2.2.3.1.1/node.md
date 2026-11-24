# N530: N173 工作点下，新鲜度敏感内容（f_realtime=5%）的 TTL=1h 策略导致的缓存失效频率 F_invalidation = R_realtime

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N173

## Claim

N173 工作点下，新鲜度敏感内容（f_realtime=5%）的 TTL=1h 策略导致的缓存失效频率 F_invalidation = R_realtime_daily / TTL，其中 R_realtime_daily = 5% * 2TB / s_avg，需量化此频率对源站 QPS 的冲击及是否超过源站承载上限。

## Corrected Claim

N173 工作点下，新鲜度敏感内容（f_realtime=5%）的 TTL=1h 策略导致的缓存失效频率 F_invalidation = R_realtime_daily / TTL，其中 R_realtime_daily = 5% * 2TB / s_avg，需量化此频率对源站 QPS 的冲击及是否超过源站承载上限。

## Evidence

先验知识/题面给定，逻辑校验通过
