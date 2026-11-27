# N168: 买家估值噪声方差 σ²_buyer_valuation 的量化估计：基于二手市场买家对同类商品价值评估的标准差，通常假设 σ_buyer_valuation ≈

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N43

## Claim

买家估值噪声方差 σ²_buyer_valuation 的量化估计：基于二手市场买家对同类商品价值评估的标准差，通常假设 σ_buyer_valuation ≈ 10%（即标准差为参考价的10%），需通过实证数据校准

## Corrected Claim

买家估值噪声方差 σ²_buyer_valuation 的量化估计：基于二手市场买家对同类商品价值评估的标准差，具体数值（如 σ_buyer_valuation）需根据特定商品类别和市场数据通过实证校准，不存在普适的固定假设值（如10%）。

## Evidence

[质询]该陈述声称“通常假设 σ_buyer_valuation ≈ 10%”，这是一个具体的经验参数。然而，在动态定价或二手市场估值的学术文献中，并没有一个普适的、被广泛公认的“10%”标准假设值。噪声方差通常取决于具体商品类别、市场成熟度及数据分布，不同研究中的假设值差异巨大（从5%到50%不等），将其表述为“通常假设”缺乏普遍性依据，属于将特定场景或作者的主观假设泛化为行业惯例。 | 逻辑上，用标准差量化估值噪声是合理的，且10%在量级上对于二手商品估值差异是可能的（非荒谬值）。但参考来源[1]讨论的是移动目标估值，未提及具体噪声方差数值；[2]讨论信号量化噪声，与买家估值无关；[3]讨论策略性买家，未提供估值噪声的具体统计假设。所有来源均未支持“通常假设为10%”这一具体经验事实，且该事实无法从第一性原理推出，属于缺乏来源支持的经验参数。

## Search Query

second-hand market buyer valuation variance standard deviation

## Retrieval Sources

- {'url': 'https://arxiv.org/pdf/2106.04689&rut=4d787702976535afea8151d6e871941a5295cce07fae71e6921db6014afb5199', 'type': 'ddg', 'title': 'arXiv:2106.04689v1 [cs.GT] 8 Jun 2021'}
- {'url': 'https://zhuanlan.zhihu.com/p/1937528234137875880&rut=0f6d9bb784d734ea74ee251f91bb9f39464cee17d3192e366a3bc9e2a41bf2c5', 'type': 'ddg', 'title': '量化 & 量化噪声 - 知乎 - 知乎专栏'}
- {'url': 'https://arxiv.org/pdf/2610.22516v1&rut=4bd0b677d089c21d3a518bd238cd568f202e95cda9bf4c2af1faf923c8e843f8', 'type': 'ddg', 'title': 'Source-Aware Dynamic Pricing with Strategic Buyers - arXiv.org'}
