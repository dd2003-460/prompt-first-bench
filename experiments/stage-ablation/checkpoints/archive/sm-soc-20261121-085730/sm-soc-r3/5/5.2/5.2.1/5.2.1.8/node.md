# N326: 库存积压指数 I_inventory 的动态计算：I_inventory(t) = t_listing / T_avg_turnover，其中 t_listin

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110, N112, N113

## Claim

库存积压指数 I_inventory 的动态计算：I_inventory(t) = t_listing / T_avg_turnover，其中 t_listing 为当前商品挂牌天数，T_avg_turnover 为过去90天同类商品平均成交周期（天），当 I_inventory > 2.0 时，卖家降价动机显著增强，C_profit,long 应上调。

## Corrected Claim

库存积压指数 I_inventory 的动态计算：I_inventory(t) = t_listing / T_avg_turnover，其中 t_listing 为当前商品挂牌天数，T_avg_turnover 为过去90天同类商品平均成交周期（天），当 I_inventory > 2.0 时，卖家降价动机显著增强，C_profit,long 应上调。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

inventory turnover ratio definition used goods platform long term holding cost
