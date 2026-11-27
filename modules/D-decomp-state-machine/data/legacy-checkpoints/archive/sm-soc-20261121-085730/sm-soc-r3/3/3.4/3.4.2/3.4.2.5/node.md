# N236: 最小干预策略D的触发条件：当 E_buyer > 0.55 且 C_buyer > 0.65 时，策略D（信号增强）为最小干预，其成本函数 C_D = c_la

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N76

## Claim

最小干预策略D的触发条件：当 E_buyer > 0.55 且 C_buyer > 0.65 时，策略D（信号增强）为最小干预，其成本函数 C_D = c_label * N_items，其中 c_label 为单个标签生成成本（$0.05），N_items 为受影响商品数。

## Corrected Claim

最小干预策略D的触发条件：当 E_buyer > 0.55 且 C_buyer > 0.65 时，策略D（信号增强）为最小干预，其成本函数 C_D = c_label * N_items，其中 c_label 为单个标签生成成本（$0.05），N_items 为受影响商品数。

## Evidence

先验知识/题面给定，逻辑校验通过
