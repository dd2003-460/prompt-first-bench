# N652: 混合策略的期望成本修正：E[C_rto] 不仅取决于 P(full)，还取决于增量恢复的额外复杂度成本 C_inc_overhead（如元数据同步、差异计算）；

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N225

## Claim

混合策略的期望成本修正：E[C_rto] 不仅取决于 P(full)，还取决于增量恢复的额外复杂度成本 C_inc_overhead（如元数据同步、差异计算）；E[C_rto] = P(full)*C_full + P(inc)*(C_inc_base + C_inc_overhead)；若 C_inc_overhead 显著高于 0，即使 P(full) 较小，混合策略也可能不如纯全量策略简单可靠。

## Corrected Claim

混合策略的期望成本修正：E[C_rto] 不仅取决于 P(full)，还取决于增量恢复的额外复杂度成本 C_inc_overhead（如元数据同步、差异计算）；E[C_rto] = P(full)*C_full + P(inc)*(C_inc_base + C_inc_overhead)；若 C_inc_overhead 显著高于 0，即使 P(full) 较小，混合策略也可能不如纯全量策略简单可靠。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

incremental restore overhead metadata sync cost comparison full restore
