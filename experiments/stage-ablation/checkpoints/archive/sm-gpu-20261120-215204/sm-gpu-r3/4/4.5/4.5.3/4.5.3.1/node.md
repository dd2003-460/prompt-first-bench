# N309: 工作点A（高性低成）：A100 80GB + FP8精度，理论峰值 = 2039 GB/s / 27 GB ≈ 75.5 Tokens/s；FP8精度下反量化开

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

工作点A（高性低成）：A100 80GB + FP8精度，理论峰值 = 2039 GB/s / 27 GB ≈ 75.5 Tokens/s；FP8精度下反量化开销较低，实际有效吞吐估算为 60-70 Tokens/s，显存占用约47GB，远低于80GB上限。

## Corrected Claim

工作点A（高性低成）：A100 80GB + FP8精度，理论峰值 = 2039 GB/s / 27 GB ≈ 75.5 Tokens/s；FP8精度下反量化开销较低，实际有效吞吐估算为 60-70 Tokens/s，显存占用约47GB，远低于80GB上限。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e 带宽约 2039 GB/s，27GB 模型在 FP8 下理论吞吐 2039/27 ≈ 75.5 Tokens/s 计算正确；考虑反量化及系统开销后 60-70 Tokens/s 估算合理；47GB 显存占用（含 KV Cache 等）低于 80GB 上限，逻辑自洽。
