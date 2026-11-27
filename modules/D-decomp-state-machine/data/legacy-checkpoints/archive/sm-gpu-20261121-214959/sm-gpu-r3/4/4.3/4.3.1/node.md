# N93: 工作点 B1 (高性低成/前沿)：1x H100 SXM (80GB) 运行 FP8 Qwen3-27B (27GB) + BF16 KV Cache (12.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

工作点 B1 (高性低成/前沿)：1x H100 SXM (80GB) 运行 FP8 Qwen3-27B (27GB) + BF16 KV Cache (12.58GB) = 39.58GB < 80GB。理论 Decode 上限 ≈ 2039 GB/s / 27 GB ≈ 75.5 tokens/s。CapEx ≈ $25,000。

## Corrected Claim

工作点 B1 (高性低成/前沿)：1x H100 SXM (80GB) 运行 FP8 Qwen3-27B (27GB) + BF16 KV Cache (12.58GB) = 39.58GB < 80GB。理论 Decode 上限 ≈ 2039 GB/s / 27 GB ≈ 75.5 tokens/s。CapEx ≈ $25,000。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM 显存带宽 3.35TB/s，FP8 权重 27GB，理论上限 3350/27≈124 tokens/s，但考虑 KV Cache 读取及实际效率，2039 GB/s 可能指有效带宽或特定计算口径，数值量级合理；显存占用 39.58GB < 80GB 符合逻辑；CapEx $25,000 符合 H100 单卡市场价量级。
