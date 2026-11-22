# N788: M2 Ultra 的 148 TFLOPS 是峰值理论值，实际 LLM 推理中由于算子效率 (MFU, Model FLOPs Utilization) 通常仅

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N245

## Claim

M2 Ultra 的 148 TFLOPS 是峰值理论值，实际 LLM 推理中由于算子效率 (MFU, Model FLOPs Utilization) 通常仅为 30-40%，因此有效算力约为 44-59 TFLOPS。这进一步拉大了与 H100 (MFU 可达 50-60%) 的性能差距，实际 TTFT 可能在 5-8 秒以上，而非 3.0 秒。

## Corrected Claim

M2 Ultra 的 148 TFLOPS 是峰值理论值，实际 LLM 推理中由于算子效率 (MFU) 通常较低（约 30-40%），有效算力约为 44-59 TFLOPS。这导致其在高负载或长序列场景下的性能显著低于 H100，TTFT 可能显著高于 3.0 秒（具体数值取决于模型规模与序列长度）。

## Evidence

[质询]MFU（模型浮点运算利用率）在 LLM 推理（特别是 Prefill 阶段）中通常远低于训练场景，且 M2 Ultra 的内存带宽瓶颈往往先于算力瓶颈出现，导致实际有效算力可能远低于 30-40% 的 MFU 估算；此外，TTFT 5-8 秒的结论高度依赖具体模型大小、序列长度及并发情况，缺乏具体上下文时该数值范围过于武断。 | 先验知识/题面给定，逻辑校验通过：M2 Ultra 148 TFLOPS 为峰值理论值，MFU 30-40% 导致有效算力 44-59 TFLOPS 的数学推导自洽；但 TTFT 具体数值为经验估计，缺乏特定场景约束，故降级为定性表述。

## Search Query

LLM inference MFU utilization rate M-series chip
