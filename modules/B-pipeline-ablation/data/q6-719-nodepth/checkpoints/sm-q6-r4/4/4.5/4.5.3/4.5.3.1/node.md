# N379: 自建 POP 到源站的 RTT 基础值 RTT_base_origin 由物理距离 d_origin 决定，公式为 RTT_base_origin ≈ 0.05

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N117

## Claim

自建 POP 到源站的 RTT 基础值 RTT_base_origin 由物理距离 d_origin 决定，公式为 RTT_base_origin ≈ 0.05 * d_origin + 5 (ms)，其中 d_origin 为 POP 到源站的数据中心距离，若 d_origin < 100km，RTT_base_origin < 10ms。

## Corrected Claim

自建 POP 到源站的 RTT 基础值 RTT_base_origin 由物理距离 d_origin 决定，公式为 RTT_base_origin ≈ 0.05 * d_origin + 5 (ms)，其中 d_origin 为 POP 到源站的数据中心距离，若 d_origin < 100km，RTT_base_origin < 10ms。

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000 km/s，单程延迟约为0.005 ms/km，往返（RTT）约为0.01 ms/km。公式中0.05 ms/km的系数虽高于纯物理极限（可能包含了交换机处理、协议栈开销等工程经验值），但在工程估算中属于合理量级；且不等式推导正确（0.05*100+5=10ms），逻辑自洽。
