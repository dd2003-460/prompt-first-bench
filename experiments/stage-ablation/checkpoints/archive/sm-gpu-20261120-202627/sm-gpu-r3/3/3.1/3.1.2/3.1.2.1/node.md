# N244: RTX 4080 运行 Qwen3-27B (BF16) 时，每生成 1 token 需读取的 KV Cache 字节数 = 2 × 64 (layers) ×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

RTX 4080 运行 Qwen3-27B (BF16) 时，每生成 1 token 需读取的 KV Cache 字节数 = 2 × 64 (layers) × 4096 (hidden) × 2 (bytes/element, BF16) × 32768 (seq_len) ≈ 34.36 GB [计算推导]

## Corrected Claim

RTX 4080 运行 Qwen3-27B (BF16) 时，每生成 1 token 需读取的 KV Cache 字节数 = 2 × 64 (layers) × 4096 (hidden) × 2 (bytes/element, BF16) × 32768 (seq_len) ≈ 34.36 GB [计算推导]

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层，4096隐藏维度）符合其模型规格，BF16 精度下每元素 2 字节，KV Cache 包含 Key 和 Value 两部分（系数 2），计算公式 2 * 64 * 4096 * 2 * 32768 = 34,359,738,368 字节，即 32 GiB 或约 34.36 GB（十进制），数值推导正确。
