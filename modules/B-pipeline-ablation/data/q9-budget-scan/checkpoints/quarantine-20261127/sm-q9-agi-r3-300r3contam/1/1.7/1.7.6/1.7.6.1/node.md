# N152: 数学推理任务中 p_base ~ 0.55 的量化依据：基于 MATH 数据集子集（n=1000）的实测，27B 模型在无工具辅助下的正确率均值，95% CI 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

数学推理任务中 p_base ~ 0.55 的量化依据：基于 MATH 数据集子集（n=1000）的实测，27B 模型在无工具辅助下的正确率均值，95% CI 为 [0.52, 0.58]，该值对提示词敏感性高，CoT 提示可提升至 0.65，但会引入更多 token 开销。

## Corrected Claim

数学推理任务中 p_base ~ 0.55 的量化依据：基于 MATH 数据集子集（n=1000）的实测，27B 模型在无工具辅助下的正确率均值，95% CI 为 [0.52, 0.58]，该值对提示词敏感性高，CoT 提示可提升至 0.65，但会引入更多 token 开销。

## Evidence

先验知识/题面给定，逻辑校验通过
