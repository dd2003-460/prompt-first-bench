# N134: RTX 4090 在 FP8 精度下的质量损失量化：基于 N81，FP8 量化后 PPL 增加 2-4%，MMLU 下降 0-1%；在 32K 长上下文下，由于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

RTX 4090 在 FP8 精度下的质量损失量化：基于 N81，FP8 量化后 PPL 增加 2-4%，MMLU 下降 0-1%；在 32K 长上下文下，由于 KV Cache 精度保持 BF16/FP16 (通常 KV Cache 不量化至 FP8 以保持注意力稳定性)，质量损失主要源于权重 FP8 化，预估综合 Quality_Score ≈ 0.98-0.99 (归一化至 BF16=1.0)

## Corrected Claim

RTX 4090 在 FP8 精度下的质量损失量化：基于 N81，FP8 量化后 PPL 增加 2-4%，MMLU 下降 0-1%；在 32K 长上下文下，由于 KV Cache 精度保持 BF16/FP16 (通常 KV Cache 不量化至 FP8 以保持注意力稳定性)，质量损失主要源于权重 FP8 化，预估综合 Quality_Score ≈ 0.98-0.99 (归一化至 BF16=1.0)

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3 27B FP8 quantization quality loss benchmark
