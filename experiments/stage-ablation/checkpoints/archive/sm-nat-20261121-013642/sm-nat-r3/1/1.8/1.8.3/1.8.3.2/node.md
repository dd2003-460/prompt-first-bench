# N167: 工作点2（中命中率/中驻留）：当 H_byte_LRU=0.7 时，T_residence = 128 / (500 * (1-0.7)) ≈ 0.85 天。此

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

工作点2（中命中率/中驻留）：当 H_byte_LRU=0.7 时，T_residence = 128 / (500 * (1-0.7)) ≈ 0.85 天。此为基准工作点，需验证该驻留时间下线性近似 f_update = 1 - U_rate * T_residence 的有效性（U_rate * T_residence = 0.0085 < 0.1，满足线性条件）。

## Corrected Claim

工作点2（中命中率/中驻留）：当 H_byte_LRU=0.7 时，T_residence = 128 / (500 * (1-0.7)) ≈ 0.85 天。此为基准工作点，需验证该驻留时间下线性近似 f_update = 1 - U_rate * T_residence 的有效性（U_rate * T_residence = 0.0085 < 0.1，满足线性条件）。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 128/(500*0.3) ≈ 0.853 正确，线性近似条件 0.0085 < 0.1 成立，逻辑自洽。
