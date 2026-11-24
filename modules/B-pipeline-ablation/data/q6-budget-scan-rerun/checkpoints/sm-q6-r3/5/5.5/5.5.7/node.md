# N156: 混合策略的P99延迟基线为 L_p99_hybrid = 150ms，由 w_core * L_self(100ms) + w_tail * L_cloud(2

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

混合策略的P99延迟基线为 L_p99_hybrid = 150ms，由 w_core * L_self(100ms) + w_tail * L_cloud(200ms) = 0.6*100 + 0.4*200 = 140ms，加上10ms路由开销，总计150ms。

## Corrected Claim

混合策略的P99延迟基线为 L_p99_hybrid = 150ms，由 w_core * L_self(100ms) + w_tail * L_cloud(200ms) = 0.6*100 + 0.4*200 = 140ms，加上10ms路由开销，总计150ms。

## Evidence

先验知识/题面给定，逻辑校验通过：0.6*100 + 0.4*200 = 140ms，加上10ms路由开销等于150ms，计算无误且逻辑自洽。
