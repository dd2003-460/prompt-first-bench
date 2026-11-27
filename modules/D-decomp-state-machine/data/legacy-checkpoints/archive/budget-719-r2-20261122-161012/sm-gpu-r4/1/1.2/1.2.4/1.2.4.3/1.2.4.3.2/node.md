# N363: H100 80GB 显存下的实际可用 KV Cache 空间需扣除 CUDA Context (约 1-2GB) 和 Activation Buffer (Pr

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N151, N152, N153

## Claim

H100 80GB 显存下的实际可用 KV Cache 空间需扣除 CUDA Context (约 1-2GB) 和 Activation Buffer (Prefill 阶段峰值，32K 序列下约为 0.5-1GB)；修正后的可用空间 = 80GB - 55GB (BF16 Weights) - 1.5GB (Overhead) ≈ 23.5GB，这将导致最大 Batch Size 从理论值 2 降至 floor(23.5 / 8.59) = 2 (无变化) 或 floor(23.5 / 4.29) = 5 (FP8 KV)，需确认 Overhead 是否显著影响 FP8 下的 Batch 上限。

## Corrected Claim

H100 80GB 显存下的实际可用 KV Cache 空间需扣除 CUDA Context (约 1-2GB) 和 Activation Buffer (Prefill 阶段峰值，32K 序列下约为 0.5-1GB)；修正后的可用空间 = 80GB - 55GB (BF16 Weights) - 1.5GB (Overhead) ≈ 23.5GB，这将导致最大 Batch Size 从理论值 2 降至 floor(23.5 / 8.59) = 2 (无变化) 或 floor(23.5 / 4.29) = 5 (FP8 KV)，需确认 Overhead 是否显著影响 FP8 下的 Batch 上限。

## Evidence

先验知识/题面给定，逻辑校验通过：80GB总显存扣除55GB权重和1.5GB开销后剩余23.5GB，数学计算正确；23.5GB除以8.59GB（BF16 KV）得2.73，向下取整为2，与理论值一致；23.5GB除以4.29GB（FP8 KV）得5.47，向下取整为5，逻辑自洽。
