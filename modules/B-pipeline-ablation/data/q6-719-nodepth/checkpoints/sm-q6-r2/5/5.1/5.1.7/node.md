# N110: 混合方案核心5 POP预置2x峰值的 CapEx 增量 = (2 × Core_Peak_Bandwidth - Core_Average_Bandwidth)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

混合方案核心5 POP预置2x峰值的 CapEx 增量 = (2 × Core_Peak_Bandwidth - Core_Average_Bandwidth) × Bandwidth_Capex_Per_Gbps，其中 Core_Traffic 占比由用户地理分布决定（假设核心区域占 60% 流量），Core_Peak_Bandwidth = 23.1 × 0.6 × 2 = 27.7 Gbps

## Corrected Claim

混合方案核心5 POP预置2x峰值的 CapEx 增量 = (2 × Core_Peak_Bandwidth - Core_Average_Bandwidth) × Bandwidth_Capex_Per_Gbps，其中 Core_Traffic 占比由用户地理分布决定（假设核心区域占 60% 流量），Core_Peak_Bandwidth = 23.1 × 0.6 × 2 = 27.7 Gbps

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合CapEx增量计算逻辑（峰值需求-现有平均/基础能力），数值计算 23.1 * 0.6 * 2 = 27.72 ≈ 27.7 准确，量纲合理。

## Search Query

hybrid CDN core POP bandwidth capex calculation
