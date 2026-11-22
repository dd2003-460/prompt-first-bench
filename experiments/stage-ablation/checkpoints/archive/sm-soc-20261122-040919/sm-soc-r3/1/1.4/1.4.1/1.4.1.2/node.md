# N163: 买家估值噪声 σ²_buyer_valuation 与共享随机源的耦合：σ²_buyer_valuation = α * σ²_market + β * σ²_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N41

## Claim

买家估值噪声 σ²_buyer_valuation 与共享随机源的耦合：σ²_buyer_valuation = α * σ²_market + β * σ²_idiosyncratic，其中 α 为系统性敏感系数，σ²_idiosyncratic 为个体特异性噪声。α 可通过回归买家估值变化对市场整体价格变动的斜率估计。

## Corrected Claim

买家估值噪声通常可分解为系统性成分和个体特异性成分，具体参数化形式（如线性方差分解）取决于特定模型假设，α可通过回归估计，但需依据具体实证数据验证。

## Evidence

[质询]该陈述描述了一个具体的参数化噪声分解模型（σ² = α*σ²_market + β*σ²_idio）及估计方法，属于经验性建模假设。参考来源[1]仅提到买家估值遵循稀疏线性模型且噪声分布未知，并未具体定义这种特定的方差分解结构或α的回归估计方法；来源[2]讨论的是估值相关性而非噪声方差分解。因此，该具体公式并非来源直接支持的事实，而是基于一般经济学直觉的特定建模选择。 | 逻辑上自洽（方差分解符合统计学直觉），但参考来源[1]和[2]均未直接支持该特定的参数化公式及估计方法，属于经验事实且缺乏直接来源支持。

## Search Query

idiosyncratic vs systematic risk buyer valuation regression coefficient

## Retrieval Sources

- {'url': 'https://arxiv.org/pdf/2610.22516v1&rut=4bd0b677d089c21d3a518bd238cd568f202e95cda9bf4c2af1faf923c8e843f8', 'type': 'ddg', 'title': 'Source-Aware Dynamic Pricing with Strategic Buyers - arXiv.org'}
- {'url': 'https://arxiv.org/html/2111.01851v1&rut=7a7426a22e34c7bd7af9f31fa301112ce63eec27b5834d6fc92822e8cd082cc4', 'type': 'ddg', 'title': 'Private Interdependent Valuations - arXiv.org'}
