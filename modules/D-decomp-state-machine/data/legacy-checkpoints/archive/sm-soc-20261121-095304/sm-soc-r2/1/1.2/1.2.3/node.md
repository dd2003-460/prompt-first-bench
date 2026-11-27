# N26: 剩余买家成交意愿概率 f(k) 的非线性函数：f(k) = 1 - Φ((k - k_threshold) / σ_f)，其中 Φ 为标准正态分布 CDF，k_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

剩余买家成交意愿概率 f(k) 的非线性函数：f(k) = 1 - Φ((k - k_threshold) / σ_f)，其中 Φ 为标准正态分布 CDF，k_threshold 为买家容忍价格溢价的阈值（通常 1.0-1.5），σ_f 为买家容忍度分布的标准差，该函数解释了为何 k>1 时 f(k) 不单调下降。

## Corrected Claim

剩余买家成交意愿概率 f(k) 可建模为非线性函数，例如 f(k) = 1 - Φ((k - k_threshold) / σ_f)，其中 k_threshold 和 σ_f 为反映买家容忍度的参数，该函数描述了 k>1 时 f(k) 的下降趋势。

## Evidence

[质询]该陈述包含具体的经验参数（k_threshold 通常 1.0-1.5）和特定的函数形式假设，属于经验事实而非第一性原理可推导的数学恒等式；且参考来源均未提供关于买家成交意愿概率 f(k) 的具体函数形式或阈值范围的支持。 | 逻辑上，使用正态分布 CDF 的补集来建模意愿随价格溢价的衰减是合理的，且 k>1 时 f(k) 下降符合直觉；但来源 [1][2][3] 仅涉及保险、信息不对称和拍卖的一般定义，未覆盖该具体模型参数，属于经验事实缺来源支持。

## Search Query

buyer willingness to pay probability function price premium threshold second hand market

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Insurance', 'type': 'wikipedia', 'title': 'Insurance'}
- {'url': 'https://en.wikipedia.org/wiki/Information_asymmetry', 'type': 'wikipedia', 'title': 'Information asymmetry'}
- {'url': 'https://en.wikipedia.org/wiki/Auction', 'type': 'wikipedia', 'title': 'Auction'}
