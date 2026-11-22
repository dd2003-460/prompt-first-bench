# N855: 美国平均商业/住宅电价并非统一的 $0.10/kWh，2024 年美国平均零售电价约为 $0.16/kWh（EIA 数据），不同地区（如加州 vs 德克萨斯）差

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N266, N267, N268

## Claim

美国平均商业/住宅电价并非统一的 $0.10/kWh，2024 年美国平均零售电价约为 $0.16/kWh（EIA 数据），不同地区（如加州 vs 德克萨斯）差异显著，需引入变量 P_price 替代固定值。

## Corrected Claim

美国平均商业/住宅电价并非统一的 $0.10/kWh，2024 年美国电力行业平均价格约为 $0.129/kWh（EIA/Wikipedia 数据），不同地区（如加州 vs 德克萨斯）差异显著，需引入变量 P_price 替代固定值。

## Evidence

[质询]数值偏差：陈述中引用的2024年美国平均零售电价约为$0.16/kWh，而参考来源[1]明确给出的2024年行业平均价格为$0.129/kWh，两者存在显著差异（约24%），且来源未直接支持$0.16这一具体数值。 | 来源[1]提供了2024年美国电力行业平均价格为$0.129/kWh的数据，与陈述中的$0.16/kWh不一致，但支持了电价存在地区差异及需引入变量的逻辑；因数值不匹配且缺乏直接支持$0.16的来源，判定为degraded。

## Search Query

US average electricity price per kWh 2024 EIA

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Electricity_sector_of_the_United_States', 'type': 'wikipedia', 'title': 'Electricity sector of the United States'}
- {'url': 'https://en.wikipedia.org/wiki/Cost_of_electricity_by_source', 'type': 'wikipedia', 'title': 'Cost of electricity by source'}
- {'url': 'https://en.wikipedia.org/wiki/Electric_energy_consumption', 'type': 'wikipedia', 'title': 'Electric energy consumption'}
