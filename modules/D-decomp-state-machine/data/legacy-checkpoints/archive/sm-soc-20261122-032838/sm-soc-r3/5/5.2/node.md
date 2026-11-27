# N91: 质量方差 $\sigma_{quality}$ 的计算基准：$\sigma_{quality}$ 应定义为近期同类商品成交价的标准差与均价之比（变异系数 CV）

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

质量方差 $\sigma_{quality}$ 的计算基准：$\sigma_{quality}$ 应定义为近期同类商品成交价的标准差与均价之比（变异系数 CV）。在二手电子产品市场，$\sigma_{quality}$ 典型值为 0.1-0.2；在二手家具/艺术品市场，$\sigma_{quality}$ 可达 0.3-0.5。需区分品类以校准 $T_{tol}$ 的绝对值。

## Corrected Claim

质量方差 $\sigma_{quality}$ 的计算基准：$\sigma_{quality}$ 应定义为近期同类商品成交价的标准差与均价之比（变异系数 CV）。在二手电子产品市场，$\sigma_{quality}$ 典型值为 0.1-0.2；在二手家具/艺术品市场，$\sigma_{quality}$ 可达 0.3-0.5。需区分品类以校准 $T_{tol}$ 的绝对值。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上正交（互斥的市场场景）且覆盖了父节点提到的典型市场范围（家具/艺术品、电子产品、标准化商品），具备完备性。然而，这三个子节点本质上是同一数学模型（σ_quality -> β -> T_tol）在不同参数区间下的实例化。它们重复了相同的推导逻辑和公式结构，仅参数取值不同，属于典型的‘参数化冗余’。）

## Search Query

second-hand market price coefficient of variation by category electronics vs furniture
