# N107: 自建10个POP点预置2x峰值带宽的 CapEx 增量 = (2 × Peak_Bandwidth - Average_Bandwidth) × Bandwid

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

自建10个POP点预置2x峰值带宽的 CapEx 增量 = (2 × Peak_Bandwidth - Average_Bandwidth) × Bandwidth_Capex_Per_Gbps，其中 Peak_Bandwidth = 2TB/日 ÷ 86400s × 86400 = 23.1 Gbps（平均），Peak_Bandwidth_peak = 23.1 × 2 = 46.2 Gbps

## Corrected Claim

自建10个POP点预置2x峰值带宽的 CapEx 增量 = (2 × Peak_Bandwidth - Average_Bandwidth) × Bandwidth_Capex_Per_Gbps，其中 Peak_Bandwidth = 2TB/日 ÷ 86400s × 86400 = 23.1 Gbps（平均），Peak_Bandwidth_peak = 23.1 × 2 = 46.2 Gbps

## Evidence

父节点级核验未通过：不完备（子节点之间逻辑正交，分别聚焦于带宽参数修正、成本构成拆解和预置策略验证，无重复或矛盾。但完备性不足：父节点明确提及“自建10个POP点”，而子节点完全未涉及“POP点数量（10）”对总CapEx的乘数影响（即总CapEx应为单点成本×10，或需考虑多节点间的冗余/聚合效应），这是计算总增量成本的关键缺失环节。）

## Search Query

edge node bandwidth capex per gbps pre-provisioning
