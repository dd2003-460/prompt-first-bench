# N96: 在缓存容量远大于总数据量（128GB >> 118.75MB）的极端情况下，LRU 的稳态字节命中率 H_byte_LRU 的理论下界为 1.0（100%），因

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在缓存容量远大于总数据量（128GB >> 118.75MB）的极端情况下，LRU 的稳态字节命中率 H_byte_LRU 的理论下界为 1.0（100%），因为所有 100,000 个对象均可同时驻留内存，任何请求都能命中，除非对象在请求前被更新失效。

## Corrected Claim

在缓存容量远大于总数据量（128GB >> 118.75MB）的极端情况下，LRU 的稳态字节命中率 H_byte_LRU 的理论下界为 1.0（100%），因为所有 100,000 个对象均可同时驻留内存，任何请求都能命中，除非对象在请求前被更新失效。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1定义了总体命中率公式及其与容量无关的特性（宏观视角），子节点2提供了该公式中关键项（失效概率）的具体微观计算模型（基于请求频率和更新率）。两者互补，无重复或矛盾，且共同完整覆盖了父节点中关于'理论下界'、'100%驻留'以及'更新失效例外'的核心逻辑。）

## Search Query

LRU cache hit rate theoretical lower bound full dataset resident
