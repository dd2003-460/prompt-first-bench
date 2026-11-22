# N127: 注意力激活值占用计算：对于每层，注意力分数矩阵大小为 (batch_size * n_heads * seq_len * seq_len)。若使用Flash A

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

注意力激活值占用计算：对于每层，注意力分数矩阵大小为 (batch_size * n_heads * seq_len * seq_len)。若使用Flash Attention，则显存占用降至 O(seq_len) 级别，不再随 seq_len^2 增长。Qwen3-27B若支持Flash Attention，激活值峰值将显著低于2.5GB，N20的2.5GB估算可能基于非Flash Attention路径或包含了KV Cache。

## Corrected Claim

注意力激活值占用计算：对于每层，注意力分数矩阵大小为 (batch_size * n_heads * seq_len * seq_len)。若使用Flash Attention，则显存占用降至 O(seq_len) 级别，不再随 seq_len^2 增长。Qwen3-27B若支持Flash Attention，激活值峰值将显著低于2.5GB，N20的2.5GB估算可能基于非Flash Attention路径或包含了KV Cache。

## Evidence

先验知识/题面给定，逻辑校验通过：Flash Attention 的核心机制确实是将注意力矩阵的显存占用从 O(N^2) 降低至 O(N)，从而显著降低激活值峰值，该陈述符合技术原理。

## Search Query

Flash Attention memory reduction O(N) vs O(N^2)
