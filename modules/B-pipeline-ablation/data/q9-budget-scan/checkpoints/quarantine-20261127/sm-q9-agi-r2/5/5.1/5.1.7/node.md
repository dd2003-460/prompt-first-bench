# N70: 准确率提升量化：ΔAccuracy = Accuracy_with_XVal - Accuracy_without_XVal，需基于 N=100 样本的对照实验

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24, N25, N26

## Claim

准确率提升量化：ΔAccuracy = Accuracy_with_XVal - Accuracy_without_XVal，需基于 N=100 样本的对照实验数据，计算交叉验证机制对最终结论正确率的绝对提升百分比，并评估其是否足以抵消成本增加。

## Corrected Claim

准确率提升量化方法定义为 ΔAccuracy = Accuracy_with_XVal - Accuracy_without_XVal，通常需基于对照实验数据计算以评估交叉验证机制的效果及成本效益。

## Evidence

[质询]该陈述描述的是一个具体的实验设计或数据分析任务（基于N=100样本计算特定场景下的准确率提升），属于经验事实或特定项目上下文，无法从第一性原理推导，且参考来源仅解释了Accuracy的定义，未提供该具体实验的数据或结论。 | 逻辑自洽，但参考来源[1]仅涉及Accuracy定义，与该具体实验事实无关，缺乏外部证据支持，且属于经验事实，故降级。

## Search Query

cross-validation impact on LLM factual accuracy percentage

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/703347415&rut=30f4a9cc372540131cde4aa876bf123294d1e9b4476b3800c76cb3c2b805a313', 'type': 'ddg', 'title': '【深度学习】Precision、Accuracy的区别，精确率与准确率：深度学习多分类问题中的性能评估详解'}
