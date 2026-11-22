# N103: 平台算法曝光倾斜的 A/B 测试效应量：计算高溢价组（δ > 0.15）与对照组（δ < 0.10）在初始 24 小时内的曝光量差异 ΔExposure，若 Δ

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N27, N28, N29

## Claim

平台算法曝光倾斜的 A/B 测试效应量：计算高溢价组（δ > 0.15）与对照组（δ < 0.10）在初始 24 小时内的曝光量差异 ΔExposure，若 ΔExposure/Exposure_base > 0.2 则支持平台驱动假设，否则置信度 < 0.5。

## Corrected Claim

平台算法曝光倾斜的 A/B 测试效应量：计算高溢价组（δ > 0.15）与对照组（δ < 0.10）在初始 24 小时内的曝光量差异 ΔExposure，若 ΔExposure/Exposure_base 显著高于基线波动（具体阈值需根据历史数据分布确定，如 > 0.2 仅为示例）则支持平台驱动假设，否则置信度 < 0.5。

## Evidence

[质询]该陈述定义了一个具体的经验性阈值（ΔExposure/Exposure_base > 0.2）作为判定平台算法驱动假设的标准，但缺乏行业通用的基准数据或统计显著性依据支持该特定数值（0.2）的合理性，属于未经证实的经验参数设定。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该阈值非第一性原理可推导，属具体实验设计参数）

## Search Query

A/B test exposure bias for high priced items in e-commerce platform algorithms
