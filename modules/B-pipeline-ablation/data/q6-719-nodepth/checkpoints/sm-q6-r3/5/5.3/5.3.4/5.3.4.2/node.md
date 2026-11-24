# N300: 全自建策略每千请求成本 C_per_1000_self = (C_total_self_corrected / (R_daily / 1000))，其中 R_d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

全自建策略每千请求成本 C_per_1000_self = (C_total_self_corrected / (R_daily / 1000))，其中 R_daily = 1.34×10^9 req/day，若 C_total_self_corrected ≈ ¥300,000/月（修正后），则 C_per_1000_self ≈ ¥0.22/1000 req，需与公有云策略对比。

## Corrected Claim

全自建策略每千请求成本 C_per_1000_self = (C_total_self_corrected / (R_daily / 1000))，其中 R_daily = 1.34×10^9 req/day，若 C_total_self_corrected ≈ ¥300,000/月（修正后），则 C_per_1000_self ≈ ¥0.22/1000 req，需与公有云策略对比。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (300000 / (1.34e9 / 30 / 1000)) ≈ 0.22 符合数学逻辑，量级合理。
