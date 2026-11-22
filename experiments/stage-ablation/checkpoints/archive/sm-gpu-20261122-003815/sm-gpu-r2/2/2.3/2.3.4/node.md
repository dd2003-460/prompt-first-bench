# N93: Qwen3-27B 在 32K 上下文长度下的 KV Cache 总占用量（FP8）：128 KB/token × 32768 tokens = 4,194,3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Qwen3-27B 在 32K 上下文长度下的 KV Cache 总占用量（FP8）：128 KB/token × 32768 tokens = 4,194,304 KB = 4 GB（基于 N64 的计算）。

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下的 KV Cache 总占用量（FP8）：128 KB/token × 32768 tokens = 4,194,304 KB = 4 GB（基于 N64 的计算）。

## Evidence

先验知识/题面给定，逻辑校验通过：128 KB × 32768 = 4,194,304 KB = 4 GB，计算无误且量级合理。
