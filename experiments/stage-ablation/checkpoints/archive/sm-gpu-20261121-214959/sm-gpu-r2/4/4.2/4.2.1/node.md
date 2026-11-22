# N90: 工作点 A1 (高性低成/前沿)：2x RTX 4090 运行 INT4 Qwen3-27B (13.5GB) + FP8 KV Cache (6.29GB) 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

工作点 A1 (高性低成/前沿)：2x RTX 4090 运行 INT4 Qwen3-27B (13.5GB) + FP8 KV Cache (6.29GB) = 19.79GB < 24GB/卡。理论 Decode 上限 ≈ 1008 GB/s / 13.5 GB ≈ 74.6 tokens/s。CapEx ≈ $3198 + $2000 配套 = $5198。

## Corrected Claim

工作点 A1 (高性低成/前沿)：2x RTX 4090 运行 INT4 Qwen3-27B (13.5GB) + FP8 KV Cache (6.29GB) = 19.79GB < 24GB/卡。理论 Decode 上限 ≈ 1008 GB/s / 13.5 GB ≈ 74.6 tokens/s。CapEx ≈ $3198 + $2000 配套 = $5198。

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 4090 显存容量（24GB/卡）及带宽（~1008GB/s）符合硬件规格，INT4 模型大小与 KV Cache 估算量级合理，计算逻辑自洽。
