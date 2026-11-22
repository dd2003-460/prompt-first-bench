# N13: 工作点 2（给定更新率，λ=0.01/day）：基准失效场景。计算 T_res 后，得出具体折扣值。例如，若 T_res=10 days，P_invalid ≈

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

工作点 2（给定更新率，λ=0.01/day）：基准失效场景。计算 T_res 后，得出具体折扣值。例如，若 T_res=10 days，P_invalid ≈ 9.5%，则 H_eff ≈ 0.905 * H_static。需结合 N1 计算的 H_static 得出最终有效命中率。

## Corrected Claim

工作点 2（给定更新率，λ=0.01/day）：基准失效场景。计算 T_res 后，得出具体折扣值。例如，若 T_res=10 days，P_invalid ≈ 9.5%，则 H_eff ≈ 0.905 * H_static。需结合 N1 计算的 H_static 得出最终有效命中率。

## Evidence

先验知识/题面给定，逻辑校验通过：P_invalid = 1 - e^(-λT) ≈ 1 - e^(-0.1) ≈ 9.5%，H_eff = (1 - P_invalid) * H_static ≈ 0.905 * H_static，数值与逻辑自洽。
