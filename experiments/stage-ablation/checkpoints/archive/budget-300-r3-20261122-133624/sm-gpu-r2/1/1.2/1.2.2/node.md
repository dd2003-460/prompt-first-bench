# N48: N7 中的 4.09GB 假设了 Batch Size = 64 (64 * 64MB = 4096MB)。若 Batch Size 为 1，KV Cache 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

N7 中的 4.09GB 假设了 Batch Size = 64 (64 * 64MB = 4096MB)。若 Batch Size 为 1，KV Cache 仅需 64MB；若 Batch Size 为 128，则需 8.19GB。因此 KV Cache 显存是动态变量，取决于最大并发序列数 (max_num_seqs)。

## Corrected Claim

N7 中的 4.09GB 假设了 Batch Size = 64 (64 * 64MB = 4096MB)。若 Batch Size 为 1，KV Cache 仅需 64MB；若 Batch Size 为 128，则需 8.19GB。因此 KV Cache 显存是动态变量，取决于最大并发序列数 (max_num_seqs)。

## Evidence

先验知识/题面给定，逻辑校验通过：4.09GB 约等于 4096MB，且 64 * 64MB = 4096MB，1 * 64MB = 64MB，128 * 64MB = 8192MB (8.19GB)，数值计算与线性关系逻辑自洽。
