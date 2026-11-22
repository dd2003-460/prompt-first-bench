# N163: SwiGLU 激活函数的中间激活值显存占用公式：Activation_Mem = Batch_Size × Seq_Len × Intermediate_Siz

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

SwiGLU 激活函数的中间激活值显存占用公式：Activation_Mem = Batch_Size × Seq_Len × Intermediate_Size × Bytes_per_element × Num_Activation_Tensors。

## Corrected Claim

SwiGLU 激活函数的中间激活值显存占用公式：Activation_Mem = Batch_Size × Seq_Len × Intermediate_Size × Bytes_per_element × Num_Activation_Tensors。

## Evidence

先验知识/题面给定，逻辑校验通过
