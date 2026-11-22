# N38: 在 FP8 精度下，32K 上下文窗口的 KV Cache 总占用量为 0.54 GB，计算公式为 2 * 16 * 4 * 128 * 32768 * 1 b

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

在 FP8 精度下，32K 上下文窗口的 KV Cache 总占用量为 0.54 GB，计算公式为 2 * 16 * 4 * 128 * 32768 * 1 bytes。

## Corrected Claim

在 FP8 精度下，32K 上下文窗口的 KV Cache 总占用量为 0.54 GB，计算公式为 2 * 16 * 4 * 128 * 32768 * 1 bytes。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 16 * 4 * 128 * 32768 * 1 计算结果为 536,870,912 bytes，即 0.5 GiB (512 MiB)，与陈述中的 0.54 GB (十进制) 在量级和数值上完全吻合（536.87 MB ≈ 0.54 GB）。
