# N145: LFU 理论增益项 Δ_H 在容量非绑定约束下的数值：由于 LRU 已能缓存全部对象（H_LRU≈1），LFU 无法通过‘避免缓存冷对象’获得额外字节命中增益，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N61

## Claim

LFU 理论增益项 Δ_H 在容量非绑定约束下的数值：由于 LRU 已能缓存全部对象（H_LRU≈1），LFU 无法通过‘避免缓存冷对象’获得额外字节命中增益，故 Δ_H_capacity = 0。LFU 的唯一潜在增益来自对‘更新后频率重置’的处理差异，但在稳态下该增益趋近于 0。

## Corrected Claim

LFU 理论增益项 Δ_H 在容量非绑定约束下的数值：由于 LRU 已能缓存全部对象（H_LRU≈1），LFU 无法通过‘避免缓存冷对象’获得额外字节命中增益，故 Δ_H_capacity = 0。LFU 的唯一潜在增益来自对‘更新后频率重置’的处理差异，但在稳态下该增益趋近于 0。

## Evidence

先验知识/题面给定，逻辑校验通过：在容量非绑定（Cache Size >= Working Set Size）条件下，LRU 命中率理论上为 100%，LFU 无法通过替换策略获得额外命中增益，故 Δ_H_capacity = 0 符合缓存理论第一性原理。
