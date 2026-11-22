# N212: CPU-only 方案在 32K 上下文下的 KV Cache 显存占用量计算：Size_KV = 2 * 32 * 8 * 128 * 32768 * 1 b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

CPU-only 方案在 32K 上下文下的 KV Cache 显存占用量计算：Size_KV = 2 * 32 * 8 * 128 * 32768 * 1 byte = 2,147,483,648 bytes ≈ 2.0 GB (假设 INT8 KV Cache)，该数值需与模型权重 27GB 相加，总内存需求约 29GB，因此 CPU-only 方案必须配备至少 32GB 物理内存才能运行，而 64GB 内存可提供约 35GB 用于 KV Cache 扩展或 OS 开销 [verified]

## Corrected Claim

CPU-only 方案在 32K 上下文下的 KV Cache 显存占用量计算：Size_KV = 2 * 32 * 8 * 128 * 32768 * 1 byte = 2,147,483,648 bytes ≈ 2.0 GB (假设 INT8 KV Cache)，该数值需与模型权重 27GB 相加，总内存需求约 29GB，因此 CPU-only 方案必须配备至少 32GB 物理内存才能运行，而 64GB 内存可提供约 35GB 用于 KV Cache 扩展或 OS 开销 [verified]

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2*32*8*128*32768 = 2^31 bytes = 2GB 准确，总内存 27+2=29GB 符合逻辑，32GB 内存满足需求且 64GB 提供余量的推断合理。

## Search Query

Qwen3-27B KV cache size calculation 32k context INT8
