# N38: LFU 与 LRU 驻留集差异的量化定义：ΔC = |C_LFU \ C_LRU|。在 β=0.9 下，LFU 更倾向于保留高频但非最新访问的对象。需计算两个集

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

LFU 与 LRU 驻留集差异的量化定义：ΔC = |C_LFU \ C_LRU|。在 β=0.9 下，LFU 更倾向于保留高频但非最新访问的对象。需计算两个集合的对称差集大小，以及该差异对应的字节命中率增益 ΔH = (Σ_{i∈C_LFU} r_i s_i - Σ_{i∈C_LRU} r_i s_i) / Total。

## Corrected Claim

LFU 与 LRU 驻留集差异的量化定义：ΔC = |C_LFU \ C_LRU|。在 β=0.9 下，LFU 更倾向于保留高频但非最新访问的对象。需计算两个集合的对称差集大小，以及该差异对应的字节命中率增益 ΔH = (Σ_{i∈C_LFU} r_i s_i - Σ_{i∈C_LRU} r_i s_i) / Total。

## Evidence

先验知识/题面给定，逻辑校验通过
