# N298: CoT 与 ReAct 性能交叉点的实证阈值：在 Qwen3-27B 上，当 Info_Density < 0.15 bits/token 时，CoT 的 EM

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

CoT 与 ReAct 性能交叉点的实证阈值：在 Qwen3-27B 上，当 Info_Density < 0.15 bits/token 时，CoT 的 EM 比 ReAct 高 4.2% (95% CI: [3.1%, 5.3%])；当 Info_Density > 0.35 bits/token 时，ReAct 反超 CoT 6.8%；0.15-0.35 区间内两者差异不显著 (p>0.05)，构成混合策略的最佳适用区。

## Corrected Claim

在特定推理任务中，CoT与ReAct的性能表现随信息密度变化存在交叉点，低信息密度下CoT占优，高信息密度下ReAct占优，中间区间差异不显著（具体阈值需依据特定实验数据确定）。

## Evidence

[质询]该陈述包含极其具体的实证数据（特定模型Qwen3-27B、特定指标Info_Density阈值0.15/0.35、精确的性能差值4.2%/6.8%及置信区间），这属于高度特定的经验事实。参考来源[1]仅为一般性的方法论对比综述，摘要中未提及任何具体数值、阈值或针对Qwen3-27B的实证实验细节，无法提供直接支持。此外，'Info_Density'作为衡量CoT与ReAct交叉点的标准指标并非领域内公认的标准定义，存在口径混淆或虚构指标的风险。 | 逻辑上自洽（存在性能交叉点符合直觉），但参考来源[1]仅涵盖定性对比，缺乏对该具体数值阈值和统计结果的直接支持，属于经验事实且缺来源支持。

## Search Query

chain of thought vs react performance crossover threshold information density LLM

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2014389672588097470&rut=a6b793ac69518a3030f03a1cf5fcd306dd57396ffc6c0cacd3b3db664600157e', 'type': 'ddg', 'title': 'CoT/ToT/ReAct 等 Reasoning 方法对比&实践 - 知乎'}
