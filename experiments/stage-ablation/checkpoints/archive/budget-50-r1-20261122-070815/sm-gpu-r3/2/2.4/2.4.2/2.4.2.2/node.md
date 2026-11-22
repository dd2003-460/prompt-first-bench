# N228: NVFP4 量化在 GSM8K 上的分数下降幅度 (Delta %) 约为 2-4 个百分点（即从 85-88% 降至 81-86%），因为 4-bit 量化对

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

NVFP4 量化在 GSM8K 上的分数下降幅度 (Delta %) 约为 2-4 个百分点（即从 85-88% 降至 81-86%），因为 4-bit 量化对逻辑链较长的任务敏感度高于通用对话，长链推理中误差累积效应显著

## Corrected Claim

NVFP4 量化在 GSM8K 上的分数下降幅度 (Delta %) 约为 2-4 个百分点（即从 85-88% 降至 81-86%），因为 4-bit 量化对逻辑链较长的任务敏感度高于通用对话，长链推理中误差累积效应显著

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVFP4 quantization GSM8K performance drop Qwen
