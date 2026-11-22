# N128: 单卡 vs 多卡对比方案1（2x RTX 4090 vs 1x A100 80GB）：2x RTX 4090总显存48GB，不足以运行BF16 Qwen3-27

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25, N26, N27

## Claim

单卡 vs 多卡对比方案1（2x RTX 4090 vs 1x A100 80GB）：2x RTX 4090总显存48GB，不足以运行BF16 Qwen3-27B (54GB)，因此该对比仅在FP8/INT8/W4精度下有效。若强制BF16，2x4090不可行，需3x4090 (72GB)或2x5090 (64GB，仍不足BF16 72.8GB需求，需量化KV)。

## Corrected Claim

单卡 vs 多卡对比方案1（2x RTX 4090 vs 1x A100 80GB）：2x RTX 4090总显存48GB，不足以运行BF16 Qwen3-27B (54GB)，因此该对比仅在FP8/INT8/W4精度下有效。若强制BF16，2x4090不可行，需3x4090 (72GB)或2x5090 (64GB，仍不足BF16 72.8GB需求，需量化KV)。

## Evidence

先验知识/题面给定，逻辑校验通过：2x4090(48GB) < 54GB(BF16 Qwen3-27B) 且 2x5090(64GB) < 72.8GB(BF16需求)，数值量级与显存计算逻辑自洽。

## Search Query

Qwen3-27B BF16 memory requirement 72GB vs 48GB dual GPU feasibility
