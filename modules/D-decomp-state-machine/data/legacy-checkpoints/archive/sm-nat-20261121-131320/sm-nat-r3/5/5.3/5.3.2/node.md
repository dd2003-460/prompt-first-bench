# N120: LRU 理论上能覆盖的字节命中率上界 H_LRU_max_byte = R_byte(S_evict)，其中 S_evict 是缓存满时驱逐的最小热度对象的大小

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

LRU 理论上能覆盖的字节命中率上界 H_LRU_max_byte = R_byte(S_evict)，其中 S_evict 是缓存满时驱逐的最小热度对象的大小阈值；若 S_evict=100KB，则 H_LRU_max_byte ≈ 55.3%；该值未考虑热度分布 β=0.9 的影响，需乘以热度修正因子 K_β 以得到实际命中率。

## Corrected Claim

LRU 理论上能覆盖的字节命中率上界 H_LRU_max_byte 取决于驱逐阈值 S_evict 及访问流模型；在特定假设下（如 S_evict=100KB），该值约为 55.3%，且需乘以热度修正因子 K_β 以反映 β=0.9 的影响。

## Evidence

[质询]数值 55.3% 缺乏通用理论推导支持，LRU 的字节命中率上界高度依赖于具体的访问流模型（如 Zipf 分布参数、对象大小分布等），仅凭 S_evict=100KB 无法唯一确定该数值，存在将特定场景经验值误作通用理论上限的风险。 | 先验知识/题面给定，逻辑校验通过（公式定义自洽，量纲合理），但具体数值 55.3% 为经验性参数，缺乏通用第一性原理推导或来源支持，故降级。
