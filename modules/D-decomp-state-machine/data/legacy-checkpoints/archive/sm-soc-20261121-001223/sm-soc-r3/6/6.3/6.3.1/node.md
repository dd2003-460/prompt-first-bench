# N196: 基准期（未降价时）的泊松参数 λ_base 的量化估计：定义为降价前 7 天或 30 天窗口内的平均每日咨询率，即 λ_base = N_consult_bas

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N72, N73, N74

## Claim

基准期（未降价时）的泊松参数 λ_base 的量化估计：定义为降价前 7 天或 30 天窗口内的平均每日咨询率，即 λ_base = N_consult_base / T_window；需基于同类目（如电子产品/奢侈品）历史数据回归得出，通常范围为 0.5-2.0 咨询/天。

## Corrected Claim

基准期（未降价时）的泊松参数 λ_base 通常定义为降价前特定窗口（如7天或30天）内的平均每日咨询率（λ_base = N_consult_base / T_window），其具体数值需基于同类目历史数据回归得出，不同类目差异较大。

## Evidence

[质询]该陈述包含具体的经验数值范围（0.5-2.0 咨询/天）和特定的业务定义（降价前7/30天窗口），这些属于特定行业或场景下的经验事实，无法从泊松分布的第一性原理或数学公理中严格推导出来。 | 来源[1]仅介绍泊松回归的一般性统计原理，未提供关于‘咨询率’的具体数值范围或业务定义，属于间接支持/无关；该事实为经验参数，逻辑自洽但缺乏直接来源支持，依据经验事实排除条款降级。

## Search Query

second-hand marketplace average daily inquiry rate baseline poisson parameter

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1981741223195735660&rut=97760f9ec83af8dcb81c77549aa4fb2b4300826261b81c328c2cfae101711f19', 'type': 'ddg', 'title': '泊松回归（Poisson Regression）学习笔记 - 知乎'}
