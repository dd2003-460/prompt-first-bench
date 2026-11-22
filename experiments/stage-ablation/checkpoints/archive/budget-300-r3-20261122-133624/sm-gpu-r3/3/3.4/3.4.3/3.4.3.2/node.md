# N281: Humanities 类题目（History, Geography）NVFP4 量化 MMLU 损失 1.0-1.5% 的机制：Humanities 题目以高频

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N89

## Claim

Humanities 类题目（History, Geography）NVFP4 量化 MMLU 损失 1.0-1.5% 的机制：Humanities 题目以高频通用词汇为主（如 'history', 'country'），token 频率 > 1e-2，量化误差较小；实测显示 Humanities 子集的平均 token 频率比 STEM 高 40%-60%，量化误差放大系数仅为 1.0-1.2。

## Corrected Claim

Humanities 类题目（History, Geography）因高频通用词汇占比高，token 频率通常高于 STEM 类，导致 NVFP4 量化下的 MMLU 损失相对较小（约 1.0-1.5%），具体频率差异和误差放大系数需视具体数据集和量化实现而定。

## Evidence

[质询]具体数值（40%-60%的频率差异、1.0-1.2的误差放大系数）缺乏公开文献直接支持，属于特定实验条件下的经验数据，可能存在过拟合或特定数据集偏差。 | 先验知识/题面给定，逻辑校验通过：高频词在量化中误差较小符合直觉，但具体量化指标（40-60%差异等）为经验事实，无外部来源直接支持，故降级。

## Search Query

NVFP4 quantization MMLU Humanities accuracy loss high frequency tokens
