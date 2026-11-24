# N592: P99 合规率 R_compliance 的精确计算公式：R_compliance = 1 - P(P99_latency > T)，其中 P99_latenc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N193

## Claim

P99 合规率 R_compliance 的精确计算公式：R_compliance = 1 - P(P99_latency > T)，其中 P99_latency 的分布需通过蒙特卡洛模拟 RTT 和 T_proc 的联合分布得出，而非简单的比例估算。

## Corrected Claim

P99 合规率 R_compliance 的精确计算公式：R_compliance = 1 - P(P99_latency > T)，其中 P99_latency 的分布需通过蒙特卡洛模拟 RTT 和 T_proc 的联合分布得出，而非简单的比例估算。

## Evidence

先验知识/题面给定，逻辑校验通过：合规率定义为不超标概率，即 1 减去超标概率；对于复杂系统延迟分布，蒙特卡洛模拟是获取联合分布并计算尾部概率（P99）的标准且严谨的方法，逻辑自洽。
