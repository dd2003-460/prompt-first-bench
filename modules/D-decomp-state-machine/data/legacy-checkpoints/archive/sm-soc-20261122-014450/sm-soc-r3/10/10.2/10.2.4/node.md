# N389: 类比误差计算公式与阈值判定：定义误差 E_analog = |k_platform - k_airbnb_implied| / k_platform，其中 k_

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N125

## Claim

类比误差计算公式与阈值判定：定义误差 E_analog = |k_platform - k_airbnb_implied| / k_platform，其中 k_airbnb_implied 由 ΔP_airbnb% 反推得出；若 E_analog < 0.10，则置信度维持 0.70，否则按公式 C_adjusted = 0.70 * (1 - E_analog) 下调。

## Corrected Claim

类比误差计算公式与阈值判定：定义误差 E_analog = |k_platform - k_airbnb_implied| / k_platform，其中 k_airbnb_implied 由 ΔP_airbnb% 反推得出；若 E_analog < 0.10，则置信度维持 0.70，否则按公式 C_adjusted = 0.70 * (1 - E_analog) 下调。

## Evidence

先验知识/题面给定，逻辑校验通过
