# N296: 全概率公式中的 P(Active) 即主动降价卖家占比，需通过平台日志统计 t 天内主动降价商品数 N_active 除以总降价商品数 N_total 得到，该

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

全概率公式中的 P(Active) 即主动降价卖家占比，需通过平台日志统计 t 天内主动降价商品数 N_active 除以总降价商品数 N_total 得到，该值直接决定修正项的权重。

## Corrected Claim

全概率公式中的 P(Active) 即主动降价卖家占比，需通过平台日志统计 t 天内主动降价商品数 N_active 除以总降价商品数 N_total 得到，该值直接决定修正项的权重。

## Evidence

先验知识/题面给定，逻辑校验通过：全概率公式中 P(Active) 作为权重项，其定义为条件概率或占比，通过统计主动降价商品数与总降价商品数之比符合概率论基本定义及业务逻辑。
