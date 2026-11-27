# N174: 卖家挂价 P_ask 的量化：P_ask = P_median * (1 + ε_seller)，其中 ε_seller 为卖家定价偏差（典型值 0.15-0.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N52

## Claim

卖家挂价 P_ask 的量化：P_ask = P_median * (1 + ε_seller)，其中 ε_seller 为卖家定价偏差（典型值 0.15-0.25），反映卖家乐观偏差或策略性高挂价行为，需基于平台挂价分布估计。

## Corrected Claim

卖家挂价 P_ask 通常高于市场中间价 P_median，可表示为 P_ask = P_median * (1 + ε_seller)，其中 ε_seller 为卖家定价偏差，具体数值需基于特定平台的挂价分布数据估计，不同市场典型值差异较大。

## Evidence

[质询]陈述中给出的具体数值范围（ε_seller 典型值 0.15-0.25）属于经验事实，缺乏通用性，不同市场（如二手车、房产、B2B）的挂价偏差差异巨大，且参考来源未提供该特定数值区间的直接支持。 | 逻辑自洽，但参考来源[1][2][3]仅定性描述了挂价与成交价的差异或趋势，未提供具体的量化偏差系数（0.15-0.25），属于经验事实缺来源直接支持。

## Search Query

seller asking price deviation median used goods platform overpricing bias

## Retrieval Sources

- {'url': 'https://www.carwhere.com/guides/how-much-can-you-negotiate-on-a-used-car&rut=84dd5a08155c41b19865ca96cef975e72b9035d453e7c11bec7308fa2c4855e0', 'type': 'ddg', 'title': 'How Much Can You Negotiate on a Used Car? | CarWhere'}
- {'url': 'https://www.deltabusinessadvisors.com/median-sale-price-vs-asking-price/&rut=cd39dd8fe39492339517ee22cb80d3192ff307ad75108e65b11bd09700c9b2cc', 'type': 'ddg', 'title': 'Median Sale Price vs Asking Price | Delta Business Advisors'}
- {'url': 'https://www.deltabusinessadvisors.com/median-sale-price-vs-asking-price-2/&rut=99eac4d8db34c88b27f538a1f53509259eaf9e51ad486c36e7d2e4121edb9180', 'type': 'ddg', 'title': 'Median Sale Price vs. Asking Price | Delta Business Advisors'}
