# N176: FP8 量化后的权重显存占用精确值：27 * 10^9 parameters * 1 byte/param = 27.0 GB。加上 N124 计算的 Per-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

FP8 量化后的权重显存占用精确值：27 * 10^9 parameters * 1 byte/param = 27.0 GB。加上 N124 计算的 Per-Channel Scale 开销 (~26 MB) 和 Bias (通常 FP16, ~50 MB)，总占用为 27.08 GB。N51 中的 27.5-28.0 GB 高估了 Scale 开销，实际应接近 27.1 GB。

## Corrected Claim

FP8 量化后的权重显存占用精确值：27 * 10^9 parameters * 1 byte/param = 27.0 GB。加上 N124 计算的 Per-Channel Scale 开销 (~26 MB) 和 Bias (通常 FP16, ~50 MB)，总占用为 27.08 GB。N51 中的 27.5-28.0 GB 高估了 Scale 开销，实际应接近 27.1 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数FP8量化基础占用27GB，加上Scale和Bias开销后总占用约27.1GB，数值量级与计算逻辑自洽。
