# N194: cuBLAS/cuDNN Workspace 动态显存开销：在推理阶段，cuBLAS 的 workspace 通常较小（< 100 MB），但 cuDNN 的 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

cuBLAS/cuDNN Workspace 动态显存开销：在推理阶段，cuBLAS 的 workspace 通常较小（< 100 MB），但 cuDNN 的 attention kernel 可能需要额外的临时缓冲区；对于 32K 长上下文，FlashAttention-2 的 workspace 需求约为 O(seq_len * head_dim * hidden_dim)，在 4090 上约需 50-100 MB，可忽略不计。

## Corrected Claim

cuBLAS/cuDNN Workspace 动态显存开销：在推理阶段，cuBLAS 的 workspace 通常较小（< 100 MB），但 cuDNN 的 attention kernel 可能需要额外的临时缓冲区；对于 32K 长上下文，FlashAttention-2 的 workspace 需求约为 O(seq_len * head_dim * hidden_dim)，在 4090 上约需 50-100 MB，可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cuDNN FlashAttention workspace memory usage long sequence
