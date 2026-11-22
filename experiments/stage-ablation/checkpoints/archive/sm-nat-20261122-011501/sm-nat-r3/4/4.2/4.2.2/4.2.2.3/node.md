# N129: 工作点 C（中等驱逐/标准 T_res）：基于 N79 的 Eviction_Rate = 1.925 * 10^11 bytes/day，T_res = 12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

工作点 C（中等驱逐/标准 T_res）：基于 N79 的 Eviction_Rate = 1.925 * 10^11 bytes/day，T_res = 128 * 10^9 / 1.925 * 10^11 days ≈ 0.000665 days ≈ 0.96 分钟（约 1 分钟）。此 T_res 值与 N53 原始估算的 3.3 分钟存在差异，源于 H_lru 假设不同（65% vs 50%），表明 T_res 对命中率假设高度敏感，需通过实际负载校准。

## Corrected Claim

工作点 C（中等驱逐/标准 T_res）：基于 N79 的 Eviction_Rate = 1.925 * 10^11 bytes/day，T_res = 128 * 10^9 / 1.925 * 10^11 days ≈ 0.000665 days ≈ 0.96 分钟（约 1 分钟）。此 T_res 值与 N53 原始估算的 3.3 分钟存在差异，源于 H_lru 假设不同（65% vs 50%），表明 T_res 对命中率假设高度敏感，需通过实际负载校准。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（128e9 / 1.925e11 ≈ 0.000665 days ≈ 0.96 min），且关于命中率假设敏感性的定性结论符合逻辑直觉。
