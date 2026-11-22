# N278: 库存压力调节项 Δp_stock：卖家的调整概率随库存天数 D_stock 增加而上升，Δp_stock = 0.01 * D_stock。若平均库存天数为 3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N83

## Claim

库存压力调节项 Δp_stock：卖家的调整概率随库存天数 D_stock 增加而上升，Δp_stock = 0.01 * D_stock。若平均库存天数为 30 天，则 p_adjust 增加 0.3，使得高库存卖家的响应率显著高于低库存卖家，导致市场偏离度压缩呈现非均匀分布。

## Corrected Claim

库存压力调节项 Δp_stock：卖家的调整概率随库存天数 D_stock 增加而上升，Δp_stock = 0.01 * D_stock。若平均库存天数为 30 天，则 p_adjust 增加 0.3，使得高库存卖家的响应率显著高于低库存卖家，导致市场偏离度压缩呈现非均匀分布。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

impact of inventory holding days on seller price adjustment willingness
