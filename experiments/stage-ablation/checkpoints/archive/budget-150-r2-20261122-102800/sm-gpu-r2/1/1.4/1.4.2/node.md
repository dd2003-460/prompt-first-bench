# N65: 2×RTX 4090 (PCIe 4.0 x16) 在 Tensor Parallel 下的 AllReduce 通信量：每生成 1 token，需交换 KV 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

2×RTX 4090 (PCIe 4.0 x16) 在 Tensor Parallel 下的 AllReduce 通信量：每生成 1 token，需交换 KV Cache 中间结果，通信量 ≈ 2 * seq_len * num_kv_heads * head_dim * bytes_per_elem = 2 * 32768 * 8 * 128 * 1 byte (INT8) = 67.1 MB/token。

## Corrected Claim

2×RTX 4090 (PCIe 4.0 x16) 在 Tensor Parallel 下的 AllReduce 通信量：每生成 1 token，需交换 KV Cache 中间结果，通信量 ≈ 2 * seq_len * num_kv_heads * head_dim * bytes_per_elem = 2 * 32768 * 8 * 128 * 1 byte (INT8) = 67.1 MB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 32768 * 8 * 128 * 1 计算结果确为 67,108,864 Bytes (67.1 MB)，量纲与数值自洽。
