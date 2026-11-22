# N92: 当更新率 U_rate=0.01/day 且 T_residence > 100 天时，线性近似公式 f_update = 1 - U_rate * T_res

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

当更新率 U_rate=0.01/day 且 T_residence > 100 天时，线性近似公式 f_update = 1 - U_rate * T_residence 失效，需采用指数衰减模型 f_update = exp(-U_rate * T_residence) 或精确的稳态陈旧占比模型 C_steady = 1 - exp(-U_rate * T_residence) 来计算有效命中率折损。

## Corrected Claim

当更新率 U_rate=0.01/day 且 T_residence > 100 天时，线性近似公式 f_update = 1 - U_rate * T_residence 失效，需采用指数衰减模型 f_update = exp(-U_rate * T_residence) 或精确的稳态陈旧占比模型 C_steady = 1 - exp(-U_rate * T_residence) 来计算有效命中率折损。

## Evidence

先验知识/题面给定，逻辑校验通过：当 U_rate*T_residence = 1 时，线性近似误差达 63%，确实失效；指数模型符合泊松过程/指数衰减的物理直觉。
