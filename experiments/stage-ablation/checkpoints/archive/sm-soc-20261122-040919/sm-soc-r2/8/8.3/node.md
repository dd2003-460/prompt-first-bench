# N116: 季节性干扰的量化修正项：设季节性波动幅度为 S%，若 S=10%，则需从观测溢价率中扣除季节性分量；具体公式为 adjusted_premium = obser

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N29

## Claim

季节性干扰的量化修正项：设季节性波动幅度为 S%，若 S=10%，则需从观测溢价率中扣除季节性分量；具体公式为 adjusted_premium = observed_premium - S * seasonal_factor(t)，其中 seasonal_factor(t) 为时间函数，[待核验]：需获取平台历史季节性数据

## Corrected Claim

季节性干扰的量化修正通常采用时间序列分解方法（如X-12-ARIMA），具体修正公式需基于平台历史数据拟合得出，通用形式为 adjusted_premium = observed_premium - seasonal_component(t)，其中 seasonal_component(t) 需通过历史数据估计。

## Evidence

[质询]该公式为经验性修正模型，其具体形式（线性减法）及参数（S, seasonal_factor）依赖于特定平台的历史数据拟合，无法从第一性原理推导，且参考来源仅涉及通用时间序列分解方法，未提供该特定公式的直接支持或验证。 | 逻辑自洽（量纲一致，修正方向合理），但属于经验事实/特定模型参数，参考来源[1]仅介绍通用季节调整方法（如X12），未直接支持该特定公式，故降级。

## Search Query

seasonal adjustment for price premium and transaction cycle in e-commerce second-hand platforms

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/d609c0359b8fcc22bcd126fff705cc1754275f5b.html&rut=9e562e45a8aa34ab4dbd197d0e7b0a227c5ff687350345e0a73976c8a2ce5935', 'type': 'ddg', 'title': '计量经济学第02章 经济时间序列的季节调整、分解和平滑详述'}
