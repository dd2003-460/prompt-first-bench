# N61: 单次完整科研循环的平均步骤数 N_steps：基于 ReAct 轨迹分析，典型科研任务（检索+代码+分析）平均包含 15-25 步工具调用；取中位数 N_ste

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

单次完整科研循环的平均步骤数 N_steps：基于 ReAct 轨迹分析，典型科研任务（检索+代码+分析）平均包含 15-25 步工具调用；取中位数 N_steps = 20。

## Corrected Claim

基于ReAct轨迹分析，典型科研任务（检索+代码+分析）通常包含多步工具调用，具体步骤数视任务复杂度而定，常见估计在15-25步之间（注：此数值为经验估计，缺乏当前来源的直接统计支持）。

## Evidence

[质询]该陈述声称基于“ReAct轨迹分析”得出特定数值范围（15-25步）及中位数（20），但提供的参考来源[1]仅介绍ReAct范式的理论背景和历史，并未包含任何具体的轨迹统计数据或步骤数量分布，属于典型的“经验事实”缺乏直接数据支撑。 | 逻辑上，复杂科研任务涉及多轮检索、代码执行和分析，20步左右的量级符合直觉且无内部矛盾；但参考来源[1]与具体数值统计无关，无法提供直接支持，且该数值属于经验事实，不能仅凭逻辑自洽判定为verified。

## Search Query

average number of steps in ReAct agent scientific research workflow

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2068108963254628516&rut=81c82826d9183cc9077c50b52dcc61640d8b28f58a50697fcc7e058e5cd676b1', 'type': 'ddg', 'title': 'AI学习Agent系列篇2（偏理论）：ReAct循环与工作流变体——推理与行动的最小闭环'}
