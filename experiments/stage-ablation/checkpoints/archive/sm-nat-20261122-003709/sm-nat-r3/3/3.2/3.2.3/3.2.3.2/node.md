# N164: 计算非独立更新下的失效概率偏差 \Delta M：若 \rho_{u,h} > 0（热门对象更新更快），则热门对象驻留时间 T_res,hot 缩短，导致 M_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

计算非独立更新下的失效概率偏差 \Delta M：若 \rho_{u,h} > 0（热门对象更新更快），则热门对象驻留时间 T_res,hot 缩短，导致 M_invalidation 被低估，偏差量 \Delta M \approx \rho_{u,h} \cdot \lambda_{base} \cdot T_{res,hot} \cdot \frac{\partial p_{hot}}{\partial T}，需通过蒙特卡洛模拟验证符号与量级。

## Corrected Claim

计算非独立更新下的失效概率偏差 \Delta M：若 \rho_{u,h} > 0（热门对象更新更快），则热门对象驻留时间 T_res,hot 缩短，导致 M_invalidation 被低估，偏差量 \Delta M \approx \rho_{u,h} \cdot \lambda_{base} \cdot T_{res,hot} \cdot \frac{\partial p_{hot}}{\partial T}，需通过蒙特卡洛模拟验证符号与量级。

## Evidence

先验知识/题面给定，逻辑校验通过
