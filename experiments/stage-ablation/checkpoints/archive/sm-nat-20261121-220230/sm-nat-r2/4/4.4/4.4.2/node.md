# N72: 失效概率 P_invalid 的精确计算：P_invalid = 1 - exp(-0.01 * T_resident)，当 T_resident 从 0.1 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

失效概率 P_invalid 的精确计算：P_invalid = 1 - exp(-0.01 * T_resident)，当 T_resident 从 0.1 天变化到 10 天时，P_invalid 从 0.1% 变化到 9.05%，需给出 T_resident 的合理估计值以确定折损系数。

## Corrected Claim

失效概率 P_invalid 的精确计算：P_invalid = 1 - exp(-0.01 * T_resident)，当 T_resident 从 0.1 天变化到 10 天时，P_invalid 从 0.1% 变化到 9.05%，需给出 T_resident 的合理估计值以确定折损系数。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P=1-exp(-0.01*T) 在 T=0.1 时约为 0.001 (0.1%)，在 T=10 时约为 0.0905 (9.05%)，数值计算准确且逻辑自洽。
