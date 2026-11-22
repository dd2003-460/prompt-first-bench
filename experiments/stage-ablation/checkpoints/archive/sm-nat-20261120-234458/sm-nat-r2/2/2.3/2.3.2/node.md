# N40: LRU 基线命中率 H_LRU 在容量足够（N5 已证 K>N）且无更新时的理论值为 1.0（100%），但在有限时间窗口 T 下，冷启动缺失率 P_miss_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LRU 基线命中率 H_LRU 在容量足够（N5 已证 K>N）且无更新时的理论值为 1.0（100%），但在有限时间窗口 T 下，冷启动缺失率 P_miss_cold = 1 - (1 - 1/N)^{Q*T}，其中 Q=5e7/天，N=1e5，T 为观察窗口。

## Corrected Claim

LRU 基线命中率 H_LRU 在容量足够（N5 已证 K>N）且无更新时的理论值为 1.0（100%），但在有限时间窗口 T 下，冷启动缺失率 P_miss_cold = 1 - (1 - 1/N)^{Q*T}，其中 Q=5e7/天，N=1e5，T 为观察窗口。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU在容量大于工作集且无更新时命中率为1；冷启动缺失率公式符合独立事件概率推导。

## Search Query

LRU cache hit rate cold start probability uniform access
