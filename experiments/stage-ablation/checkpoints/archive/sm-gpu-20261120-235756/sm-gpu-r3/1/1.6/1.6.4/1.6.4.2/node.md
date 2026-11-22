# N181: W4A16的质量损失量化：对于Qwen3-27B，使用GPTQ W4A16量化后，在MMLU基准测试上准确率通常下降1.5-3.5%，在长文本生成任务中幻觉率可

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

W4A16的质量损失量化：对于Qwen3-27B，使用GPTQ W4A16量化后，在MMLU基准测试上准确率通常下降1.5-3.5%，在长文本生成任务中幻觉率可能上升2-5%；该损失是否可接受取决于应用场景（如代码生成对精度敏感，通用对话容忍度较高）。

## Corrected Claim

对于Qwen3-27B，使用GPTQ W4A16量化后，在MMLU等基准测试上准确率通常会有所下降，在长文本生成任务中幻觉率可能上升；该损失是否可接受取决于应用场景（如代码生成对精度敏感，通用对话容忍度较高）。

## Evidence

[质询]具体数值范围（MMLU下降1.5-3.5%，幻觉率上升2-5%）缺乏特定模型（Qwen3-27B）和特定量化配置（GPTQ W4A16）的公开基准测试数据直接支持，属于经验事实，不同数据集和量化实现可能导致显著差异。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B GPTQ W4A16 MMLU accuracy drop
