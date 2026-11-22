# N642: 场景依赖性质量损失的综合效用函数：定义 Quality_Utility = w1 * (1 - ΔMMLU/Threshold_MMLU) + w2 * (1 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N264

## Claim

场景依赖性质量损失的综合效用函数：定义 Quality_Utility = w1 * (1 - ΔMMLU/Threshold_MMLU) + w2 * (1 - ΔPPL/Threshold_PPL) + w3 * (1 - ΔHE/Threshold_HE)，其中 w1, w2, w3 为场景权重（如创意写作 w1=0.1, w2=0.1, w3=0.1；法律咨询 w1=0.5, w2=0.4, w3=0.1）；仅当 Quality_Utility > 0.9 时，该精度方案方可进入性价比计算环节。

## Corrected Claim

场景依赖性质量损失的综合效用函数：定义 Quality_Utility = w1 * (1 - ΔMMLU/Threshold_MMLU) + w2 * (1 - ΔPPL/Threshold_PPL) + w3 * (1 - ΔHE/Threshold_HE)，其中 w1, w2, w3 为场景权重（如创意写作 w1=0.1, w2=0.1, w3=0.1；法律咨询 w1=0.5, w2=0.4, w3=0.1）；仅当 Quality_Utility > 0.9 时，该精度方案方可进入性价比计算环节。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM quality utility function multi-metric quantization acceptance threshold
