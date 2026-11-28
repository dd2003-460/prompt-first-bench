# N304: 在科研假设生成任务中，CoT 模板的边际收益拐点出现在 Prompt 长度超过 2000 tokens 时：此时由于 'Lost in the Middle' 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

在科研假设生成任务中，CoT 模板的边际收益拐点出现在 Prompt 长度超过 2000 tokens 时：此时由于 'Lost in the Middle' 效应 (N94)，CoT 带来的逻辑清晰度增益 (< 2%) 不足以抵消长上下文导致的注意力稀释和推理延迟增加 (> 15%)，建议对此类长 Prompt 改用分段摘要 + 短 CoT 策略。

## Corrected Claim

在科研假设生成任务中，随着Prompt长度增加，CoT模板的边际收益可能因长上下文处理效率下降（如‘Lost in the Middle’效应）而降低，建议在超长Prompt场景下评估分段摘要+短CoT策略的有效性，具体拐点需根据实际模型与任务基准测试确定。

## Evidence

[质询]该陈述包含具体的经验性阈值（2000 tokens）和精确的性能变化数值（<2%增益, >15%延迟），这些并非第一性原理可推导的数学或物理事实，而是依赖于特定模型架构、任务分布及评估基准的经验数据。现有参考来源仅介绍CoT概念，未提供此类量化拐点数据，且‘Lost in the Middle’效应通常指中间信息遗忘，将其直接量化为‘注意力稀释导致推理延迟增加>15%’缺乏通用理论支撑，属于过度具体的经验断言。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2]仅涉及CoT基础概念，未覆盖具体token阈值及量化性能指标）

## Search Query

long context lost in the middle effect chain of thought performance drop threshold

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/809100987&rut=cb6146d7011671feef6418219801618484ebc439a84340d9e0ba63875e681d96', 'type': 'ddg', 'title': '全自动思维链COT一秒优化Prompt提升AI能力，COT详解 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/659102403&rut=e8282a31f1dfc135b093da782880948026b701c6acd44305baacbbd74a34e3e3', 'type': 'ddg', 'title': 'ChatGPT|Prompt中的CoT和ReAct - 知乎'}
