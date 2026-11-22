# N217: 直接效用项投影 Direct_U 的期望值 E[Direct_U]：E[(V_true - P_ask*)·q] = (μ_V - P_ask*)·E[q]，在

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N64

## Claim

直接效用项投影 Direct_U 的期望值 E[Direct_U]：E[(V_true - P_ask*)·q] = (μ_V - P_ask*)·E[q]，在 P_ask* = 1.2μ_V 且 E[q]=0.4 时，E[Direct_U] = -0.2μ_V·0.4 = -0.08μ_V。

## Corrected Claim

直接效用项投影 Direct_U 的期望值 E[Direct_U]：E[(V_true - P_ask*)·q] = (μ_V - P_ask*)·E[q]，在 P_ask* = 1.2μ_V 且 E[q]=0.4 时，E[Direct_U] = -0.2μ_V·0.4 = -0.08μ_V。

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导 E[(V-P)q] = (μ_V-P)E[q] 成立，代入 P=1.2μ_V 和 E[q]=0.4 计算得 -0.2μ_V * 0.4 = -0.08μ_V，数值与逻辑均自洽。
