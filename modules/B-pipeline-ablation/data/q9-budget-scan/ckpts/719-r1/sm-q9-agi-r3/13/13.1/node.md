# N328: mypy --strict 静态类型检查在 Qwen3.8-27B 生成的 Pandas 科研代码上的前置拦截率（Preemptive Interception

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104, N105, N106

## Claim

mypy --strict 静态类型检查在 Qwen3.8-27B 生成的 Pandas 科研代码上的前置拦截率（Preemptive Interception Rate）为 65%-80%（针对变量名不一致与类型错误），拦截耗时 < 200ms/文件，使得 First-Pass Execution Success Rate 从基线 45% 提升至 75%-85%。

## Corrected Claim

mypy --strict 静态类型检查可用于拦截 Qwen3.8-27B 生成的 Pandas 科研代码中的变量名不一致与类型错误，从而提升首次执行成功率（具体拦截率与耗时需参考特定实验报告，当前来源未提供确切数值）。

## Evidence

[质询]该陈述包含具体的量化指标（拦截率65%-80%、耗时<200ms、成功率提升45%->75%-85%）以及特定模型（Qwen3.8-27B）的实验数据，属于经验事实。参考来源均为通用的mypy使用教程或官方文档，完全未涉及任何LLM生成代码的评估实验、特定模型版本或上述具体统计数据，因此缺乏直接来源支持。 | 逻辑上静态类型检查确实能拦截部分错误并提升执行成功率，量级在理论上合理；但所有参考来源（[1][2][3]）仅介绍mypy通用用法，与该特定实验场景（Qwen3.8-27B生成的Pandas代码）无关，无法提供数值支持，故依据经验事实排除条款降级。

## Search Query

mypy static analysis python code generation success rate LLM improvement

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00446/article/details/150864176&rut=ae49a4f4b542f0fd3f263f4eeafbb4d5a34b389f4e5c1d1901b4dbb1d87966fc', 'type': 'ddg', 'title': '3步快速上手MyPy：Python静态类型检查的终极指南 - CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00978/article/details/151234357&rut=91826053cffe0c836ce273d004f636b9defd08ff7111570284799598d4d87c75', 'type': 'ddg', 'title': 'Python开发者必备：mypy静态类型检查实战指南 - CSDN博客'}
- {'url': 'https://mypy-lang.org/&rut=310aa55e040c4cce61af4ce3285a9a6459fc0a47e8d817b0a8f0c0ee904a1561', 'type': 'ddg', 'title': 'mypy - Optional Static Typing for Python'}
