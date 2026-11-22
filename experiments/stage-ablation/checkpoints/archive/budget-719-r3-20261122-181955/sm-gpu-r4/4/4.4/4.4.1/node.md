# N108: GPU 价格波动参数化：RTX 4090 价格服从正态分布 N($1,750, $150) 或均匀分布 U($1,600, $1,900)；A100 80GB 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N32

## Claim

GPU 价格波动参数化：RTX 4090 价格服从正态分布 N($1,750, $150) 或均匀分布 U($1,600, $1,900)；A100 80GB 服从 U($15,000, $18,000)；H100 服从 U($25,000, $30,000)；波动率主要受供应链和新品发布周期影响，历史季度波动幅度约为 5-10%。

## Corrected Claim

GPU价格受供应链和新品发布周期影响，历史季度波动幅度约为5-10%。具体价格分布参数需根据实时市场数据动态调整，不宜固定为单一正态或均匀分布参数。

## Evidence

[质询]具体数值参数（如RTX 4090均值$1750、A100区间$15k-18k、H100区间$25k-30k）属于经验事实，且不同时期/渠道价格差异巨大，缺乏权威来源直接支持这些特定的统计分布参数；来源仅讨论价格影响因素，未提供具体分布参数。 | 来源[1][2]仅定性分析RTX 4090价格影响因素，未提供具体分布参数；A100/H100价格区间无来源覆盖；作为经验事实，逻辑自洽但缺直接来源支持，故降级。

## Search Query

RTX 4090 A100 H100 price volatility 2024 2025 historical data

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_42587866/article/details/152242428&rut=abbb03db0183a7478bea14462cf0cf15bf8ac9e4a6e7d8a1a5c2364dcce2e48f', 'type': 'ddg', 'title': 'Rxt4090显卡的价格走势预测 - Csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_36364707/article/details/152066094&rut=52dc0ddb919d92aa3659fd25c80c6ab0348d246d2c09b6b1d74b8daefd15c543', 'type': 'ddg', 'title': '2025年rtx4090显卡价格预测 - Csdn博客'}
