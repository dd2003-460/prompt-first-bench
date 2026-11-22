# N271: 计算 2x RTX 4090 (FP8) 的 Quality_Score：基于 N81，FP8 量化导致 MMLU 下降 0-1%。设 BF16 MMLU 为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

计算 2x RTX 4090 (FP8) 的 Quality_Score：基于 N81，FP8 量化导致 MMLU 下降 0-1%。设 BF16 MMLU 为 0.75 (Qwen3-27B 典型值 [待核验])，FP8 MMLU ≈ 0.7425-0.75。归一化 Quality_Score = MMLU_FP8 / MMLU_BF16 ≈ 0.99-1.0。满足 >= 0.98 的条件。

## Corrected Claim

计算 2x RTX 4090 (FP8) 的 Quality_Score：基于 N81，FP8 量化导致 MMLU 下降 0-1%。设 BF16 MMLU 为 0.75 (Qwen3-27B 典型值 [待核验])，FP8 MMLU ≈ 0.7425-0.75。归一化 Quality_Score = MMLU_FP8 / MMLU_BF16 ≈ 0.99-1.0。满足 >= 0.98 的条件。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B MMLU score BF16 baseline
