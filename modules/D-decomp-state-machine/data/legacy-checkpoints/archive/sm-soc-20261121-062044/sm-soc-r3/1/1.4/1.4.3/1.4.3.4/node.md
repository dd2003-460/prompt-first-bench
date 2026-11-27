# N122: 公式有效性边界条件：当 P_markup 超过市场最大可接受溢价 P_max_accept（通常 P_market * 1.5）时，ln(P_willing_h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

公式有效性边界条件：当 P_markup 超过市场最大可接受溢价 P_max_accept（通常 P_market * 1.5）时，ln(P_willing_high) 趋近于 -∞ 或 C_signal 趋近于 0，此时 ΔT_short 不再单调递减，需引入非线性饱和项 exp(-γ * (P_markup - P_max_accept)) 进行修正。

## Corrected Claim

公式有效性边界条件：当 P_markup 超过市场最大可接受溢价 P_max_accept（通常 P_market * 1.5）时，ln(P_willing_high) 趋近于 -∞ 或 C_signal 趋近于 0，此时 ΔT_short 不再单调递减，需引入非线性饱和项 exp(-γ * (P_markup - P_max_accept)) 进行修正。

## Evidence

先验知识/题面给定，逻辑校验通过
