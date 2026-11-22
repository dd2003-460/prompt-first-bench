# N257: 在 Prefill 阶段（长序列、大 Batch 或单用户长上下文），计算受限场景下的 MFU (Model FLOPs Utilization) 经验取值通常

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

在 Prefill 阶段（长序列、大 Batch 或单用户长上下文），计算受限场景下的 MFU (Model FLOPs Utilization) 经验取值通常为 0.6-0.8，受限于矩阵乘法库优化效率及内存访问模式，低于 Decode 阶段的带宽受限瓶颈。

## Corrected Claim

在 Prefill 阶段（长序列、大 Batch 或单用户长上下文），计算受限场景下的 MFU (Model FLOPs Utilization) 经验取值通常为 0.6-0.8，受限于矩阵乘法库优化效率及内存访问模式，低于 Decode 阶段的带宽受限瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference prefill MFU typical value 0.6 0.8
