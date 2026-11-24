# N149: 在跨洋链路（距离 d=10,000km）场景下，修正光速 c_fiber=2×10^8 m/s 计算单向延迟为 10,000km / (2×10^8 m/s) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

在跨洋链路（距离 d=10,000km）场景下，修正光速 c_fiber=2×10^8 m/s 计算单向延迟为 10,000km / (2×10^8 m/s) = 50ms，RTT=100ms；该场景下光速修正对总延迟影响较小（相比路由跳数延迟），但在短距离高精度估算中必须使用修正值。

## Corrected Claim

在跨洋链路（距离 d=10,000km）场景下，修正光速 c_fiber=2×10^8 m/s 计算单向延迟为 10,000km / (2×10^8 m/s) = 50ms，RTT=100ms；该场景下光速修正对总延迟影响较小（相比路由跳数延迟），但在短距离高精度估算中必须使用修正值。

## Evidence

先验知识/题面给定，逻辑校验通过：10,000km / (2×10^8 m/s) = 0.05s = 50ms，RTT=100ms，计算正确且符合光纤传输物理常识。

## Search Query

transoceanic fiber latency 10000km 50ms one-way
