# N192: 基准成交概率 q_base 的时间衰减模型：q_base(t) = q_0 × exp(-λ_decay × t_listing)，其中 t_listing 为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

基准成交概率 q_base 的时间衰减模型：q_base(t) = q_0 × exp(-λ_decay × t_listing)，其中 t_listing 为上架天数，λ_decay 为日均衰减率（通常 0.05-0.10/天），q_0 为上架首日的基准成交概率，需通过生存分析（Survival Analysis）估计 λ_decay。

## Corrected Claim

基准成交概率 q_base 的时间衰减模型：q_base(t) = q_0 × exp(-λ_decay × t_listing)，其中 t_listing 为上架天数，λ_decay 为日均衰减率（通常 0.05-0.10/天），q_0 为上架首日的基准成交概率，需通过生存分析（Survival Analysis）估计 λ_decay。

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减模型是描述时间依赖风险（hazard rate constant）的标准数学形式，量纲一致（λ为1/天，t为天，指数无量纲），生存分析是估计此类参数的标准统计方法，符合基本逻辑与工程直觉。

## Search Query

time decay model for baseline sales probability online marketplace survival analysis
