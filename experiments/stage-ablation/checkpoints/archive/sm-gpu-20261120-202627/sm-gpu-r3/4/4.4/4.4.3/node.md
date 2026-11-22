# N115: 隐性 TCO 折算公式：隐性成本增加 = (Throughput_NVLink - Throughput_PCIe) / Throughput_NVLink ×

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

隐性 TCO 折算公式：隐性成本增加 = (Throughput_NVLink - Throughput_PCIe) / Throughput_NVLink × (OpEx_per_hour + CapEx_annualized / 8760)，用于计算因吞吐量降低导致的额外运营时间成本 [knowledge]

## Corrected Claim

隐性 TCO 折算公式：隐性成本增加 = (Throughput_NVLink - Throughput_PCIe) / Throughput_NVLink × (OpEx_per_hour + CapEx_annualized / 8760)，用于计算因吞吐量降低导致的额外运营时间成本 [knowledge]

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中不同参数取值下的具体应用场景（基准、典型瓶颈、极端瓶颈），彼此独立且互不重叠；通过三个典型工作点（A/B/C）完整覆盖了公式在不同吞吐量差距和成本结构下的应用逻辑，体现了公式的适用范围；虽然本质上是同一公式的不同参数代入，但作为[knowledge]节点，展示不同工况下的具体计算实例和结论判断（如性价比反转、可行性评估）具有独立的认知价值，不属于简单的参数冗余，而是必要的案例展开。）
