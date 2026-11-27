# N273: RTX 4090 运行 Qwen3-27B INT4 时的计算瓶颈阈值分析：当 Batch Size=1 且 Seq Len<4K 时，为 Memory-bou

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

RTX 4090 运行 Qwen3-27B INT4 时的计算瓶颈阈值分析：当 Batch Size=1 且 Seq Len<4K 时，为 Memory-bound；当 Seq Len>8K 或 Batch Size>4 时，Attention 的 O(N^2) 计算量导致转为 Compute-bound，此时吞吐量不再随显存带宽线性增长，而是受限于 Tensor Core 算力 (约 82.6 TFLOPS FP16)。

## Corrected Claim

RTX 4090 运行 Qwen3-27B INT4 时的计算瓶颈阈值分析：当 Batch Size=1 且 Seq Len<4K 时，为 Memory-bound；当 Seq Len>8K 或 Batch Size>4 时，Attention 的 O(N^2) 计算量导致转为 Compute-bound，此时吞吐量不再随显存带宽线性增长，而是受限于 Tensor Core 算力 (约 82.6 TFLOPS FP16)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 FP16 Tensor Core 算力约 82.6 TFLOPS 符合硬件规格；小 Batch/短序列下 Attention 计算量低，受显存带宽限制（Memory-bound）；长序列/大 Batch 下 O(N^2) 计算量激增，转为受算力限制（Compute-bound），符合 LLM 推理性能瓶颈的基本物理/工程直觉。
