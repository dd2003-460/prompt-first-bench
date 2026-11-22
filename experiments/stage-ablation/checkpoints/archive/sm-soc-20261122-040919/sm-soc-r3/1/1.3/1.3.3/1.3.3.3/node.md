# N161: 买家保留价格 v_base 的分布特征：v_base ~ N(μ_v, σ_v²)，其中 μ_v 为市场均价 p_market_avg，σ_v 为买家估值离散度

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

买家保留价格 v_base 的分布特征：v_base ~ N(μ_v, σ_v²)，其中 μ_v 为市场均价 p_market_avg，σ_v 为买家估值离散度。σ_v 的估计需基于买家历史出价与最终成交价差的方差计算。

## Corrected Claim

在简化拍卖模型中，常假设买家保留价格 v_base 服从正态分布 N(μ_v, σ_v²)，其中 μ_v 近似市场均价，σ_v 反映买家估值离散度；具体参数估计需结合特定市场数据（如出价与成交价差）进行校准。

## Evidence

[质询]该陈述属于特定拍卖/市场模型中的经验性假设或定义，而非普适真理。将买家保留价格分布直接设定为正态分布（Normal Distribution）且均值等于市场均价，是一种建模简化，忽略了保留价格通常具有下限（如成本价）且可能呈现偏态分布（如Log-normal）的经济直觉。此外，σ_v 的估计方法（基于出价与成交价差的方差）依赖于特定的市场微观结构假设，并非通用统计事实。 | 参考来源[1]仅介绍多元正态分布的数学性质，未涉及拍卖理论、买家保留价格或市场微观结构，属于无关来源。该事实为经验性建模假设，逻辑上自洽（正态分布常用于近似连续变量），但缺乏直接来源支持，且存在被更复杂分布替代的可能性，故降级。

## Search Query

buyer valuation variance second hand market empirical estimate

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Multivariate_normal_distribution&rut=dfb1e9a4f9b10b314f69f7cbb9b24a2507251782040a03dd8a45847165ff3cc7', 'type': 'ddg', 'title': 'Multivariate normal distribution - Wikipedia'}
