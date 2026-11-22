# N184: A100 80GB SXM4 在 FP8 精度下运行 Qwen3-27B 的显存占用校验：权重 27GB + KV Cache (32K, FP8, 8.6GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

A100 80GB SXM4 在 FP8 精度下运行 Qwen3-27B 的显存占用校验：权重 27GB + KV Cache (32K, FP8, 8.6GB) + 激活/碎片 (2GB) = 37.6GB，低于 80GB 上限，可行；若使用 BF16 KV (17.2GB)，总占用 46.2GB，仍可行。

## Corrected Claim

A100 80GB SXM4 在 FP8 精度下运行 Qwen3-27B 的显存占用校验：权重 27GB + KV Cache (32K, FP8, 8.6GB) + 激活/碎片 (2GB) = 37.6GB，低于 80GB 上限，可行；若使用 BF16 KV (17.2GB)，总占用 46.2GB，仍可行。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 参数量约 27B，FP8 权重约 27GB；KV Cache 计算符合公式（2 * 层数 * 头数 * 头维 * 序列长度 * 字节数），32K 序列下 FP8 约 8.6GB，BF16 约 17.2GB，总显存占用远低于 80GB 上限，数值量级合理且自洽。
