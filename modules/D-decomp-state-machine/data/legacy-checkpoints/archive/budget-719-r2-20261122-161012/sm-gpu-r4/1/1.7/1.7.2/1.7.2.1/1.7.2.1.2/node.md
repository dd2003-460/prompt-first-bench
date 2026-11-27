# N440: Qwen3-27B 每 token 的 KV Cache 增量（FP8）：KV_per_token = 2 * 64 * 8 * 128 * 1 = 131,0

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N183

## Claim

Qwen3-27B 每 token 的 KV Cache 增量（FP8）：KV_per_token = 2 * 64 * 8 * 128 * 1 = 131,072 bytes = 128 KiB。在 32K 上下文下，FP8 KV Cache 总大小为 128 KiB * 32768 = 4,096 MiB = 4 GiB？不，是 128 KiB * 32768 = 4,194,304 KiB = 4 GiB。等等，128 * 32768 = 4,194,304 KB = 4 GB? 128 KiB * 32768 = 4,194,304 KiB = 4 GiB = 4.29 GB。重新检查：131,072 bytes * 32768 = 4,294,967,296 bytes = 4 GiB = 4.29 GB。

## Corrected Claim

Qwen3-27B 每 token 的 KV Cache 增量（FP8）：KV_per_token = 2 * 64 * 8 * 128 * 1 = 131,072 bytes = 128 KiB。在 32K 上下文下，FP8 KV Cache 总大小为 128 KiB * 32768 = 4,096 MiB = 4 GiB？不，是 128 KiB * 32768 = 4,194,304 KiB = 4 GiB。等等，128 * 32768 = 4,194,304 KB = 4 GB? 128 KiB * 32768 = 4,194,304 KiB = 4 GiB = 4.29 GB。重新检查：131,072 bytes * 32768 = 4,294,967,296 bytes = 4 GiB = 4.29 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式 2 * 64 * 8 * 128 * 1 = 131,072 bytes (128 KiB) 正确；总大小 131,072 * 32,768 = 4,294,967,296 bytes = 4 GiB 计算无误。

## Search Query

Qwen3-27B kv cache per token fp8 bytes
