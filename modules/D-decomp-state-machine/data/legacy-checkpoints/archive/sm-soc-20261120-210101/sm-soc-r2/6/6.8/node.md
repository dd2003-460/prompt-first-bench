# N110: '库存积压'标签的代理变量量化：若商品挂价时间 T_list > 30天 且 期间无任何咨询，则标记为'潜在积压'；或若卖家近30天上架商品数 N_list >

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

'库存积压'标签的代理变量量化：若商品挂价时间 T_list > 30天 且 期间无任何咨询，则标记为'潜在积压'；或若卖家近30天上架商品数 N_list > 5，则标记为'多库存卖家'。这些标签需作为控制变量进入回归模型。

## Corrected Claim

'库存积压'标签的代理变量量化：若商品挂价时间 T_list > 30天 且 期间无任何咨询，则标记为'潜在积压'；或若卖家近30天上架商品数 N_list > 5，则标记为'多库存卖家'。这些标签需作为控制变量进入回归模型。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

inventory overstock proxy variable listing age seller activity
