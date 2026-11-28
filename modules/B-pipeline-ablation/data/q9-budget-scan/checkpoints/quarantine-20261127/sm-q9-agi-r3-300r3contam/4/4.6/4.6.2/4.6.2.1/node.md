# N200: 复杂度敏感度系数 α 的标定方法：通过收集 100 个 S_task ∈ [6,9] 的任务，记录本地模型失败率 F_local(S) 与云端模型成功率先验 F

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N69

## Claim

复杂度敏感度系数 α 的标定方法：通过收集 100 个 S_task ∈ [6,9] 的任务，记录本地模型失败率 F_local(S) 与云端模型成功率先验 F_cloud(S)，利用线性回归 F_cloud(S) - F_local(S) = α * (S - S_base) * β_cloud 拟合斜率，预期 α ∈ [0.05, 0.15]，置信区间需覆盖 95% 样本。

## Corrected Claim

复杂度敏感度系数 α 可通过收集一定数量（如100个）中等复杂度任务，记录本地与云端模型性能差异，并利用线性回归拟合斜率进行标定；具体系数范围需根据实际数据集确定，通常预期在较小范围内（如0.05-0.15）。

## Evidence

[质询]该陈述描述了一个具体的实验标定方案（包括特定的样本量100、任务复杂度范围[6,9]、线性回归公式及预期系数范围[0.05, 0.15]），这些均为经验性参数和特定研究设计，无法从第一性原理或通用逻辑中推导得出，且参考来源中未包含此具体实验细节。 | 逻辑上自洽（线性回归拟合敏感度系数是合理的统计方法），但参考来源[1][2]仅讨论LLM失败模式与复杂度的宏观关系，未提供该具体标定方法的数值支持或实验细节，属于经验事实且缺乏直接来源支持。

## Search Query

LLM complexity scaling factor high difficulty tasks cloud vs local performance gap

## Retrieval Sources

- {'url': 'https://arxiv.org/pdf/2511.12869v1&rut=0bf7051238f1296fc9534b70433226b5922d94e750a6371c81f4a2d709b8c090', 'type': 'ddg', 'title': 'On the Fundamental Limits of LLMs at Scale - arXiv.org'}
- {'url': 'https://arxiv.org/html/2503.15113v1&rut=c73f6209fe793fd392476ae2319a4492ce7b00f565d4e1c9625a964217373df7', 'type': 'ddg', 'title': 'Reasoning Effort and Problem Complexity: A Scaling Analysis in LLMs'}
