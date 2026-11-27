# N154: 单位 Token 能耗对比：Mac Studio (M2 Ultra) 的单位 Token 能耗 (Joule/Token) = P_avg_MacStudio

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

单位 Token 能耗对比：Mac Studio (M2 Ultra) 的单位 Token 能耗 (Joule/Token) = P_avg_MacStudio / Throughput_MacStudio；RTX 4090 的单位 Token 能耗 = P_avg_4090 / Throughput_4090。若 M2 Ultra 吞吐量为 RTX 4090 的 70% 且功耗为 50% (150W vs 300W)，则单位 Token 能耗比 = (150/0.7) / (300/1.0) = 0.714，即 M2 Ultra 每 Token 能耗低 28.6%，抵消了部分硬件成本劣势。

## Corrected Claim

单位 Token 能耗对比：Mac Studio (M2 Ultra) 的单位 Token 能耗 (Joule/Token) = P_avg_MacStudio / Throughput_MacStudio；RTX 4090 的单位 Token 能耗 = P_avg_4090 / Throughput_4090。若 M2 Ultra 吞吐量为 RTX 4090 的 70% 且功耗为 50% (150W vs 300W)，则单位 Token 能耗比 = (150/0.7) / (300/1.0) = 0.714，即 M2 Ultra 每 Token 能耗低 28.6%，抵消了部分硬件成本劣势。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导 (150/0.7)/(300/1.0) = 0.714 正确，28.6% 的能耗降低计算无误，符合物理直觉。
