# N68: Batch Size 对激活值的线性影响系数：由于 Attention 和 MLP 激活值均与 batch_size 成正比，当 batch_size 从 1 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

Batch Size 对激活值的线性影响系数：由于 Attention 和 MLP 激活值均与 batch_size 成正比，当 batch_size 从 1 增加到 N 时，激活值总占用线性增加 N 倍；在 32K 上下文下，batch_size=2 时激活值峰值将从 ~5GB 翻倍至 ~10GB，可能挤占 KV Cache 空间。

## Corrected Claim

Batch Size 对激活值的线性影响系数：由于 Attention 和 MLP 激活值均与 batch_size 成正比，当 batch_size 从 1 增加到 N 时，激活值总占用线性增加 N 倍；在 32K 上下文下，batch_size=2 时激活值峰值将从 ~5GB 翻倍至 ~10GB，可能挤占 KV Cache 空间。

## Evidence

先验知识/题面给定，逻辑校验通过：Transformer中Attention和MLP层的激活值确实与batch_size线性相关，batch_size翻倍导致激活值占用翻倍符合基本原理。
