# N228: 共享随机源：买家认知噪声 ε_cognition，定义为同一商品在不同买家手中点击次数 N_clicks 的波动标准差 σ_clicks，需通过追踪同一商品被不

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

共享随机源：买家认知噪声 ε_cognition，定义为同一商品在不同买家手中点击次数 N_clicks 的波动标准差 σ_clicks，需通过追踪同一商品被不同用户浏览的路径数据估计，假设 σ_clicks ≈ 0.8 clicks [待核验]。

## Corrected Claim

共享随机源：买家认知噪声 ε_cognition，定义为同一商品在不同买家手中点击次数 N_clicks 的波动标准差 σ_clicks，需通过追踪同一商品被不同用户浏览的路径数据估计，其具体数值需根据实际业务数据校准，此处暂设为 0.8 clicks 作为初始假设。

## Evidence

[质询]该数值（0.8 clicks）属于具体的经验统计参数，缺乏公开文献或标准数据集的直接支持，且不同平台/品类的点击波动率差异巨大，单一数值假设可能过于简化。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值0.8的准确性）

## Search Query

user click path variance same product different users behavioral data
