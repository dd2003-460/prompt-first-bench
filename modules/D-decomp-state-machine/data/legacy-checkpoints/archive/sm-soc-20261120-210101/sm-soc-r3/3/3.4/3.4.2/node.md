# N70: 透明化系数 η_transparency 的实证估算：通过A/B测试或历史数据回归，估算展示均价后高挂价幅度的压缩比例。公式：η = (ΔP_high_old 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

透明化系数 η_transparency 的实证估算：通过A/B测试或历史数据回归，估算展示均价后高挂价幅度的压缩比例。公式：η = (ΔP_high_old - ΔP_high_new) / ΔP_high_old。需确定 η 的置信区间，若 η ∈ [0.5, 0.8] 且统计显著，则支持‘透明化能显著压缩高溢价’的断言。

## Corrected Claim

透明化系数 η_transparency 的实证估算：通过A/B测试或历史数据回归，估算展示均价后高挂价幅度的压缩比例。公式：η = (ΔP_high_old - ΔP_high_new) / ΔP_high_old。需确定 η 的置信区间，若 η 显著大于 0 且统计显著，则支持‘透明化能显著压缩高溢价’的断言（具体阈值需根据特定业务场景的历史数据分布确定）。

## Evidence

[质询]该陈述包含具体的经验性数值区间（η ∈ [0.5, 0.8]）作为判定标准，这属于经验事实而非第一性原理可推导的数学或逻辑结论。缺乏外部来源支持该特定数值区间的普适性或准确性，且不同市场/品类下透明化对溢价的影响程度差异巨大，直接断言该区间为有效判定标准存在过度概括风险。 | 经验事实，逻辑自洽但缺来源支持。公式定义在逻辑上自洽，但具体的置信区间 [0.5, 0.8] 属于经验参数，无检索来源支持，且无法从第一性原理严格推出，故降级。

## Search Query

price transparency intervention effect on listing price premium A/B test
