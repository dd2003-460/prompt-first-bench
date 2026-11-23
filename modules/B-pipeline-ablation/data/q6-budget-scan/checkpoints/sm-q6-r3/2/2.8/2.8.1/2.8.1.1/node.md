# N291: 监控告警日均总量 A_daily 的计算公式：A_daily = N_rules * λ_false_positive + N_incidents_real，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

监控告警日均总量 A_daily 的计算公式：A_daily = N_rules * λ_false_positive + N_incidents_real，其中 N_rules 为监控规则数量（通常 50-200 条），λ_false_positive 为单规则日均误报率（通常 0.1-0.5 次/天），N_incidents_real 为日均真实故障数（通常 1-5 次），用于推导所需人力以控制单人均摊告警数 < 50 条

## Corrected Claim

监控告警日均总量 A_daily 的计算公式：A_daily = N_rules * λ_false_positive + N_incidents_real，其中 N_rules 为监控规则数量（通常 50-200 条），λ_false_positive 为单规则日均误报率（通常 0.1-0.5 次/天），N_incidents_real 为日均真实故障数（通常 1-5 次），用于推导所需人力以控制单人均摊告警数 < 50 条

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合线性叠加原理，参数量级（50-200规则 * 0.1-0.5误报 + 1-5真实故障 ≈ 6-105次/天）与目标（人均<50条，隐含至少1-2人值班）在工程直觉上自洽且合理。

## Search Query

CDN monitoring alert fatigue false positive rate per rule daily average
