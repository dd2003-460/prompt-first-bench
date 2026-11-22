# N209: 工作点2（中驻留/平衡点）：设定 T_resident = 3.0 天，基于 N71 公式代入 P_eviction≈0.45，计算得 P_invalid = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

工作点2（中驻留/平衡点）：设定 T_resident = 3.0 天，基于 N71 公式代入 P_eviction≈0.45，计算得 P_invalid = 1 - exp(-0.03) ≈ 2.956%，折损因子 D ≈ 0.97044

## Corrected Claim

工作点2（中驻留/平衡点）：设定 T_resident = 3.0 天，基于 N71 公式代入 P_eviction≈0.45，计算得 P_invalid = 1 - exp(-0.03) ≈ 2.956%，折损因子 D ≈ 0.97044

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - exp(-0.03) ≈ 0.029556，即 2.956%；折损因子 D = 1 - 0.029556 ≈ 0.97044，数值与逻辑均自洽。
