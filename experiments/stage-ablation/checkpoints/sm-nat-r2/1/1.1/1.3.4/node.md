# N33: E[S] 的敏感性分析：若 x_min 取 100 Bytes (更小的最小对象)，则 E[S] = 1.1 KB，K_avg 将增加 10 倍至 ~1.2 万

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

E[S] 的敏感性分析：若 x_min 取 100 Bytes (更小的最小对象)，则 E[S] = 1.1 KB，K_avg 将增加 10 倍至 ~1.2 万，这会显著改变 LRU 的缓存覆盖范围，需确认 x_min 的量级对命中率下界的影响。

## Corrected Claim

E[S] 的敏感性分析：若 x_min 取 100 Bytes (更小的最小对象)，则 E[S] = 1.1 KB，K_avg 将增加 10 倍至 ~1.2 万，这会显著改变 LRU 的缓存覆盖范围，需确认 x_min 的量级对命中率下界的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：x_min 从 1KB 降至 100B (10倍)，对象数量 K 相应增加 10 倍，量级推导自洽。

## Search Query

Pareto alpha 1.1 mean size sensitivity minimum value
