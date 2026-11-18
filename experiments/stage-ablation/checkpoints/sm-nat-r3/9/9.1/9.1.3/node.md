# N178: 实际 LFU 与理想上限的差距来源：LFU 的计数器衰减机制导致冷门大对象占据容量，实际 K_lfu_actual < K_lfu_max，差距取决于 LFU 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

实际 LFU 与理想上限的差距来源：LFU 的计数器衰减机制导致冷门大对象占据容量，实际 K_lfu_actual < K_lfu_max，差距取决于 LFU 参数（如衰减因子 δ）和访问分布的长尾效应。

## Corrected Claim

实际 LFU 与理想上限的差距来源：LFU 的计数器衰减机制导致冷门大对象占据容量，实际 K_lfu_actual < K_lfu_max，差距取决于 LFU 参数（如衰减因子 δ）和访问分布的长尾效应。

## Evidence

先验知识/题面给定，逻辑校验通过
