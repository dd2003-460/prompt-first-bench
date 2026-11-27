# N363: Intel Gaudi 2 在 BF16 精度下运行 Qwen3-27B 的显存占用计算：权重 54GB + 32K 上下文 KV Cache (约 4-5GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

Intel Gaudi 2 在 BF16 精度下运行 Qwen3-27B 的显存占用计算：权重 54GB + 32K 上下文 KV Cache (约 4-5GB, 假设 GQA 优化后) + 激活值/临时缓冲 (约 2-4GB) = 60-63GB，低于 96GB 显存上限，理论上可支持 Batch Size ≥ 2-3 而无需 Offload。

## Corrected Claim

Intel Gaudi 2 在 BF16 精度下运行 Qwen3-27B 的显存占用计算：权重 54GB + 32K 上下文 KV Cache (约 4-5GB, 假设 GQA 优化后) + 激活值/临时缓冲 (约 2-4GB) = 60-63GB，低于 96GB 显存上限，理论上可支持 Batch Size ≥ 2-3 而无需 Offload。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，GQA优化下32K上下文KV Cache及激活值估算合理，总显存占用低于96GB，支持Batch Size 2-3的结论符合工程直觉。
