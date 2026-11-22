# N24: 可接受的精度下限定义：对于通用对话任务，困惑度增加<10%且人类评估（human eval）胜率>90%（vs BF16）为可接受；对于代码生成或数学推理任务，

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

可接受的精度下限定义：对于通用对话任务，困惑度增加<10%且人类评估（human eval）胜率>90%（vs BF16）为可接受；对于代码生成或数学推理任务，阈值收紧至困惑度增加<5%且胜率>95%

## Corrected Claim

对于通用对话任务，通常认为困惑度小幅增加（如<10%）且人类评估胜率较高（如>90%）为可接受；对于代码生成或数学推理任务，由于对精确性要求更高，阈值通常需收紧（如困惑度增加<5%且胜率>95%）。具体阈值需根据实际业务场景和评估基准确定。

## Evidence

[质询]该陈述包含具体的经验性阈值（如困惑度增加<10%、胜率>90%等），这些数值并非由第一性原理或数学公理严格推导得出，而是依赖于特定实验设置、数据集和评估协议的经验总结。参考来源仅讨论了困惑度与下游任务的关系及评估指标，并未提供这些具体的量化阈值标准，因此存在将特定实验结果泛化为通用标准的可能性，且缺乏直接来源支持。 | 逻辑自洽（代码/数学任务通常要求更高精度，阈值收紧符合直觉），但参考来源[1][2][3]仅涉及困惑度分析原理及指标介绍，未提供具体的可接受精度下限数值（如<10% PPL, >90% win rate），属于经验事实且缺来源直接支持。

## Search Query

LLM quantization quality threshold perplexity human eval win rate acceptable degradation

## Retrieval Sources

- {'url': 'https://cloud.tencent.com/developer/article/2589118&rut=18dec1677cfa89e285439782fbe0bf8b1ea490db09bfa7fe599dbe3dc1675d86', 'type': 'ddg', 'title': '121_训练评估：困惑度分析 - 分析指标与下游任务关系'}
- {'url': 'https://developer.cloud.tencent.com/article/2589118&rut=8be753cdf62b0132306a434a5f472040ee9b01fbf514e5ad94b7e62495d070c4', 'type': 'ddg', 'title': '121_训练评估：困惑度分析 - 分析指标与下游任务关系-腾讯云开发者社区-腾讯云'}
- {'url': 'https://zsc.github.io/llm_train_tutorial/html/chapter10.html&rut=0ac229eeacaa1005143e5fdff124be4529eecb15dfcbbc586c8d4235d708b6c2', 'type': 'ddg', 'title': 'chapter10.md — 评估：验证困惑度'}
