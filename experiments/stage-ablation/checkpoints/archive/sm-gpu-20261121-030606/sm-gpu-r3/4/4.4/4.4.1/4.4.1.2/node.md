# N312: 计算瓶颈边界条件：当 FLOPs_per_token / Memory_Bandwidth > 1 / Arithmetic_Intensity_Thresho

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133

## Claim

计算瓶颈边界条件：当 FLOPs_per_token / Memory_Bandwidth > 1 / Arithmetic_Intensity_Threshold 时，公式失效，需切换为 Compute-Limited 模型 Throughput = FLOPS / (2 * Params * SeqLen)，该阈值取决于 GPU 的 Tensor Core 效率与内存带宽比

## Corrected Claim

计算瓶颈边界条件：当 FLOPs_per_token / Memory_Bandwidth > 1 / Arithmetic_Intensity_Threshold 时，公式失效，需切换为 Compute-Limited 模型 Throughput = FLOPS / (2 * Params * SeqLen)，该阈值取决于 GPU 的 Tensor Core 效率与内存带宽比

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述准确描述了Roofline模型中计算瓶颈与内存瓶颈的切换条件（算术强度阈值），且Compute-Limited下的吞吐量公式（FLOPS / 总FLOPs）符合基本物理/工程直觉。

## Search Query

memory bound vs compute bound LLM inference threshold arithmetic intensity
