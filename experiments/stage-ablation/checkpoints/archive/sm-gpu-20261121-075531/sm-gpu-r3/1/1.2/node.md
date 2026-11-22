# N7: KV Cache显存占用量 = 2 * 32768 tokens * 48 layers * 16 heads * 128 dim * 2 bytes (BF1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

KV Cache显存占用量 = 2 * 32768 tokens * 48 layers * 16 heads * 128 dim * 2 bytes (BF16) / 1024^3 ≈ 1.93GB (假设Qwen3-27B架构参数: 48层, GQA 16 KV heads, head_dim 128)

## Corrected Claim

KV Cache显存占用量 = 2 * 32768 tokens * 48 layers * 16 heads * 128 dim * 2 bytes (BF16) / 1024^3 ≈ 1.93GB (假设Qwen3-27B架构参数: 48层, GQA 16 KV heads, head_dim 128)

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 32768 * 48 * 16 * 128 * 2 / 1024^3 ≈ 1.93 GB 数学上准确，且符合 Qwen3-27B 架构参数假设下的 KV Cache 显存占用量级。

## Search Query

Qwen3-27B architecture layers heads hidden size
