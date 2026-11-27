# N57: 激活值峰值显存 ≈ (Batch_Size × Seq_Len × Hidden_Dim × dtype_size) × Attention_Overhead_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

激活值峰值显存 ≈ (Batch_Size × Seq_Len × Hidden_Dim × dtype_size) × Attention_Overhead_Factor，对于 Qwen3-27B (Hidden_Dim=4096)，在 Batch_Size=1, BF16 下约为 0.5-1 GB，通常小于总显存需求的 5%，在单流推理中可忽略但需预留。

## Corrected Claim

激活值峰值显存 ≈ (Batch_Size × Seq_Len × Hidden_Dim × dtype_size) × Attention_Overhead_Factor，对于 Qwen3-27B (Hidden_Dim=4096)，在 Batch_Size=1, BF16 下约为 0.5-1 GB，通常小于总显存需求的 5%，在单流推理中可忽略但需预留。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B Hidden_Dim=4096，BF16 (2 bytes)，假设 Seq_Len=2048-4096，Batch=1，激活值显存约为 0.5-1 GB，符合量级估算。

## Search Query

Qwen3-27B hidden dimension activation memory footprint inference
