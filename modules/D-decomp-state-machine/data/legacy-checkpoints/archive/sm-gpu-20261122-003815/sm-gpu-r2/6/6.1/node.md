# N36: 性价比指标定义：性价比 = (Performance_Metric / Cost_Metric)。Performance_Metric 可选：tokens/se

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

性价比指标定义：性价比 = (Performance_Metric / Cost_Metric)。Performance_Metric 可选：tokens/second (吞吐) 或 latency (延迟)。Cost_Metric 可选：Purchase_Cost (初始) 或 TCO (全生命周期)。需明确选择口径，例如 '每美元获得的 tokens/second'。

## Corrected Claim

性价比指标定义：性价比 = (Performance_Metric / Cost_Metric)。Performance_Metric 可选：tokens/second (吞吐) 或 latency (延迟)。Cost_Metric 可选：Purchase_Cost (初始) 或 TCO (全生命周期)。需明确选择口径，例如 '每美元获得的 tokens/second'。

## Evidence

父节点级核验未通过：不完备（子节点1仅定义了Performance_Metric（吞吐），子节点2定义了综合指标（基于吞吐和TCO）。父节点明确提到Performance_Metric可选'latency'，Cost_Metric可选'Purchase_Cost'，但子节点未涵盖延迟指标或初始购买成本的定义，导致覆盖不全。）
