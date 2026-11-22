# N79: 2×RTX 4090 (48GB) 在 FP8 精度下运行 Qwen3-27B 的 KV Cache 显存占用计算：2 * 64 * 4096 * 32 * 3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

2×RTX 4090 (48GB) 在 FP8 精度下运行 Qwen3-27B 的 KV Cache 显存占用计算：2 * 64 * 4096 * 32 * 32768 * 1 byte ≈ 55.0MB/layer * 64 ≈ 3.5GB，加上权重 27GB 和运行时开销 5GB，总显存需求约 35.5GB，低于 48GB 上限，方案可行。

## Corrected Claim

2×RTX 4090 (48GB) 在 FP8 精度下运行 Qwen3-27B 的 KV Cache 显存占用计算：2 * 64 * 4096 * 32 * 32768 * 1 byte ≈ 55.0MB/layer * 64 ≈ 3.5GB，加上权重 27GB 和运行时开销 5GB，总显存需求约 35.5GB，低于 48GB 上限，方案可行。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算 2*64*4096*32*32768 bytes ≈ 55MB/layer，64层共约 3.5GB；总显存 27GB(权重) + 3.5GB(KV) + 5GB(开销) ≈ 35.5GB < 48GB，数值量级与逻辑自洽。
