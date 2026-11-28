# N308: 在'不改权重'约束下，通过ReAct框架集成外部Python沙箱执行环境，可使27B模型在数值计算类科研子任务上的Pass@1成功率从纯LLM生成的15-20%

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在'不改权重'约束下，通过ReAct框架集成外部Python沙箱执行环境，可使27B模型在数值计算类科研子任务上的Pass@1成功率从纯LLM生成的15-20%提升至75-85%，因为LLM仅负责代码生成而非心算，消除了算术幻觉这一主要失败源。

## Corrected Claim

在'不改权重'约束下，通过ReAct框架集成外部Python沙箱执行环境，通常能显著提升27B模型在数值计算类科研子任务上的Pass@1成功率，因为LLM仅负责代码生成而非心算，消除了算术幻觉这一主要失败源。

## Evidence

[质询]具体的数值提升幅度（15-20%至75-85%）及特定模型规模（27B）属于经验事实，缺乏通用基准数据支持，不同数据集和任务定义下波动极大，存在以偏概全风险。 | 来源[1]仅介绍ReAct原理，未提供具体性能数据；该陈述为经验事实，逻辑自洽但缺来源直接支持具体数值。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1991816580384957616&rut=5a0969352f8a34fa111f5a96c88b7c898e6da2c4b42d50b28a53eceee98c112c', 'type': 'ddg', 'title': '拥抱大模型：深入剖析ReAct的核心原理、技术架构 - 知乎'}
