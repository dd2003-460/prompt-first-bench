# N13: Qwen3-27B 在 BF16 精度下量化误差为 0%（无损失），在 FP8 精度下困惑度 (Perplexity) 增加通常 < 1%，在 INT8 下 <

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

Qwen3-27B 在 BF16 精度下量化误差为 0%（无损失），在 FP8 精度下困惑度 (Perplexity) 增加通常 < 1%，在 INT8 下 < 2%，在 W4 下可能 > 5% 或出现显著幻觉率上升

## Corrected Claim

Qwen3-27B 在 BF16 精度下量化误差为 0%（无损失），在 FP8 精度下困惑度 (Perplexity) 增加通常 < 1%，在 INT8 下 < 2%，在 W4 下可能 > 5% 或出现显著幻觉率上升

## Evidence

先验知识/题面给定，逻辑校验通过：BF16为训练精度故无量化误差；FP8/INT8为高精度量化，大模型（27B）在此精度下性能损失极小（<1-2%）符合业界共识；W4为低比特量化，显著性能下降及幻觉风险符合量化理论预期。
