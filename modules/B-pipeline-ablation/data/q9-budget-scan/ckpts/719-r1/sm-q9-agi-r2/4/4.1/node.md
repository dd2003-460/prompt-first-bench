# N16: 定义‘可发表级’结论的自动化校验基准：选取3篇Nature/Science子刊近1年AI相关论文，提取其核心统计指标（p-value < 0.05, effec

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

定义‘可发表级’结论的自动化校验基准：选取3篇Nature/Science子刊近1年AI相关论文，提取其核心统计指标（p-value < 0.05, effect size > 0.2, n > 30）作为硬约束阈值

## Corrected Claim

定义‘可发表级’结论的自动化校验基准：选取3篇Nature/Science子刊近1年AI相关论文，提取其核心统计指标作为参考阈值，但需注意不同学科对p-value、effect size和样本量的具体要求可能存在差异，不宜简单统一为固定硬约束。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别针对父节点中定义的三个独立统计指标（p-value, effect size, sample size）进行了具体的方法论细化与修正。它们在逻辑上是正交的（互不重叠），共同覆盖了父节点设定的所有硬约束阈值，且不存在将一个参数拆分为多个互斥取值的冗余情况。）

## Search Query

Nature Science 2025 AI research statistical significance thresholds p-value effect size sample size

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/2020500882727469784&rut=76b98d48080a7eb0f01ec946c3c171aafbaef27ede693afd06618730003e6bdc', 'type': 'ddg', 'title': 'AI 科学家登上 Nature，论文实现全自动化并过审，这将如何定义「科学」？ - 知乎'}
