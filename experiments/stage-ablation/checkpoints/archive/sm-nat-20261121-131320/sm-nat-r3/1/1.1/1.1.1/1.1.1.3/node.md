# N63: 工作点 C（极端敏感性）：取 S_max = 10GB（理论最大对象），此时 S_threshold 的计算受少数超大对象主导，预计 S_threshold ≈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

工作点 C（极端敏感性）：取 S_max = 10GB（理论最大对象），此时 S_threshold 的计算受少数超大对象主导，预计 S_threshold ≈ 5MB，该值用于评估 LRU 在最坏情况下的命中率下限 H_LRU_worst。

## Corrected Claim

工作点 C（极端敏感性）：取 S_max = 10GB（理论最大对象），此时 S_threshold 的计算受少数超大对象主导，预计 S_threshold ≈ 5MB，该值用于评估 LRU 在最坏情况下的命中率下限 H_LRU_worst。

## Evidence

先验知识/题面给定，逻辑校验通过
