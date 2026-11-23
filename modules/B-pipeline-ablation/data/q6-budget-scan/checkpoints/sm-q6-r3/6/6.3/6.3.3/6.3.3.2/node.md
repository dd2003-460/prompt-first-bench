# N309: 工作点 B（匹配峰值/中成本）：每 POP 预留 10Mbps 出口带宽（总 100Mbps），假设单 Gbps 月租 1000 元，月带宽成本 C_bw^se

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

工作点 B（匹配峰值/中成本）：每 POP 预留 10Mbps 出口带宽（总 100Mbps），假设单 Gbps 月租 1000 元，月带宽成本 C_bw^self = 10 * 0.01Gbps * 1000 元/Gbps = 100 元/月，刚好覆盖 K_peak=2.0 时的峰值需求（单 POP 峰值 ≈ 4.6Mbps），成本效益最优。

## Corrected Claim

工作点 B（匹配峰值/中成本）：每 POP 预留 10Mbps 出口带宽（总 100Mbps），假设单 Gbps 月租 1000 元，月带宽成本 C_bw^self = 10 * 0.01Gbps * 1000 元/Gbps = 100 元/月，刚好覆盖 K_peak=2.0 时的峰值需求（单 POP 峰值 ≈ 4.6Mbps），成本效益最优。

## Evidence

先验知识/题面给定，逻辑校验通过：10Mbps=0.01Gbps，0.01*1000=10元/POP，10个POP共100元，计算无误；10Mbps > 4.6Mbps峰值，覆盖逻辑成立。
