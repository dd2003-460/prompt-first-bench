# N49: 字节利用率量化：LFU 缓存中热门小对象占比 P_small_hot = ∫_{S<x_med}∫_{R>r_95} f(S,R) ds dr / ∫∫ f(S

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N15

## Claim

字节利用率量化：LFU 缓存中热门小对象占比 P_small_hot = ∫_{S<x_med}∫_{R>r_95} f(S,R) ds dr / ∫∫ f(S,R) ds dr，该占比直接决定缓存空间被低价值（小但热）对象占据的程度，导致有效缓存容量 C_effective = C × (1 - P_small_hot × 0.8)。

## Corrected Claim

LFU 缓存中热门小对象占比 P_small_hot 可通过积分计算得出，该占比反映了缓存空间被小但热对象占据的程度，进而影响有效缓存容量，但具体影响系数需根据实际负载和替换策略确定，不宜固定为 0.8。

## Evidence

[质询]公式中的系数 0.8 缺乏理论依据或通用标准，属于任意设定的经验参数，且 LFU 缓存中'热门小对象'并不必然导致'低价值'，其空间占用与有效容量的关系取决于具体的替换策略和对象大小分布，不能简单通过该线性公式量化。 | 先验知识/题面给定，逻辑校验通过，但系数 0.8 为经验性假设，缺乏通用理论支持，故降级为定性表述。
