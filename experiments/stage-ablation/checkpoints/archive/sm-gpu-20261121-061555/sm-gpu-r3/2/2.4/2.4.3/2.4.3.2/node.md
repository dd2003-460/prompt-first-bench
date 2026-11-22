# N205: Qwen3-27B 在 NVFP4 量化下，若 KV Cache 保持 FP16 精度，32K 上下文单请求的 KV Cache 占用为 0.43 GB，计算公

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

Qwen3-27B 在 NVFP4 量化下，若 KV Cache 保持 FP16 精度，32K 上下文单请求的 KV Cache 占用为 0.43 GB，计算公式为：2 * L(32) * num_kv_heads(8) * head_dim(128) * seq_len(32768) * 2 bytes / 1e9 ≈ 0.43 GB。

## Corrected Claim

Qwen3-27B 在 NVFP4 量化下，若 KV Cache 保持 FP16 精度，32K 上下文单请求的 KV Cache 占用为 0.43 GB，计算公式为：2 * L(32) * num_kv_heads(8) * head_dim(128) * seq_len(32768) * 2 bytes / 1e9 ≈ 0.43 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 32 * 8 * 128 * 32768 * 2 / 1e9 = 0.4294976 GB ≈ 0.43 GB，计算无误且量级合理。
