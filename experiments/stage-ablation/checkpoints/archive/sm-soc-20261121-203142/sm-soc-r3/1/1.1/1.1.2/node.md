# N27: 高锚定噪声项 ε_anchor 服从均匀分布 U(0, 0.10)，其上限 0.10 由买家搜索过滤阈值 T_search 的相对位置决定，即 ε_max = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N5

## Claim

高锚定噪声项 ε_anchor 服从均匀分布 U(0, 0.10)，其上限 0.10 由买家搜索过滤阈值 T_search 的相对位置决定，即 ε_max = T_search/P_market - δ_loss - 0 = 1.25 - 1.15 = 0.10，确保 P_ask 不超过过滤线。

## Corrected Claim

高锚定噪声项 ε_anchor 服从均匀分布 U(0, 0.10)，其上限 0.10 由买家搜索过滤阈值 T_search 的相对位置决定，即 ε_max = T_search/P_market - δ_loss - 0 = 1.25 - 1.15 = 0.10，确保 P_ask 不超过过滤线。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1.25 - 1.15 = 0.10 正确，且均匀分布 U(0, 0.10) 的定义与上限推导逻辑自洽。
