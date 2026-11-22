# N222: 买家支付意愿 W 的分布参数估计：W ~ N(μ_W, σ_W^2)，需通过平台历史成交数据估计 μ_W 和 σ_W，以计算 P(W > P_ask + C_s

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

买家支付意愿 W 的分布参数估计：W ~ N(μ_W, σ_W^2)，需通过平台历史成交数据估计 μ_W 和 σ_W，以计算 P(W > P_ask + C_search + E[Lemon_Risk])，从而确定买家购买概率。

## Corrected Claim

买家支付意愿 W 的分布参数估计：W 通常服从右偏分布（如对数正态分布），需通过平台历史成交数据估计分布参数，以计算 P(W > P_ask + C_search + E[Lemon_Risk])，从而确定买家购买概率。

## Evidence

[质询]将买家支付意愿（W）假设为正态分布（Normal Distribution）在经济学和实证研究中存在显著缺陷，因为支付意愿通常具有右偏长尾特征且下限为0，正态分布允许负值且无法捕捉长尾，更常见的模型是对数正态分布或帕累托分布。 | 经验事实，逻辑自洽但缺来源支持；正态分布假设虽在简化模型中常见，但作为对支付意愿分布的通用描述缺乏实证稳健性，且无外部来源支持该特定参数化选择。

## Search Query

willingness to pay distribution estimation second hand market
