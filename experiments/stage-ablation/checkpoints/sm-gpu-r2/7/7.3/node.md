# N90: Normalized_Quality_Loss 计算公式：Normalized_Quality_Loss = (MMLU_Drop / MMLU_Baselin

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

Normalized_Quality_Loss 计算公式：Normalized_Quality_Loss = (MMLU_Drop / MMLU_Baseline) * Weight_MMLU + (PPL_Increase / PPL_Baseline) * Weight_PPL，其中 Weight_MMLU = 0.6, Weight_PPL = 0.4（基于任务重要性加权）

## Corrected Claim

Normalized_Quality_Loss 计算公式：Normalized_Quality_Loss = (MMLU_Drop / MMLU_Baseline) * Weight_MMLU + (PPL_Increase / PPL_Baseline) * Weight_PPL，其中 Weight_MMLU = 0.6, Weight_PPL = 0.4（基于任务重要性加权）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM quality loss normalization formula MMLU PPL weighting
