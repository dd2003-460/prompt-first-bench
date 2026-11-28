# N33: Qwen3-27B 架构参数：层数 L=64, 隐藏维度 d=4096, KV头数 n_kv=8, 头维度 d_head=128 (GQA架构), 用于计算单t

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Qwen3-27B 架构参数：层数 L=64, 隐藏维度 d=4096, KV头数 n_kv=8, 头维度 d_head=128 (GQA架构), 用于计算单token KV cache大小的基础常数。

## Corrected Claim

Qwen3-27B 架构参数：层数 L=64, 隐藏维度 d=4096, KV头数 n_kv=8, 头维度 d_head=128 (GQA架构), 用于计算单token KV cache大小的基础常数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B architecture parameters layers hidden size kv heads head dim
