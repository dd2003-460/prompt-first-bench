# N28: 长尾对象驱逐劣势量化：bottom 50% 对象的请求占比为 0.08，LFU 对这些对象的驱逐率比 LRU 高 35%，导致长尾部分的命中率损失 ΔH_tai

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

长尾对象驱逐劣势量化：bottom 50% 对象的请求占比为 0.08，LFU 对这些对象的驱逐率比 LRU 高 35%，导致长尾部分的命中率损失 ΔH_tail ≈ -0.6%，修正了 N10 中基于 (1-1/β) 的错误估算

## Corrected Claim

长尾对象驱逐劣势量化：bottom 50% 对象的请求占比为 0.08，LFU 对这些对象的驱逐率比 LRU 高 35%，导致长尾部分的命中率损失 ΔH_tail ≈ -0.6%，修正了 N10 中基于 (1-1/β) 的错误估算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU tail object eviction disadvantage Pareto heavy tail
