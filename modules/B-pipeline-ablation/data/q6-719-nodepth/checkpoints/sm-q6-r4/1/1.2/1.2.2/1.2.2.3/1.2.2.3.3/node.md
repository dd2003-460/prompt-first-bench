# N472: 公有云 Fallback 延迟分布 F_cloud(x) 的边界条件：当自建 POP 缓存未命中且回源失败时，延迟退化至 F_cloud_failover(x)

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N158

## Claim

公有云 Fallback 延迟分布 F_cloud(x) 的边界条件：当自建 POP 缓存未命中且回源失败时，延迟退化至 F_cloud_failover(x)，其 P99 通常比正常 F_cloud 高 50-100ms，需按故障概率 P_fail 加权计入整体 P99。

## Corrected Claim

公有云 Fallback 延迟分布 F_cloud(x) 的边界条件：当自建 POP 缓存未命中且回源失败时，延迟退化至 F_cloud_failover(x)，其 P99 通常比正常 F_cloud 高 50-100ms，需按故障概率 P_fail 加权计入整体 P99。

## Evidence

先验知识/题面给定，逻辑校验通过
