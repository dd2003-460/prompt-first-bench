# N168: 整体 T_network P99 加权计算：Σ(w_i × T_i) = 7.5 + 27.0 + 34.5 = 69.0ms，考虑网络抖动和路由非最优因素，实

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N63

## Claim

整体 T_network P99 加权计算：Σ(w_i × T_i) = 7.5 + 27.0 + 34.5 = 69.0ms，考虑网络抖动和路由非最优因素，实际 P99 约为 70-85ms

## Corrected Claim

整体 T_network P99 加权计算：Σ(w_i × T_i) = 7.5 + 27.0 + 34.5 = 69.0ms，考虑网络抖动和路由非最优因素，实际 P99 约为 70-85ms

## Evidence

先验知识/题面给定，逻辑校验通过：加权求和 7.5+27.0+34.5=69.0 计算正确，且 70-85ms 的区间合理覆盖了 69ms 基准值加上网络抖动和非最优路由带来的额外延迟。
