# N425: 工作点1（高核心占比/低混合成本）：P_core=0.8 时，混合策略总成本 C_total_mix = 0.8*C_self + 0.2*C_public，P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

工作点1（高核心占比/低混合成本）：P_core=0.8 时，混合策略总成本 C_total_mix = 0.8*C_self + 0.2*C_public，P99_mix ≈ 0.8*100ms + 0.2*150ms = 110ms，满足 T=150ms 且成本低于全公有云 15%。

## Corrected Claim

工作点1（高核心占比/低混合成本）：P_core=0.8 时，混合策略总成本 C_total_mix = 0.8*C_self + 0.2*C_public，P99_mix ≈ 0.8*100ms + 0.2*150ms = 110ms，满足 T=150ms 且成本低于全公有云 15%。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均延迟计算正确（0.8*100+0.2*150=110ms < 150ms），成本降低15%符合线性加权逻辑（假设C_self显著低于C_public），无内部矛盾。
