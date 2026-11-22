# N162: 共享随机源：市场流动性噪声 ε_market ~ N(0, σ²_market)，其中 σ²_market 反映宏观供需波动。σ²_market 可通过平台每日

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N41

## Claim

共享随机源：市场流动性噪声 ε_market ~ N(0, σ²_market)，其中 σ²_market 反映宏观供需波动。σ²_market 可通过平台每日成交量与挂价比的残差方差估计。

## Corrected Claim

共享随机源：市场流动性噪声 ε_market 通常建模为均值为零的正态分布，其方差 σ²_market 反映宏观供需波动。一种可能的估计方法是利用平台每日成交量与挂价比的残差方差，但该方法的有效性需结合具体市场微观结构验证。

## Evidence

[质询]该陈述属于具体的计量经济学建模假设与估计方法，并非第一性原理可推导的数学或物理事实。参考来源仅涉及随机矩阵理论（RMT）在因子分析中的应用，未提供关于“成交量与挂价比残差方差”作为流动性噪声估计量的直接支持或验证，存在方法论上的单一来源缺失风险。 | 逻辑上自洽（残差方差常用于估计噪声），但参考来源[1]主题不匹配且无直接支持，属于经验性建模假设，缺乏外部证据直接验证。

## Search Query

market liquidity noise variance estimation daily trading volume price ratio

## Retrieval Sources

- {'url': 'https://github.com/eluckydog/spectral-gap-factor&rut=1091b383c9081e9e29394e1bc8b47abbda93e8a24cbbdd327e53b221d4a88ba3', 'type': 'ddg', 'title': 'GitHub - eluckydog/spectral-gap-factor: Eigenvalue gap as a market ...'}
