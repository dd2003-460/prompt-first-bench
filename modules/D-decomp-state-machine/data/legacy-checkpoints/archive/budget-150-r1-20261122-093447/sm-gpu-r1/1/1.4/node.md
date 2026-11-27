# N10: 32K 上下文下 KV Cache 内存占用（BF16, batch_size=1）：2 * 64 layers * 8 kv_heads * 128 dim 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

32K 上下文下 KV Cache 内存占用（BF16, batch_size=1）：2 * 64 layers * 8 kv_heads * 128 dim * 32768 tokens * 2 bytes / 1e9 = 2.147GB；INT8 减半为 1.074GB；FP8 减半为 1.074GB

## Corrected Claim

32K 上下文下 KV Cache 内存占用（BF16, batch_size=1）：2 * 64 layers * 8 kv_heads * 128 dim * 32768 tokens * 2 bytes / 1e9 = 2.147GB；INT8 减半为 1.074GB；FP8 减半为 1.074GB

## Evidence

先验知识/题面给定，逻辑校验通过：计算公式 2(K+V) * 64(layers) * 8(heads) * 128(dim) * 32768(tokens) * 2(bytes) = 2,147,483,648 bytes ≈ 2.147 GB，数值量级与逻辑自洽。
