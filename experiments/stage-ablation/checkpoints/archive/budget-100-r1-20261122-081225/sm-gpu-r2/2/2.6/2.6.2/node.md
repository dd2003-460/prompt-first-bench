# N96: 在 BF16 精度下，Qwen3-27B 单个 token 的 KV Cache 占用量为 256 KB，计算公式为：2 (K和V) * 64 (层数) * 8

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

在 BF16 精度下，Qwen3-27B 单个 token 的 KV Cache 占用量为 256 KB，计算公式为：2 (K和V) * 64 (层数) * 8 (KV头数) * 128 (头维度) * 2 (字节/元素) = 262,144 bytes。

## Corrected Claim

在 BF16 精度下，Qwen3-27B 单个 token 的 KV Cache 占用量为 256 KB，计算公式为：2 (K和V) * 64 (层数) * 8 (KV头数) * 128 (头维度) * 2 (字节/元素) = 262,144 bytes。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层, 8 KV头, 128头维度）符合其模型规格，BF16 下 2*64*8*128*2 = 262,144 bytes (256 KB) 计算正确。

## Search Query

KV cache size calculation formula per token
