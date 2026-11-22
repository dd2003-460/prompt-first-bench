# N105: 电价敏感性分析：美国平均电价 $0.15/kWh，欧洲平均 $0.25/kWh，中国居民电价 $0.06/kWh；电价波动 ±50% 会导致年 OpEx 波动 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N28

## Claim

电价敏感性分析：美国平均电价 $0.15/kWh，欧洲平均 $0.25/kWh，中国居民电价 $0.06/kWh；电价波动 ±50% 会导致年 OpEx 波动 ±50%，在 3 年 TCO 中占比约 5-15%（取决于硬件功耗）

## Corrected Claim

电价敏感性分析：美国平均电价约$0.15-0.17/kWh，欧洲平均约$0.25-0.26/kWh，中国居民电价约$0.06-0.09/kWh（视地区及口径而定）；电价波动±50%会导致电力相关OpEx波动±50%，在3年TCO中电力成本占比通常为5-15%（取决于硬件功耗及电价水平）。

## Evidence

[质询]数值偏差：来源[1]显示2026年Q1全球居民平均电价为$0.17/kWh，欧洲平均$0.26/kWh，亚洲平均$0.09/kWh；而陈述中美国$0.15、欧洲$0.25、中国$0.06的数值虽在合理量级内，但与中国/亚洲平均值（$0.09）存在一定偏差，且未明确区分居民/商业/工业电价口径（数据中心通常使用商业或工业电价，通常高于居民电价）。 | 来源[1]和[2]提供了全球及美国电价数据（$0.166-$0.17/kWh），与陈述中的$0.15/kWh量级一致但略有偏差；欧洲$0.25与来源$0.26接近；中国$0.06低于亚洲平均$0.09，可能因特定地区或居民电价口径导致。逻辑上，电价波动±50%直接导致OpEx中电力成本部分波动±50%，若电力成本占TCO 5-15%，则对总TCO影响为2.5-7.5%，陈述中‘年OpEx波动±50%’指电力部分，‘TCO占比5-15%’指电力成本占比，逻辑自洽。但具体数值缺乏直接精确支持，且口径（居民vs商业）未明确，故降级。

## Search Query

average electricity price per kWh USA Europe China 2024 residential commercial

## Retrieval Sources

- {'url': 'https://electricitycostcalc.com/kwh-cost-by-country.html&rut=7276c78b361ffbb9cd2799f232904e6f5c26c6b97fdb31f8ae050fe865f9f491', 'type': 'ddg', 'title': 'Electricity Price by Country 2026 - kWh Cost Worldwide'}
- {'url': 'https://zh.globalpetrolprices.com/USA/electricity_prices/&rut=ebb807476c9bb76c5f7596fef34a675e7a0a167d934c1dfa3a82d5128fe6e72d', 'type': 'ddg', 'title': '美国 电价, 三月 2026 | GlobalPetrolPrices.com'}
- {'url': 'https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_a&rut=6172c3ddfd982d3f88dcdbef0fa4d63aebfd1630372b465e199113ffaa0bd93e', 'type': 'ddg', 'title': 'Electric Power Monthly - U.S. Energy Information Administration (EIA)'}
