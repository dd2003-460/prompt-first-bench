# N129: 通用对话/摘要任务对量化误差的容忍度量化：当 perplexity 增加 < 2% 且 ROUGE-L 分数下降 < 1% 时，INT8 或 W4 精度在主观评

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

通用对话/摘要任务对量化误差的容忍度量化：当 perplexity 增加 < 2% 且 ROUGE-L 分数下降 < 1% 时，INT8 或 W4 精度在主观评估（LLM-as-a-Judge）中无显著差异，此时可接受最高压缩比以最大化性价比。

## Corrected Claim

在通用对话/摘要任务中，当量化导致的perplexity增加和ROUGE-L分数下降处于较小范围（如<2%和<1%）时，INT8或W4精度在主观评估中通常表现为无显著差异，此时可权衡压缩比与性能损失以最大化性价比。

## Evidence

[质询]该陈述将具体的量化阈值（perplexity < 2%, ROUGE-L < 1%）与主观评估结论（无显著差异）直接挂钩，属于经验性工程经验而非第一性原理可推导的数学或物理事实。不同模型架构、数据集分布及量化算法（如GPTQ, AWQ, SmoothQuant）对误差的敏感度不同，这些具体数值缺乏普适性，且‘无显著差异’的定义依赖于具体的评估协议和统计显著性水平，存在口径混淆风险。 | source=knowledge，逻辑自洽（量化误差与性能指标及主观体验的相关性符合直觉），但具体阈值（2%, 1%）属于经验参数，缺乏普适性证明，且无外部来源支持，依据经验事实排除条款及knowledge节点在存在可信攻击点时的降档规则，判定为degraded。
