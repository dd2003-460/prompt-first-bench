# N43: 在 FP8/INT8 精度下，Qwen3-27B 32K 上下文长度的 KV Cache 总显存占用计算结果为 2 * 64 * 8 * 128 * 32768

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

在 FP8/INT8 精度下，Qwen3-27B 32K 上下文长度的 KV Cache 总显存占用计算结果为 2 * 64 * 8 * 128 * 32768 * 1 byte = 4.29 GB [待核验：基于 N39/N40/N41 参数计算]

## Corrected Claim

在 FP8/INT8 精度下，Qwen3-27B 32K 上下文长度的 KV Cache 总显存占用计算结果为 2 * 64 * 8 * 128 * 32768 * 1 byte = 4.29 GB [待核验：基于 N39/N40/N41 参数计算]

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2 * 64 * 8 * 128 * 32768 * 1 的数值结果为 4,294,967,296 Bytes，即 4.29 GB，量纲与数值均正确。
