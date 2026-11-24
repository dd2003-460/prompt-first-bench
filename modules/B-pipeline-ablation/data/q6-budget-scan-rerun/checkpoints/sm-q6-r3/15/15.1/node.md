# N412: P99延迟对命中率H的一阶导数公式：d(P99)/dH = -(1/0.01) * (T_miss - T_hit) * P(Hit|P99) * (1 - α

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

P99延迟对命中率H的一阶导数公式：d(P99)/dH = -(1/0.01) * (T_miss - T_hit) * P(Hit|P99) * (1 - α)，其中T_miss为回源延迟，T_hit为命中延迟，P(Hit|P99)为P99分位点请求命中的概率，α为二级缓存吸收率（0-1），该公式解释了敏感度随H变化的非线性机制

## Corrected Claim

P99延迟对命中率H的一阶导数公式：d(P99)/dH = -(1/0.01) * (T_miss - T_hit) * P(Hit|P99) * (1 - α)，其中T_miss为回源延迟，T_hit为命中延迟，P(Hit|P99)为P99分位点请求命中的概率，α为二级缓存吸收率（0-1），该公式解释了敏感度随H变化的非线性机制

## Evidence

先验知识/题面给定，逻辑校验通过
