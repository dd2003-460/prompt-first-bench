# N12: 最小可行 Agent 架构包含三个核心角色：Orchestrator（规划下一步行动，输入当前状态+目标，输出动作序列）、Executor（执行具体 API/代

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

最小可行 Agent 架构包含三个核心角色：Orchestrator（规划下一步行动，输入当前状态+目标，输出动作序列）、Executor（执行具体 API/代码/检索调用）、Critic（评估中间结果是否符合科研逻辑，决定是否回溯），三者通过 JSON 结构化消息通信，避免自然语言歧义导致的指令漂移

## Corrected Claim

最小可行 Agent 架构包含三个核心角色：Orchestrator（规划下一步行动，输入当前状态+目标，输出动作序列）、Executor（执行具体 API/代码/检索调用）、Critic（评估中间结果是否符合科研逻辑，决定是否回溯），三者通过 JSON 结构化消息通信，避免自然语言歧义导致的指令漂移

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-agent system orchestrator executor critic architecture llm
