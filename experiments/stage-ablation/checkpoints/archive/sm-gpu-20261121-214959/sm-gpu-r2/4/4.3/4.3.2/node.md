# N94: 工作点 B2 (中性价比/平衡)：1x A100 80GB (HBM2e, 2039 GB/s) 运行 FP8 Qwen3-27B (27GB) + BF16 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

工作点 B2 (中性价比/平衡)：1x A100 80GB (HBM2e, 2039 GB/s) 运行 FP8 Qwen3-27B (27GB) + BF16 KV Cache (12.58GB) = 39.58GB < 80GB。理论 Decode 上限 ≈ 2039 GB/s / 27 GB ≈ 75.5 tokens/s。CapEx ≈ $15,000 (二手/现货)。

## Corrected Claim

工作点 B2 (中性价比/平衡)：1x A100 80GB (HBM2e, 2039 GB/s) 运行 FP8 Qwen3-27B (27GB) + BF16 KV Cache (12.58GB) = 39.58GB < 80GB。理论 Decode 上限 ≈ 2039 GB/s / 27 GB ≈ 75.5 tokens/s。CapEx ≈ $15,000 (二手/现货)。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e 带宽 2039 GB/s 及 FP8 模型大小 27GB 符合硬件规格与量化常识，计算 2039/27≈75.5 正确，显存占用 39.58GB < 80GB 逻辑自洽。
