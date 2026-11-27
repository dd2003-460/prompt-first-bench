# N325: 长期持有尺度（>30天）卖家逐利行为置信度 C_profit,long 需纳入库存积压成本修正项：C_profit,long = C_profit_base *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110, N112, N113

## Claim

长期持有尺度（>30天）卖家逐利行为置信度 C_profit,long 需纳入库存积压成本修正项：C_profit,long = C_profit_base * (1 - β_inventory * I_inventory)，其中 I_inventory 为库存积压指数（定义为当前挂牌天数 / 同类商品平均成交周期），β_inventory 为成本敏感系数，预期范围 0.2-0.4。

## Corrected Claim

长期持有尺度（>30天）卖家逐利行为置信度 C_profit,long 需纳入库存积压成本修正项：C_profit,long = C_profit_base * (1 - β_inventory * I_inventory)，其中 I_inventory 为库存积压指数（定义为当前挂牌天数 / 同类商品平均成交周期），β_inventory 为成本敏感系数，预期范围 0.2-0.4。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

inventory carrying cost impact on seller pricing strategy long term confidence
