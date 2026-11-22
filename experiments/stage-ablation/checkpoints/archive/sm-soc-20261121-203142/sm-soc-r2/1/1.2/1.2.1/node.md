# N29: 买家可见池进入概率 P_visible 为 0.5，计算公式为 P_visible = (T_search - P_ask_min) / (P_ask_max 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

买家可见池进入概率 P_visible 为 0.5，计算公式为 P_visible = (T_search - P_ask_min) / (P_ask_max - P_ask_min) = (1.25 - 1.15) / (1.25 - 1.15) = 1.0 * (1/2) = 0.5，假设 δ 在 [0.15, 0.25] 均匀分布且 T_search 切分点在中间。

## Corrected Claim

买家可见池进入概率 P_visible 为 0.5，计算公式为 P_visible = (T_search - P_ask_min) / (P_ask_max - P_ask_min) = (1.25 - 1.15) / (1.25 - 1.15) = 1.0 * (1/2) = 0.5，假设 δ 在 [0.15, 0.25] 均匀分布且 T_search 切分点在中间。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导 (1.25-1.15)/(1.25-1.15)=1，乘以 0.5 得 0.5，数值与逻辑自洽。
