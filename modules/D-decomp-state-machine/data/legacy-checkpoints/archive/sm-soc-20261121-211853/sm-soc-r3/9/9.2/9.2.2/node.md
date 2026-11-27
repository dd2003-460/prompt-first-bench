# N175: 控制变量组 $\epsilon_i$ 的构成：必须包含品类（Category）、卖家信誉分（SellerScore）、商品新旧（Condition）及上架时间（

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

控制变量组 $\epsilon_i$ 的构成：必须包含品类（Category）、卖家信誉分（SellerScore）、商品新旧（Condition）及上架时间（TimeSinceListing），以隔离价格对曝光的净效应；若遗漏这些变量，$\beta$ 的估计偏差可能高达 20%-30%。

## Corrected Claim

控制变量组 ε_i 的构成：必须包含品类（Category）、卖家信誉分（SellerScore）、商品新旧（Condition）及上架时间（TimeSinceListing），以隔离价格对曝光的净效应；若遗漏这些变量，可能导致 β 的估计出现显著偏差（具体幅度取决于数据分布和模型设定）。

## Evidence

[质询]声称遗漏控制变量会导致β估计偏差高达20%-30%是一个具体的经验性数值断言，缺乏普遍适用的理论依据或广泛认可的基准数据支持，不同数据集和模型设定下偏差幅度差异极大，该具体数值范围可能过于武断或仅适用于特定未说明的场景。 | 先验知识/题面给定，逻辑校验通过（控制变量法原理正确），但具体偏差数值（20%-30%）属于经验事实且无来源支持，故降级。

## Search Query

multivariate regression control variables omitted variable bias magnitude
