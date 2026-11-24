# N110: 混合方案核心5 POP预置2x峰值的 CapEx 增量 = (2 × Core_Peak_Bandwidth - Core_Average_Bandwidth)

- **status**: pending
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

父节点级核验未通过：非正交（子节点2（Core_Peak_Bandwidth推导）与父节点存在严重矛盾。父节点明确给出假设 'Core_Peak_Bandwidth = 23.1 × 0.6 × 2 = 27.7 Gbps'，而子节点2基于不同的假设（峰值系数3，4小时集中）推导出 '20.25 Gbps'。这种关键参数的数值冲突破坏了正交性，导致父节点的公式在子节点提供的参数下无法复现父节点的结果。）

## Search Query

hybrid CDN core POP bandwidth capex calculation
