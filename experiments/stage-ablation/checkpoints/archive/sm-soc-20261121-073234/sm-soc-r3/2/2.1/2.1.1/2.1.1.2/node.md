# N175: 估值标准差 σ_v 的量化：σ_v = sqrt(Var(Bid_i | Item_i))，其中 Bid_i 为同一商品不同买家的出价；在缺乏标准化质检的二手市

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N53

## Claim

估值标准差 σ_v 的量化：σ_v = sqrt(Var(Bid_i | Item_i))，其中 Bid_i 为同一商品不同买家的出价；在缺乏标准化质检的二手市场，σ_v 通常占商品价值 E[V] 的 10%-20%，具体数值需按商品类别（如电子产品 vs 奢侈品）分层计算。

## Corrected Claim

估值标准差 σ_v 的量化：σ_v = sqrt(Var(Bid_i | Item_i))，其中 Bid_i 为同一商品不同买家的出价；在缺乏标准化质检的二手市场，σ_v 通常显著高于标准化市场，具体数值需按商品类别（如电子产品 vs 奢侈品）分层计算，缺乏统一的标准比例。

## Evidence

[质询]该陈述包含具体的经验性数值范围（10%-20%），这属于二手市场特定领域的经验事实，无法从第一性原理或数学定义中直接推导出来，且参考来源未提供相关数据支持。 | 逻辑上，σ_v 定义为条件标准差是合理的，且量纲一致；但参考来源 [1] 和 [2] 均讨论量化交易中的风险指标（VaR/CVaR等），与二手市场估值方差的具体数值范围无关，属于经验事实且缺乏来源支持。

## Search Query

buyer valuation variance used goods market bid dispersion standard deviation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1979964857915810264&rut=bee17705e0b48e7c14332f98466627253c6fb5a32a98945602639d63ae558b45', 'type': 'ddg', 'title': '量化交易中的数学基础 - 知乎专栏'}
- {'url': 'https://zhuanlan.zhihu.com/p/140802624&rut=b6aa28b624152507f20cd69a3eecfc9ec68889aef8f479a4e8d1057eaf5e7487', 'type': 'ddg', 'title': '资产组合VaR 和CVaR值的求解方法 - 知乎'}
