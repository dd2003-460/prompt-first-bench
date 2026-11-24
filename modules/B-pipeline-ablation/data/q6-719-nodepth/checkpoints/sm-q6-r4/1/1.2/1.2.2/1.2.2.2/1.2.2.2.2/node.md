# N468: Pareto 分布最小值 x_min 的确定：x_min 应取为网络 RTT 的物理下限，即光传播延迟 + 协议栈处理延迟，典型值约为 1ms (本地) 至 2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

Pareto 分布最小值 x_min 的确定：x_min 应取为网络 RTT 的物理下限，即光传播延迟 + 协议栈处理延迟，典型值约为 1ms (本地) 至 20ms (跨国)，需根据用户地理分布加权确定全局 x_min。

## Corrected Claim

Pareto 分布最小值 x_min 的确定：x_min 应取为网络 RTT 的物理下限，即光传播延迟 + 协议栈处理延迟，典型值约为 1ms (本地) 至 20ms (跨国)，需根据用户地理分布加权确定全局 x_min。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布用于建模网络延迟时，x_min确实对应物理及协议栈处理的最小延迟下限，1ms-20ms的量级符合本地至跨国网络的典型RTT物理极限。
