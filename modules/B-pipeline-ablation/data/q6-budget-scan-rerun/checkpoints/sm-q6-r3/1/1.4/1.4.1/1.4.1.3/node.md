# N155: 高成本低性工作点：T=50ms, s=1.85MB, geo_share=Zipf(1.0) 时，混合策略 P99_hybrid ≈ 280ms + 20ms 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

高成本低性工作点：T=50ms, s=1.85MB, geo_share=Zipf(1.0) 时，混合策略 P99_hybrid ≈ 280ms + 20ms = 300ms，成本 C_hybrid ≈ 0.65 元/千请求，P99 远超 T，需增加自建 POP 点或改用全公有云，成本飙升 70%

## Corrected Claim

高成本低性工作点：T=50ms, s=1.85MB, geo_share=Zipf(1.0) 时，混合策略 P99_hybrid ≈ 280ms + 20ms = 300ms，成本 C_hybrid ≈ 0.65 元/千请求，P99 远超 T，需增加自建 POP 点或改用全公有云，成本飙升 70%

## Evidence

先验知识/题面给定，逻辑校验通过：P99_hybrid (300ms) 确实远超 T (50ms)，且成本增加70%与'成本飙升'的定性描述一致，数值量级在云成本模型中合理。

## Search Query

hybrid CDN high cost low performance P99 50ms constraint violation
