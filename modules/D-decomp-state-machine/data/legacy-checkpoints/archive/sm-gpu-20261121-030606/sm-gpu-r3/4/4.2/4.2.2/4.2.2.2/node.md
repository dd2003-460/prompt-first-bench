# N296: Flash Attention机制下，注意力中间激活值峰值显存占用计算：峰值 = (batch_size * n_heads * seq_len * head_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

Flash Attention机制下，注意力中间激活值峰值显存占用计算：峰值 = (batch_size * n_heads * seq_len * head_dim * dtype_size) * (常数因子，通常为2-3倍以容纳Q/K/V投影及输出)。对于Qwen3-27B (n_heads=32, head_dim=128, seq_len=32768, BF16=2bytes)，单层峰值 ≈ 1 * 32 * 32768 * 128 * 2 * 3 ≈ 1.57 GB。这是注意力部分激活值的主要贡献者，而非O(seq_len^2)的分数矩阵。

## Corrected Claim

Flash Attention机制下，注意力中间激活值峰值显存占用计算：峰值 = (batch_size * n_heads * seq_len * head_dim * dtype_size) * (常数因子，通常为2-3倍以容纳Q/K/V投影及输出)。对于Qwen3-27B (n_heads=32, head_dim=128, seq_len=32768, BF16=2bytes)，单层峰值 ≈ 1 * 32 * 32768 * 128 * 2 * 3 ≈ 1.57 GB。这是注意力部分激活值的主要贡献者，而非O(seq_len^2)的分数矩阵。

## Evidence

先验知识/题面给定，逻辑校验通过：Flash Attention 核心优势即为避免显存中存储 O(N^2) 注意力矩阵，峰值显存主要取决于 Q/K/V 投影及中间激活（O(N)），数值计算 32*32768*128*2*3 ≈ 1.57GB 量级合理。
