# N545: 当源站出口带宽 B_origin=10Gbps 且未命中流量峰值需求为 222Mbps 时，链路利用率 U = 222/10000 = 2.2%，此时排队延迟 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N185

## Claim

当源站出口带宽 B_origin=10Gbps 且未命中流量峰值需求为 222Mbps 时，链路利用率 U = 222/10000 = 2.2%，此时排队延迟 T_queue ≈ 0ms，属于低负载高冗余工作点，成本浪费但延迟极低。

## Corrected Claim

当源站出口带宽 B_origin=10Gbps 且未命中流量峰值需求为 222Mbps 时，链路利用率 U = 222/10000 = 2.2%，此时排队延迟 T_queue ≈ 0ms，属于低负载高冗余工作点，成本浪费但延迟极低。

## Evidence

先验知识/题面给定，逻辑校验通过：222Mbps/10Gbps=2.2%计算正确，低负载下排队延迟趋近于0符合排队论直觉
