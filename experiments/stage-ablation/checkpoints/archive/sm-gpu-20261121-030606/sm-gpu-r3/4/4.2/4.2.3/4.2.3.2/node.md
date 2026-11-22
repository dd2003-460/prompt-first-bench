# N299: Flash Attention实现细节对激活值峰值的影响：标准Flash Attention v2在计算Softmax(QK^T)V时，需要临时存储分块后的Q 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N127

## Claim

Flash Attention实现细节对激活值峰值的影响：标准Flash Attention v2在计算Softmax(QK^T)V时，需要临时存储分块后的Q (seq_len_chunk * head_dim) 和累积的Output (seq_len * head_dim)。峰值显存 ≈ 2 * (batch * n_heads * seq_len * head_dim * dtype_size)。若考虑反向传播或特定优化，系数可能增至3-4。对于32K上下文，BF16下峰值约为 2 * 1 * 32 * 32768 * 128 * 2 = 1.07 GB (理论最小) 至 2.15 GB (含冗余)。

## Corrected Claim

Flash Attention实现细节对激活值峰值的影响：标准Flash Attention v2在计算Softmax(QK^T)V时，需要临时存储分块后的Q (seq_len_chunk * head_dim) 和累积的Output (seq_len * head_dim)。峰值显存 ≈ 2 * (batch * n_heads * seq_len * head_dim * dtype_size)。若考虑反向传播或特定优化，系数可能增至3-4。对于32K上下文，BF16下峰值约为 2 * 1 * 32 * 32768 * 128 * 2 = 1.07 GB (理论最小) 至 2.15 GB (含冗余)。
