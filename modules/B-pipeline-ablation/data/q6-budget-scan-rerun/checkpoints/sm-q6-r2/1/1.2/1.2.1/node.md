# N41: 公有云 CDN P99=150ms 的构成拆解：T_pub = T_last_mile (最后一公里接入) + T_edge_processing (边缘节点处

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

公有云 CDN P99=150ms 的构成拆解：T_pub = T_last_mile (最后一公里接入) + T_edge_processing (边缘节点处理) + T_origin_fallback (回源概率加权延迟)，其中 T_last_mile 典型值 50-80ms (4G/5G/Wi-Fi 混合)，T_edge_processing 典型值 10-20ms (缓存命中时)，T_origin_fallback = (1-CHR) * T_origin，T_origin 典型值 100-200ms

## Corrected Claim

公有云 CDN P99=150ms 的构成拆解：T_pub = T_last_mile (最后一公里接入) + T_edge_processing (边缘节点处理) + T_origin_fallback (回源概率加权延迟)，其中 T_last_mile 典型值 50-80ms (4G/5G/Wi-Fi 混合)，T_edge_processing 典型值 10-20ms (缓存命中时)，T_origin_fallback = (1-CHR) * T_origin，T_origin 典型值 100-200ms

## Evidence

先验知识/题面给定，逻辑校验通过：各分项延迟量级（最后一公里50-80ms、边缘处理10-20ms、回源100-200ms）符合公有云CDN典型工程经验，且加权求和逻辑自洽，无来源矛盾。

## Search Query

Cloudflare Alibaba CDN P99 latency breakdown last mile edge processing origin fallback
