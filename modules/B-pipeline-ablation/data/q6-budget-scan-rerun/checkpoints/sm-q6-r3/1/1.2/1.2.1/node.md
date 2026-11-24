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

父节点级核验通过：正交+完备+无冗余（子节点严格对应父节点公式中的三个独立分量（T_last_mile, T_edge_processing, T_origin_fallback），彼此无重叠且逻辑独立；三者相加覆盖了父节点定义的全部构成要素，无遗漏；每个子节点代表不同的物理/逻辑阶段，并非同一参数的不同取值，因此不存在冗余。）

## Search Query

Cloudflare Alibaba CDN P99 latency breakdown last mile edge processing origin fallback
