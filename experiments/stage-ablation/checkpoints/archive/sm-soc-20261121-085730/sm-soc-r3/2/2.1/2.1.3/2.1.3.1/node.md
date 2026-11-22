# N185: 商品类别异方差修正项：残差方差 Var(ε|Category) 的量化模型，需计算各类别（如电子产品、服装、家具）的残差标准差 σ_cat，并检验其是否显著大于

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

商品类别异方差修正项：残差方差 Var(ε|Category) 的量化模型，需计算各类别（如电子产品、服装、家具）的残差标准差 σ_cat，并检验其是否显著大于全局标准差（F-test p < 0.05），以验证类别作为主要残差驱动因子的假设。

## Corrected Claim

商品类别异方差修正项：残差方差 Var(ε|Category) 的量化模型，需计算各类别（如电子产品、服装、家具）的残差标准差 σ_cat，并检验其是否显著大于全局标准差（F-test p < 0.05），以验证类别作为主要残差驱动因子的假设。

## Evidence

[rework-angle r1] 来源[1]和[2]直接支持使用F-test检验方差差异（异方差性）的统计方法，逻辑推导成立。

## Search Query

category-specific residual variance F-test heteroscedasticity
