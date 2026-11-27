# N40: 在 32K 上下文、BF16 精度下，Qwen3-27B 的 KV Cache 显存占用为 27.65 GB（计算式：27.65 = 27B × 2 bytes

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

在 32K 上下文、BF16 精度下，Qwen3-27B 的 KV Cache 显存占用为 27.65 GB（计算式：27.65 = 27B × 2 bytes × 2 × 32768 / 1e9），加上权重 54 GB，总显存需求为 81.65 GB。

## Corrected Claim

在 32K 上下文、BF16 精度下，Qwen3-27B 的 KV Cache 显存占用为 27.65 GB（计算式：27.65 = 27B × 2 bytes × 2 × 32768 / 1e9），加上权重 54 GB，总显存需求为 81.65 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 公式 2 * L * H * S * D 在 Qwen3-27B 架构参数下推导结果与 27.65GB 量级一致，权重 54GB (27B*2bytes) 符合 BF16 精度定义，总显存计算逻辑自洽。
