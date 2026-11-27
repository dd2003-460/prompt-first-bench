# N90: 初始挂价偏差 δ 与损失厌恶系数 λ 的非线性关系：P_ask = P* * (1 + δ)，其中 δ = f(λ, P*)，具体形式为 δ = λ * (P*

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

初始挂价偏差 δ 与损失厌恶系数 λ 的非线性关系：P_ask = P* * (1 + δ)，其中 δ = f(λ, P*)，具体形式为 δ = λ * (P* - E[Deal_Price]) / P*，需通过实证回归确定 f 的函数形式（线性或凸性）。

## Corrected Claim

初始挂价偏差 δ 与损失厌恶系数 λ 存在非线性关系，具体函数形式 δ = f(λ, P*) 需通过实证回归确定，现有理论未给出统一的线性解析式。

## Evidence

[质询]该陈述将初始挂价偏差 δ 与损失厌恶系数 λ 的关系具体化为一个特定的线性公式 δ = λ * (P* - E[Deal_Price]) / P*，并声称需通过实证回归确定其形式。然而，行为经济学中损失厌恶（Loss Aversion）通常通过前景理论（Prospect Theory）中的价值函数斜率差异来刻画，并不直接存在一个公认的、将初始挂价偏差直接表示为 λ 与价格差线性乘积的标准理论公式。该具体函数形式缺乏理论依据，且参考来源中未包含任何关于此特定定价公式的内容，属于缺乏来源支持的特定经验/模型假设。 | 逻辑上量纲自洽（δ为无量纲比率，右侧分子为价格差，分母为价格，λ为系数），但参考来源[1]-[4]仅涉及管理经济学、金融概览、经济学定义及损失厌恶的一般定义，均未提及或支持该特定的挂价偏差公式，属于经验事实/模型假设且缺来源直接支持。

## Search Query

seller pricing bias loss aversion function form empirical regression

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Managerial_economics', 'type': 'wikipedia', 'title': 'Managerial economics'}
- {'url': 'https://en.wikipedia.org/wiki/Outline_of_finance', 'type': 'wikipedia', 'title': 'Outline of finance'}
- {'url': 'https://en.wikipedia.org/wiki/Economics', 'type': 'wikipedia', 'title': 'Economics'}
- {'url': 'https://en.wikipedia.org/wiki/Loss_aversion&rut=763025b285f26f0e779fd88040fd48d98f6a424cbe58a47d992939ae0de68d67', 'type': 'ddg', 'title': 'Loss aversion - Wikipedia'}
