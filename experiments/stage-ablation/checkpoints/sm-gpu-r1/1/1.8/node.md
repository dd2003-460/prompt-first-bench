# N14: 质量损失可接受阈值的量化定义：基于任务类型（代码生成/数学推理/通用对话）设定的最低得分底线（如 MMLU ≥ 70% 或 GSM8K ≥ 80%），以及低于该

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

质量损失可接受阈值的量化定义：基于任务类型（代码生成/数学推理/通用对话）设定的最低得分底线（如 MMLU ≥ 70% 或 GSM8K ≥ 80%），以及低于该阈值时的业务不可行判定标准

## Corrected Claim

质量损失可接受阈值需基于任务类型（代码生成/数学推理/通用对话）及具体业务场景设定最低得分底线（如MMLU或GSM8K的特定百分比），低于该阈值时判定为业务不可行；具体数值需根据实际业务需求确定，而非固定为MMLU ≥ 70%或GSM8K ≥ 80%。

## Evidence

[质询]陈述中给出的具体数值阈值（MMLU ≥ 70% 或 GSM8K ≥ 80%）属于经验性业务标准，并非行业通用的固定物理常数或数学公理，不同业务场景下阈值差异巨大，且参考来源中未提供这些具体数值的支持。 | 来源[1]和[2]讨论了量化模型精度评估和质量评估的方法论，支持了‘需要设定阈值以验证业务要求’的逻辑框架，但未提供具体的MMLU/GSM8K数值阈值，属于间接支持；具体数值为经验事实，缺乏直接来源支持。

## Search Query

LLM quantization acceptable accuracy threshold MMLU GSM8K minimum score

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1995649267013018246&rut=a0423e0cd622d7b30623728afcdae1c96e141b82ee7a58f9f1e2f57eec60e955', 'type': 'ddg', 'title': '如何科学评估量化模型的精度 - 知乎'}
- {'url': 'https://developer.baidu.com/article/detail.html?id=5554944&rut=2d9874f5ab794d199f279bc58b63bc93df6168d087594e01cd73c5a1944cc9a1', 'type': 'ddg', 'title': '大模型生成质量评估指南：6大核心计算方法解析-百度开发者中心'}
