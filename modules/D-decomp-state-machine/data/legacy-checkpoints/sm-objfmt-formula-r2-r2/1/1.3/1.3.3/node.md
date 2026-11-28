# N42: vLLM 中激活值内存占用取决于批处理大小 Batch Size 和序列长度，公式为 Activation_Mem ≈ Batch_Size × Seq_Len

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

vLLM 中激活值内存占用取决于批处理大小 Batch Size 和序列长度，公式为 Activation_Mem ≈ Batch_Size × Seq_Len × Hidden_Dim × Dtype_Bytes × Num_Activations_Layers，其中 Num_Activations_Layers 通常取 1-2 层（仅缓存当前层和下一层的激活值）。

## Corrected Claim

vLLM 中激活值内存占用取决于批处理大小 Batch Size 和序列长度，公式为 Activation_Mem ≈ Batch_Size × Seq_Len × Hidden_Dim × Dtype_Bytes × Num_Activations_Layers，其中 Num_Activations_Layers 通常取 1-2 层（仅缓存当前层和下一层的激活值）。

## Evidence

先验知识/题面给定，逻辑校验通过
