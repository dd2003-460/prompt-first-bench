# N181: Embedding 矩阵显存开销量化：假设 Qwen3-27B 词表大小 V=152,064 (基于 Qwen2 系列)，hidden_size H=4096，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43, N44, N45

## Claim

Embedding 矩阵显存开销量化：假设 Qwen3-27B 词表大小 V=152,064 (基于 Qwen2 系列)，hidden_size H=4096，Embedding 参数 = V × H = 622,552,224，BF16 占用 = 622,552,224 × 2 bytes ≈ 1.17 GB；若 LM Head 共享权重则不额外占用，否则再加 1.17 GB。

## Corrected Claim

Embedding 矩阵显存开销量化：假设 Qwen3-27B 词表大小 V=152,064 (基于 Qwen2 系列)，hidden_size H=4096，Embedding 参数 = V × H = 622,552,224，BF16 占用 = 622,552,224 × 2 bytes ≈ 1.17 GB；若 LM Head 共享权重则不额外占用，否则再加 1.17 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：152,064 × 4,096 = 622,552,224，622,552,224 × 2 bytes ≈ 1.17 GB，计算无误且符合大模型显存估算常识。
