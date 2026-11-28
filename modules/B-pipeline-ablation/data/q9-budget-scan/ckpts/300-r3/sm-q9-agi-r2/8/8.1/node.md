# N118: 端到端科研循环时间 T_cycle 的分解公式：T_cycle = T_inference + T_tool_call + T_retrieval + T_ve

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

端到端科研循环时间 T_cycle 的分解公式：T_cycle = T_inference + T_tool_call + T_retrieval + T_verification，其中 T_inference 为主要变量，受限于 V100 集群的 tokens/s 吞吐率；T_tool_call 和 T_retrieval 为并行可优化的固定开销，T_verification 为串行瓶颈。

## Corrected Claim

端到端科研循环时间 T_cycle 的分解公式：T_cycle = T_inference + T_tool_call + T_retrieval + T_verification，其中 T_inference 为主要变量，受限于 V100 集群的 tokens/s 吞吐率；T_tool_call 和 T_retrieval 为并行可优化的固定开销，T_verification 为串行瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过
