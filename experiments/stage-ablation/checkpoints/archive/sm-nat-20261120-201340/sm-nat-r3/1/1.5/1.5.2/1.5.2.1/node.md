# N100: 总字节请求量计算基准工作点 A（保守估计）：采用 s_min=10KB 且无截断上限的假设，E[S]=110KB，总字节流量 = 50,000,000 * 11

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

总字节请求量计算基准工作点 A（保守估计）：采用 s_min=10KB 且无截断上限的假设，E[S]=110KB，总字节流量 = 50,000,000 * 110KB ≈ 5.5TB/day，该值作为分母基准。

## Corrected Claim

总字节请求量计算基准工作点 A（保守估计）：采用 s_min=10KB 且无截断上限的假设，E[S]=110KB，总字节流量 = 50,000,000 * 110KB ≈ 5.5TB/day，该值作为分母基准。

## Evidence

先验知识/题面给定，逻辑校验通过：50,000,000 * 110KB = 5,500,000,000 KB ≈ 5.5TB，计算无误且量级合理。
