# N116: 季节性干扰的量化修正项：设季节性波动幅度为 S%，若 S=10%，则需从观测溢价率中扣除季节性分量；具体公式为 adjusted_premium = obser

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

季节性干扰的量化修正项：设季节性波动幅度为 S%，若 S=10%，则需从观测溢价率中扣除季节性分量；具体公式为 adjusted_premium = observed_premium - S * seasonal_factor(t)，其中 seasonal_factor(t) 为时间函数，[待核验]：需获取平台历史季节性数据

## Corrected Claim

季节性干扰的量化修正通常采用时间序列分解方法（如X-12-ARIMA），具体修正公式需基于平台历史数据拟合得出，通用形式为 adjusted_premium = observed_premium - seasonal_component(t)，其中 seasonal_component(t) 需通过历史数据估计。

## Evidence

父节点级核验未通过：有冗余（子节点在方法论（移动平均、X-12-ARIMA、状态空间）和数据粒度上互斥，正交性良好；覆盖了父节点中[待核验]的历史季节性数据获取这一核心任务，完备性满足。但三个子节点本质上是同一决策变量（精度/成本权衡）的不同离散取值，结构高度同构，属于典型的参数化选项而非独立的逻辑分支，存在结构性冗余。）

## Search Query

seasonal adjustment for price premium and transaction cycle in e-commerce second-hand platforms

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/d609c0359b8fcc22bcd126fff705cc1754275f5b.html&rut=9e562e45a8aa34ab4dbd197d0e7b0a227c5ff687350345e0a73976c8a2ce5935', 'type': 'ddg', 'title': '计量经济学第02章 经济时间序列的季节调整、分解和平滑详述'}
