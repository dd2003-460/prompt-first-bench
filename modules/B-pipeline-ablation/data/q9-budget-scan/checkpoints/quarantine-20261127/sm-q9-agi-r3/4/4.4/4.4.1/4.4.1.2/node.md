# N206: Llama-3-8B (INT8) 在 V100 上 max_seq_len=8192 单并发的 KV Cache 显存计算：KV Cache 大小 = 2 (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

Llama-3-8B (INT8) 在 V100 上 max_seq_len=8192 单并发的 KV Cache 显存计算：KV Cache 大小 = 2 (K+V) * num_layers (32) * hidden_dim (4096) * seq_len (8192) * num_heads (32? No, KV heads usually less or same. Let's use standard formula: 2 * L * H_kv * S * D_head). For Llama3-8B, L=32, H_kv=8 (GQA), D_head=128. Size = 2 * 32 * 8 * 8192 * 128 * 2 bytes (FP16) = 1,073,741,824 bytes ≈ 1 GB. 剩余 8GB 足以支持 8 并发或更长序列。

## Corrected Claim

Llama-3-8B (INT8) 在 V100 上 max_seq_len=8192 单并发的 KV Cache 显存计算：KV Cache 大小 = 2 (K+V) * num_layers (32) * hidden_dim (4096) * seq_len (8192) * num_heads (32? No, KV heads usually less or same. Let's use standard formula: 2 * L * H_kv * S * D_head). For Llama3-8B, L=32, H_kv=8 (GQA), D_head=128. Size = 2 * 32 * 8 * 8192 * 128 * 2 bytes (FP16) = 1,073,741,824 bytes ≈ 1 GB. 剩余 8GB 足以支持 8 并发或更长序列。

## Evidence

先验知识/题面给定，逻辑校验通过：Llama-3-8B 架构参数（32层，GQA 8个KV头，128维头）及 FP16 精度下的 KV Cache 计算公式正确，数值推导无误（2*32*8*8192*128*2 ≈ 1GB），符合显存占用常识。
