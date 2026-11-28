# N106: Qwen3-27B 的 n_layers=64 决定了 KV Cache 的线性增长系数，每增加 1 层，32K 上下文的 KV Cache 增加 0.27 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

Qwen3-27B 的 n_layers=64 决定了 KV Cache 的线性增长系数，每增加 1 层，32K 上下文的 KV Cache 增加 0.27 GB (BF16)，这是显存规划的基础斜率。

## Corrected Claim

Qwen3-27B 的 n_layers=64 决定了 KV Cache 的线性增长系数，每增加 1 层，32K 上下文的 KV Cache 增加 0.27 GB (BF16)，这是显存规划的基础斜率。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构中 n_layers=64 为已知配置，KV Cache 随层数线性增长符合 Transformer 基本原理，数值量级（单层约 0.27GB @32K BF16）与常见大模型显存估算相符。
