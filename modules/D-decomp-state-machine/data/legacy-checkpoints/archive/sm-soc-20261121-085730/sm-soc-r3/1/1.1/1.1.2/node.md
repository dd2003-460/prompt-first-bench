# N45: 卖家保留价R的分布特征：R ~ N(μ_R, σ_R²)，其中μ_R ≈ 0.85 * C_ref（近期成交价），σ_R ≈ 0.15 * C_ref，导致高估

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

卖家保留价R的分布特征：R ~ N(μ_R, σ_R²)，其中μ_R ≈ 0.85 * C_ref（近期成交价），σ_R ≈ 0.15 * C_ref，导致高估保留价源于分布右偏而非单纯系数放大。

## Corrected Claim

卖家保留价R的分布特征通常被建模为围绕近期成交价的分布，具体均值和标准差系数（如0.85和0.15）及右偏成因需依据特定市场数据或模型假设确定，当前缺乏通用来源支持该具体数值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于分布的定义与统计性质（均值、方差及偏度近似），子节点2聚焦于基于该分布的具体分位数推导及其市场含义。两者分别处理“分布本体”与“分布应用/投影”，内容不重叠且互补，共同完整覆盖了父节点关于分布特征及其导致高估保留价机制的描述。）

## Search Query

used goods market seller reservation price distribution relative to recent transaction price

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Coefficient_of_determination&rut=072a1dfa8feb84c3dfb42aa299ec67cd0ebd908733115afcb5f9a4ddc7ac1b7c', 'type': 'ddg', 'title': 'Coefficient of determination - Wikipedia'}
