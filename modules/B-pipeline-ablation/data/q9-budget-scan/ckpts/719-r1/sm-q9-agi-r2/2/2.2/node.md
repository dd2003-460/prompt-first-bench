# N11: ReAct (Reasoning + Acting) 或类似 Agent 框架中，工具调用链路（如代码执行器、文献搜索API）的单次平均延迟（Latency p

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

ReAct (Reasoning + Acting) 或类似 Agent 框架中，工具调用链路（如代码执行器、文献搜索API）的单次平均延迟（Latency per Tool Call）与任务成功率（Task Success Rate）的关系曲线。

## Corrected Claim

ReAct 框架中，工具调用的延迟可能影响任务成功率（例如通过增加超时风险或消耗上下文窗口），但具体的延迟-成功率关系曲线需依赖特定实验环境的数据，现有通用文献未给出统一的标准曲线。

## Evidence

[质询]该陈述描述的是一个具体的经验性关系曲线（Latency vs Success Rate），这属于经验事实。提供的参考来源 [1] 和 [2] 主要介绍 ReAct 框架的定义、起源及核心思想（推理与行动的结合），并未包含关于“单次工具调用平均延迟”与“任务成功率”之间具体量化关系或曲线的数据分析。因此，缺乏直接的外部证据支持这一特定经验结论。 | 逻辑上，高延迟可能导致超时或上下文窗口溢出从而降低成功率，符合直觉；但参考来源 [1][2] 仅定义 ReAct 框架，未提供延迟与成功率的实证数据或曲线，属于经验事实且缺来源直接支持。

## Search Query

ReAct agent tool calling latency vs task success rate empirical data

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1935762059888419552&rut=2136fc8598d21547f89da8e4afc594d65d4774c0d3644607c30e4ece62b86c3a', 'type': 'ddg', 'title': 'ReAct：AI Agent 的推理与行动融合框架 - 知乎'}
- {'url': 'https://arxiv.org/abs/2210.03629&rut=afdfa271f0e4da0290d9f66e85c70ecb1e751c63db470d7f19673271e9226517', 'type': 'ddg', 'title': 'ReAct: Synergizing Reasoning and Acting in Language Models'}
