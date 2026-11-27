# N12: 实验设计阶段的迭代循环次数：基于文献检索结果，平均需 3-5 次 refinement 才能收敛到可执行方案；每次 refinement 涉及 1-2k tok

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

实验设计阶段的迭代循环次数：基于文献检索结果，平均需 3-5 次 refinement 才能收敛到可执行方案；每次 refinement 涉及 1-2k tokens 的上下文更新，总 token 消耗约为初始 prompt 的 4-8 倍

## Corrected Claim

实验设计阶段通常经历多次迭代循环以收敛至可执行方案，每次迭代伴随一定规模的上下文更新，导致总token消耗显著高于初始prompt，具体次数与倍数视任务复杂度而定。

## Evidence

[质询]该陈述包含具体的经验性数值（3-5次迭代、1-2k tokens、4-8倍消耗），这些并非从第一性原理或逻辑公理中必然推导出的恒定值，而是高度依赖于具体任务复杂度、模型版本及提示词工程的经验统计数据，缺乏普适性的理论支撑。 | source=knowledge，逻辑自洽（迭代收敛与token累积符合一般LLM交互直觉），但作为经验事实缺乏直接来源支持，依据规则降级。
