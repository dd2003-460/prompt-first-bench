# N226: 2x RTX 4090 BF16 不可行边界：总显存 48GB < 55GB 需求，缺口 7GB，导致 BF16 精度下无法加载完整模型，此配置在 BF16 口

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

2x RTX 4090 BF16 不可行边界：总显存 48GB < 55GB 需求，缺口 7GB，导致 BF16 精度下无法加载完整模型，此配置在 BF16 口径下被排除，必须降级至 FP8 或启用 CPU Offload (导致延迟激增 >50ms/token)。

## Corrected Claim

2x RTX 4090 BF16 不可行边界：总显存 48GB < 55GB 需求，缺口 7GB，导致 BF16 精度下无法加载完整模型，此配置在 BF16 口径下被排除，必须降级至 FP8 或启用 CPU Offload (导致延迟激增 >50ms/token)。

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 4090 显存为 48GB，小于 55GB 需求，缺口 7GB，BF16 下无法加载完整模型，需降级至 FP8 或启用 CPU Offload（延迟激增 >50ms/token），数值与逻辑自洽。
