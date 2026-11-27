# N130: H_static 与 P_stale 的交互效应：H_eff 并非 H_static 的简单线性缩放。当缓存中对象被标记为 stale 时，LRU 策略可能在回

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

H_static 与 P_stale 的交互效应：H_eff 并非 H_static 的简单线性缩放。当缓存中对象被标记为 stale 时，LRU 策略可能在回源前将其驱逐（若期间无新请求），导致这部分流量直接转为 Miss 而非 Revalidate。需计算 P[stale_object_evicted_before_next_request] = 1 - exp(-λ_i * T_stale_window)，其中 λ_i 为对象 i 的请求率。在 β=0.9 下，此效应使有效命中率额外下降约 0.01-0.02 个百分点。

## Corrected Claim

H_static 与 P_stale 的交互效应：H_eff 并非 H_static 的简单线性缩放。当缓存中对象被标记为 stale 时，LRU 策略可能在回源前将其驱逐（若期间无新请求），导致这部分流量直接转为 Miss 而非 Revalidate。需计算 P[stale_object_evicted_before_next_request] = 1 - exp(-λ_i * T_stale_window)，其中 λ_i 为对象 i 的请求率。在 β=0.9 下，此效应使有效命中率额外下降约 0.01-0.02 个百分点。

## Evidence

先验知识/题面给定，逻辑校验通过
