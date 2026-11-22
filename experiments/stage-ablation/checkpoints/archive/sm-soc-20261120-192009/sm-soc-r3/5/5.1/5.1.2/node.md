# N291: 品类异质性检验：检验奢侈品与日用品的 $\alpha_{risk}$ 是否存在显著差异，模型为 $\alpha_{risk, category} = \alph

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

品类异质性检验：检验奢侈品与日用品的 $\alpha_{risk}$ 是否存在显著差异，模型为 $\alpha_{risk, category} = \alpha_{base} + \delta_{luxury} * Dummy_{luxury}$；若 $\delta_{luxury}$ 显著为正（如 $\alpha_{luxury} = 0.4$ vs $\alpha_{daily} = 0.1$），则统一使用 0.2 会导致奢侈品定价策略被低估风险厌恶，需分品类设定参数。

## Corrected Claim

品类异质性检验：检验奢侈品与日用品的 $\alpha_{risk}$ 是否存在显著差异，模型为 $\alpha_{risk, category} = \alpha_{base} + \delta_{luxury} * Dummy_{luxury}$；若 $\delta_{luxury}$ 显著为正（如 $\alpha_{luxury} = 0.4$ vs $\alpha_{daily} = 0.1$），则统一使用 0.2 会导致奢侈品定价策略被低估风险厌恶，需分品类设定参数。

## Evidence

先验知识/题面给定，逻辑校验通过：模型设定符合计量经济学交互项/分组回归逻辑，数值量级（0.4 vs 0.1）在风险厌恶系数语境下合理，且结论推导（统一参数导致低估）符合逻辑。

## Search Query

category heterogeneity risk aversion luxury vs daily goods pricing
