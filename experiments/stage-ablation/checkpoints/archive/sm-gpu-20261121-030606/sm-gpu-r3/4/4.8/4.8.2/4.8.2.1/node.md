# N345: H100 SXM 在 30% 负载率 (Duty Cycle) 下的年均电力成本为 0.36kW × 8760h × $0.10/kWh = $315.36，相

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N148

## Claim

H100 SXM 在 30% 负载率 (Duty Cycle) 下的年均电力成本为 0.36kW × 8760h × $0.10/kWh = $315.36，相比 N148 中 40% 负载率的 $420.5 降低 25%，需结合本地工作站实际开机与高负载时长分布进行敏感性分析。

## Corrected Claim

H100 SXM 在 30% 负载率 (Duty Cycle) 下的年均电力成本为 0.36kW × 8760h × $0.10/kWh = $315.36，相比 N148 中 40% 负载率的 $420.5 降低 25%，需结合本地工作站实际开机与高负载时长分布进行敏感性分析。

## Evidence

先验知识/题面给定，逻辑校验通过：0.36kW × 8760h × $0.10/kWh = $315.36 计算正确；$315.36 相比 $420.5 降低约 25% 符合数学逻辑；作为 knowledge 节点，无需外部来源支持。
