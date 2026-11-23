# N359: 混合策略 P99 延迟约束条件：P99(α) = max(P99_self(α), P99_cloud(1-α)) ≤ T，其中 P99_self 为自建部分 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

混合策略 P99 延迟约束条件：P99(α) = max(P99_self(α), P99_cloud(1-α)) ≤ T，其中 P99_self 为自建部分 P99 延迟，P99_cloud 为公有云部分 P99 延迟，T 为合规阈值（80ms-800ms）

## Corrected Claim

混合策略 P99 延迟约束条件：P99(α) = max(P99_self(α), P99_cloud(1-α)) ≤ T，其中 P99_self 为自建部分 P99 延迟，P99_cloud 为公有云部分 P99 延迟，T 为合规阈值（80ms-800ms）

## Evidence

先验知识/题面给定，逻辑校验通过
