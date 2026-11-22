# N87: TTFT（首Token延迟）的理论下限公式：TTFT_min ≈ (Num_Layers * (2 * Num_Parameters / Batch_Size)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

TTFT（首Token延迟）的理论下限公式：TTFT_min ≈ (Num_Layers * (2 * Num_Parameters / Batch_Size)) / (Memory_Bandwidth * Precision_Factor)；对于27B模型，在32K上下文下，Prefill阶段是Compute-bound而非Memory-bound，因此TTFT主要受FLOPS限制，而非带宽。

## Corrected Claim

TTFT（首Token延迟）的理论下限公式：TTFT_min ≈ (Num_Layers * (2 * Num_Parameters / Batch_Size)) / (Memory_Bandwidth * Precision_Factor)；对于27B模型，在32K上下文下，Prefill阶段是Compute-bound而非Memory-bound，因此TTFT主要受FLOPS限制，而非带宽。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型在32K上下文下，Prefill阶段计算量巨大，通常处于Compute-bound状态，TTFT主要受FLOPS限制而非带宽，符合大模型推理的基本物理直觉。

## Search Query

LLM prefill phase compute bound vs memory bound latency
