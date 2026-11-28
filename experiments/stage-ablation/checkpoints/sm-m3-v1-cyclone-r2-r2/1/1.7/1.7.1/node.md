# N41: HURDAT2 数据集中，最大持续风速 (Vmax) > 64 kt 的热带气旋在登陆后首小时 (t=0 to t=1h) 的 Vmax 绝对衰减量中位数约为 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

HURDAT2 数据集中，最大持续风速 (Vmax) > 64 kt 的热带气旋在登陆后首小时 (t=0 to t=1h) 的 Vmax 绝对衰减量中位数约为 10-15 kt，95% 置信区间为 [8, 18] kt。

## Corrected Claim

HURDAT2 数据集中，最大持续风速 (Vmax) > 64 kt 的热带气旋在登陆后首小时 (t=0 to t=1h) 的 Vmax 绝对衰减量通常表现为显著减弱，具体中位数及置信区间需查阅基于该数据集的最新统计分析文献以确认精确数值。

## Evidence

[质询]参考来源仅提供了HURDAT2数据集的定义、格式和访问方式，完全缺失关于‘登陆后首小时Vmax衰减量’的具体统计数值（中位数及置信区间）。该陈述包含具体的经验统计数据（10-15 kt, [8, 18] kt），属于经验事实，无法从第一性原理推导，且现有来源无法验证其数值的准确性。 | 来源[1][2][3]仅描述HURDAT2数据集结构，未提供登陆衰减统计值；该事实为经验数据，逻辑上量级合理（强台风登陆后快速减弱符合物理直觉），但因缺乏直接来源支持具体数值，依据经验事实排除条款降级。

## Search Query

HURDAT2 median maximum sustained wind decay rate first hour after landfall major hurricanes >64 knots

## Retrieval Sources

- {'url': 'https://www.nhc.noaa.gov/data/&rut=8bbf36c24d5e9585a4af7f791439e472dfec89912c0719d2b8529848c11afe54', 'type': 'ddg', 'title': 'NHC Data Archive - National Hurricane Center'}
- {'url': 'https://developers.google.cn/earth-engine/datasets/catalog/NOAA_NHC_HURDAT2_pacific?hl=zh-cn&rut=7d70a2ff73666d9c3b7cb813aaf0eb0940b04bf9ef4afb796f7d317617e1387f', 'type': 'ddg', 'title': 'NOAA NHC HURDAT2 Pacific Hurricane Catalog - Google Developers'}
- {'url': 'https://www.nhc.noaa.gov/data/hurdat/hurdat2-format-nov2019.pdf&rut=686f52a2da47cd9d5e4a2d3e0dbfed4000b09a2c5c0b229b47d9e1f3b8ebd9ac', 'type': 'ddg', 'title': 'PDF The revised Atlantic hurricane database (HURDAT2) - Chris Landsea and ...'}
