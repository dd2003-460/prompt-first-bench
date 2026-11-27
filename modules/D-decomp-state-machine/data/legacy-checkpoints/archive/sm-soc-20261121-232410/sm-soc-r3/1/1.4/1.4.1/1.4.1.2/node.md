# N116: 下游投影1：季节性修正因子 S_season，定义为当前月份平均成交价与年度平均成交价的比值偏差，在3C类目中Q4（10-12月）S_season中位数为1.1

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N40

## Claim

下游投影1：季节性修正因子 S_season，定义为当前月份平均成交价与年度平均成交价的比值偏差，在3C类目中Q4（10-12月）S_season中位数为1.15，服饰类目中Q2（4-6月）S_season中位数为0.85。

## Corrected Claim

下游投影1：季节性修正因子 S_season，定义为当前月份平均成交价与年度平均成交价的比值偏差，在3C类目中Q4（10-12月）S_season通常大于1，服饰类目中Q2（4-6月）S_season通常小于1。

## Evidence

[质询]具体数值（1.15和0.85）属于特定市场经验数据，缺乏通用性，且不同年份、不同平台数据可能存在显著波动，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

seasonal price index second-hand electronics vs clothing quarterly variation
