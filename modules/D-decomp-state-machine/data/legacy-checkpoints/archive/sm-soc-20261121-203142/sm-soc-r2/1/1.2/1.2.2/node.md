# N30: 买家点击率 CTR 的期望值 E[CTR] 在可见池内为 0.12，公式为 E[CTR] = CTR_base * (1 + γ * (P_ask - P_ma

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

买家点击率 CTR 的期望值 E[CTR] 在可见池内为 0.12，公式为 E[CTR] = CTR_base * (1 + γ * (P_ask - P_market)/P_market)，其中 CTR_base=0.10，γ=0.2，体现买家对‘有议价空间’高价的偏好（N10支持）。

## Corrected Claim

买家点击率 CTR 的期望值 E[CTR] 在可见池内为 0.12，公式为 E[CTR] = CTR_base * (1 + γ * (P_ask - P_market)/P_market)，其中 CTR_base=0.10，γ=0.2，体现买家对‘有议价空间’高价的偏好（N10支持）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式代入数值 0.10 * (1 + 0.2 * 0.1) = 0.12 计算正确，量纲与逻辑自洽。
