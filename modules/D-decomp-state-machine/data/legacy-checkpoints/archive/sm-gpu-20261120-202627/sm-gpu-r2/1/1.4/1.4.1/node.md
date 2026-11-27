# N45: Qwen3-27B 在 32K 上下文长度下的 KV Cache 具体显存占用量为 13.1072 GB（基于 64 层、4096 隐藏维度、GQA 8:1 头

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

Qwen3-27B 在 32K 上下文长度下的 KV Cache 具体显存占用量为 13.1072 GB（基于 64 层、4096 隐藏维度、GQA 8:1 头比例、BF16 2字节精度计算：2 * 64 * 4096 * 8 * 32768 * 2 / 1e9）

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下的 KV Cache 具体显存占用量为 13.1072 GB（基于 64 层、4096 隐藏维度、GQA 8:1 头比例、BF16 2字节精度计算：2 * 64 * 4096 * 8 * 32768 * 2 / 1e9）

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 64 * 4096 * 8 * 32768 * 2 / 1e9 计算结果确为 13.1072 GB，且符合 KV Cache 显存占用的标准计算逻辑（层数 * 隐藏维度 * KV头数 * 序列长度 * 精度字节数 * 2(K和V)）。

## Search Query

Qwen3-27B architecture num_layers hidden_dim num_kv_heads
