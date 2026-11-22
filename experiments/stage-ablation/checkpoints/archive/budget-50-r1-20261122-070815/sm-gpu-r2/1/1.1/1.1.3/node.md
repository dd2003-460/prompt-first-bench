# N37: 在 BF16 精度下，32K 上下文窗口的 KV Cache 总占用量为 1.07 GB，计算公式为 2 * 16 * 4 * 128 * 32768 * 2 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

在 BF16 精度下，32K 上下文窗口的 KV Cache 总占用量为 1.07 GB，计算公式为 2 * 16 * 4 * 128 * 32768 * 2 bytes。

## Corrected Claim

在 BF16 精度下，32K 上下文窗口的 KV Cache 总占用量为 1.07 GB，计算公式为 2 * 16 * 4 * 128 * 32768 * 2 bytes。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 16 * 4 * 128 * 32768 * 2 计算结果为 1,073,741,824 bytes，即 1.07 GB，数值与量纲均正确。
