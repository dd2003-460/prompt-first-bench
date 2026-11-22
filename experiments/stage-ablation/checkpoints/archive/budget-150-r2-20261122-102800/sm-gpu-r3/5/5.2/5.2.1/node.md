# N111: 美国居民用电平均价格为 $0.16/kWh，但该价格存在显著的地域差异（如加州 > $0.30/kWh, 德克萨斯 < $0.12/kWh），且未包含商业/小型

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36, N37, N38

## Claim

美国居民用电平均价格为 $0.16/kWh，但该价格存在显著的地域差异（如加州 > $0.30/kWh, 德克萨斯 < $0.12/kWh），且未包含商业/小型办公室电价（通常为 $0.08-$0.15/kWh），需根据用户具体部署地点修正

## Corrected Claim

美国居民用电平均价格约为$0.16/kWh，存在显著地域差异（如东北部 > $0.26/kWh, 南部 < $0.17/kWh），商业/小型办公室电价因地区而异，需根据具体部署地点查询当地电价数据。

## Evidence

[质询]陈述中关于商业/小型办公室电价（$0.08-$0.15/kWh）的具体数值范围缺乏参考来源支持，且该范围可能过于简化，未反映不同地区商业电价的显著差异；此外，$0.16/kWh作为全国平均值的精确性需结合最新数据验证（来源[2]显示南部地区平均为$0.164，东北部为$0.265，全国平均可能略高于$0.16）。 | 来源[1]和[2]支持美国居民用电价格存在显著地域差异（如东北部高于南部），但均未直接提供商业/小型办公室电价的具体范围，且来源[2]显示南部地区平均电价接近$0.164，可能使全国平均值略高于$0.16，因此商业电价部分缺乏直接支持。

## Search Query

average residential electricity price by state US 2024 EIA

## Retrieval Sources

- {'url': 'https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_06_b&rut=c32811b8bbb63c435f00237371c36339d2683b68ca4b1981f15aec42ccfbb3cb', 'type': 'ddg', 'title': 'Electric Power Monthly - U.S. Energy Information Administration (EIA)'}
- {'url': 'https://fred.stlouisfed.org/blog/2026/03/electricity-prices-have-increased-and-vary-by-region/&rut=0047179a7c175bc398e979cb7af120c33329bc04e9a7a8e5168f7710321b50ab', 'type': 'ddg', 'title': 'Electricity prices have increased and vary by region - FRED'}
