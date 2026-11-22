# N358: AllReduce延迟模型：AllReduce时间 = (2 * N * S) / B + 2 * (N-1) * t_lat，其中N为GPU数量（此处N=2）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N152

## Claim

AllReduce延迟模型：AllReduce时间 = (2 * N * S) / B + 2 * (N-1) * t_lat，其中N为GPU数量（此处N=2），S为消息大小（8KB/层），B为有效带宽，t_lat为单向延迟。对于2卡，AllReduce简化为一次AllGather+一次ReduceScatter，通信量为2*S，时间=2*S/B + 2*t_lat。

## Corrected Claim

AllReduce延迟模型：AllReduce时间 = (2 * N * S) / B + 2 * (N-1) * t_lat，其中N为GPU数量（此处N=2），S为消息大小（8KB/层），B为有效带宽，t_lat为单向延迟。对于2卡，AllReduce简化为一次AllGather+一次ReduceScatter，通信量为2*S，时间=2*S/B + 2*t_lat。

## Evidence

先验知识/题面给定，逻辑校验通过：AllReduce在2卡场景下确实等价于一次AllGather和一次ReduceScatter，总通信量为2S，延迟模型符合标准Ring-AllReduce或Tree-AllReduce在N=2时的简化形式。
