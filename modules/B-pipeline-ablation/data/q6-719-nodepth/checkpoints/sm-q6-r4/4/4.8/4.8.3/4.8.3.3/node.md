# N427: 工作点3（低核心占比/高混合风险）：P_core=0.4 时，C_total_mix = 0.4*C_self + 0.6*C_public，P99_mix ≈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

工作点3（低核心占比/高混合风险）：P_core=0.4 时，C_total_mix = 0.4*C_self + 0.6*C_public，P99_mix ≈ 0.4*100ms + 0.6*150ms = 130ms，接近 T=150ms 边界，且自建固定成本摊销 C_fixed_per_req 上升，总成本可能高于全公有云。

## Corrected Claim

工作点3（低核心占比/高混合风险）：P_core=0.4 时，C_total_mix = 0.4*C_self + 0.6*C_public，P99_mix ≈ 0.4*100ms + 0.6*150ms = 130ms，接近 T=150ms 边界，且自建固定成本摊销 C_fixed_per_req 上升，总成本可能高于全公有云。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.4*100 + 0.6*150 = 130ms 正确，且 130ms 接近 150ms 边界的定性描述符合逻辑；成本上升归因于固定成本摊销符合经济学直觉。
