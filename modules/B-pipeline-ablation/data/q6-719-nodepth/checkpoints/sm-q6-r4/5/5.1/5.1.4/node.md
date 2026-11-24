# N107: 自建10个POP点预置2x峰值带宽的 CapEx 增量 = (2 × Peak_Bandwidth - Average_Bandwidth) × Bandwid

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（三个子节点分别针对公式中的三个关键变量/假设（峰值带宽定义、CapEx单价构成、预置倍数合理性）进行独立拆解，彼此正交且无重复。它们共同覆盖了父节点公式中所有需要进一步细化或验证的环节，逻辑完备。）

## Search Query

edge node bandwidth capex per gbps pre-provisioning
