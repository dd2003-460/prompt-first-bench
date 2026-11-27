# N144: 差异对象的平均大小差 ΔS 的量化计算：ΔS = E[S_LFU] - E[S_LRU]。基于工作点 A（LFU 0.5MB）和工作点 C（LRU 1.5MB）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

差异对象的平均大小差 ΔS 的量化计算：ΔS = E[S_LFU] - E[S_LRU]。基于工作点 A（LFU 0.5MB）和工作点 C（LRU 1.5MB），ΔS = 0.5 - 1.5 = -1.0MB。负值表明 LFU 缓存的对象平均更小，从而在相同容量下可容纳更多对象。

## Corrected Claim

差异对象的平均大小差 ΔS 的量化计算：ΔS = E[S_LFU] - E[S_LRU]。基于工作点 A（LFU 0.5MB）和工作点 C（LRU 1.5MB），ΔS = 0.5 - 1.5 = -1.0MB。负值表明 LFU 缓存的对象平均更小，从而在相同容量下可容纳更多对象。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 0.5 - 1.5 = -1.0 正确，负值含义解释符合缓存原理（对象越小，同容量下数量越多）。
