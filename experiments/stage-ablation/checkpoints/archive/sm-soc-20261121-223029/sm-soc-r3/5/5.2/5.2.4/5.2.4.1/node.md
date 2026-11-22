# N308: 基线曝光量 Exposure_base 的构成：Exposure_base = N_visitors_24h * P_base_impression，其中 N_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N103

## Claim

基线曝光量 Exposure_base 的构成：Exposure_base = N_visitors_24h * P_base_impression，其中 N_visitors_24h 为平台日均24小时独立访客数，P_base_impression 为单个商品在基准状态下的平均曝光概率（需从平台日志中 δ<0.10 且无特殊标签商品的曝光分布中位数提取）。

## Corrected Claim

基线曝光量 Exposure_base 通常由日均独立访客数与基准曝光概率乘积构成，具体参数提取逻辑（如δ阈值、统计量选择）需依据特定平台日志规范确定。

## Evidence

[质询]该陈述定义了具体的业务指标计算公式及参数提取逻辑（如δ<0.10阈值、中位数提取），属于特定平台或实验设计的经验性定义，无法从第一性原理推导，且缺乏来源支持其具体数值口径的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

second hand marketplace platform daily unique visitors average product impression rate baseline data
