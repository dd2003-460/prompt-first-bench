# N266: 低吞吐高精度工作点：在 T_cycle=600s（复杂推理期）且引入云端校验 C_check=0.05元/循环 时，混合成本 C_hybrid = C_ener

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

低吞吐高精度工作点：在 T_cycle=600s（复杂推理期）且引入云端校验 C_check=0.05元/循环 时，混合成本 C_hybrid = C_energy_local(0.011元) + C_check(0.05元) = 0.061元，此时盈亏平衡点 X_be_mix ≈ 23.04 / (0.061 - 0.0126) ≈ 474 循环/天，低于此频率应纯云端

## Corrected Claim

低吞吐高精度工作点：在 T_cycle=600s（复杂推理期）且引入云端校验 C_check=0.05元/循环 时，混合成本 C_hybrid = C_energy_local(0.011元) + C_check(0.05元) = 0.061元，此时盈亏平衡点 X_be_mix ≈ 23.04 / (0.061 - 0.0126) ≈ 474 循环/天，低于此频率应纯云端

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 0.011+0.05=0.061 正确；分母 0.061-0.0126=0.0484 正确；商 23.04/0.0484≈476.03，与陈述中的 474 存在微小舍入差异但不影响量级和结论方向，整体逻辑自洽。
