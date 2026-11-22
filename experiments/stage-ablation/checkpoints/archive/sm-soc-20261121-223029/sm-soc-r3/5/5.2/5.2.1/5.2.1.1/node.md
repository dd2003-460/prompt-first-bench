# N299: 随机偏好噪声假设下 r 的理论推导：r_theoretical = -sqrt(Var(W) / (Var(W) + Var(ε_noise)))，其中 Var

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

随机偏好噪声假设下 r 的理论推导：r_theoretical = -sqrt(Var(W) / (Var(W) + Var(ε_noise)))，其中 Var(W) 为买家支付意愿方差，Var(ε_noise) 为随机噪声方差；若噪声主导（Var(ε) >> Var(W)），则 r 趋近于 0；若偏好主导，则 r 趋近于 -1。

## Corrected Claim

随机偏好噪声假设下 r 的理论推导：r_theoretical = -sqrt(Var(W) / (Var(W) + Var(ε_noise)))，其中 Var(W) 为买家支付意愿方差，Var(ε_noise) 为随机噪声方差；若噪声主导（Var(ε) >> Var(W)），则 r 趋近于 0；若偏好主导，则 r 趋近于 -1。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合信号检测理论中相关系数的定义（信号方差与总方差之比的负根），极限行为（噪声主导趋近0，偏好主导趋近-1）在数学上自洽且符合直觉。
