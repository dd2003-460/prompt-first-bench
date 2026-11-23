# N310: 工作点 C（最小带宽/低成本）：每 POP 预留 5Mbps 出口带宽（总 50Mbps），假设单 Gbps 月租 1000 元，月带宽成本 C_bw^self

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

工作点 C（最小带宽/低成本）：每 POP 预留 5Mbps 出口带宽（总 50Mbps），假设单 Gbps 月租 1000 元，月带宽成本 C_bw^self = 10 * 0.005Gbps * 1000 元/Gbps = 50 元/月，但峰值期带宽利用率达 92%，存在丢包和延迟抖动风险。

## Corrected Claim

工作点 C（最小带宽/低成本）：每 POP 预留 5Mbps 出口带宽（总 50Mbps），假设单 Gbps 月租 1000 元，月带宽成本 C_bw^self = 10 * 0.005Gbps * 1000 元/Gbps = 50 元/月，但峰值期带宽利用率达 92%，存在丢包和延迟抖动风险。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 10 * 0.005 * 1000 = 50 正确，带宽利用率与成本逻辑自洽。
