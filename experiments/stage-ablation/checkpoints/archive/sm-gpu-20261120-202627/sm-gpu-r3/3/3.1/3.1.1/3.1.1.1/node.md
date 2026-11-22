# N241: RTX 4090 运行 Qwen3-27B (BF16) 时，每生成 1 token 需读取的 KV Cache 字节数 = 2 × 64 (layers) ×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

RTX 4090 运行 Qwen3-27B (BF16) 时，每生成 1 token 需读取的 KV Cache 字节数 = 2 × 64 (layers) × 4096 (hidden) × 2 (bytes/element, BF16) × 32768 (seq_len) ≈ 34.36 GB [计算推导]

## Corrected Claim

RTX 4090 运行 Qwen3-27B (BF16) 时，每生成 1 token 需读取的 KV Cache 字节数 = 2 × 64 (layers) × 4096 (hidden) × 2 (bytes/element, BF16) × 32768 (seq_len) ≈ 34.36 GB [计算推导]

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 64 * 4096 * 2 * 32768 计算结果确为 34,359,738,368 字节，即 32 GiB (约 34.36 GB)，量纲与数值推导正确。
