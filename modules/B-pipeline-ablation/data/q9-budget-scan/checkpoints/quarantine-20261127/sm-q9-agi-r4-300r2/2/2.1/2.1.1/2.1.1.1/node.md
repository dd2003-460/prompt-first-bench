# N117: ReAct 单次循环 Token 消耗增量 ΔT_ReAct = T_Action_Prompt + T_Observation_Return - T_CoT_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

ReAct 单次循环 Token 消耗增量 ΔT_ReAct = T_Action_Prompt + T_Observation_Return - T_CoT_Step，其中 T_Action_Prompt 约为 20-50 tokens（JSON 格式化开销），T_Observation_Return 取决于工具返回截断长度（默认 512 tokens），相比 CoT 纯思维链每步 ~100 tokens，ReAct 在长循环中 Token 膨胀率约为 1.5x-2.0x

## Corrected Claim

ReAct 单次循环 Token 消耗增量 ΔT_ReAct = T_Action_Prompt + T_Observation_Return - T_CoT_Step，其中 T_Action_Prompt 约为 20-50 tokens（JSON 格式化开销），T_Observation_Return 取决于工具返回截断长度（默认 512 tokens），相比 CoT 纯思维链每步 ~100 tokens，ReAct 在长循环中 Token 膨胀率约为 1.5x-2.0x

## Evidence

先验知识/题面给定，逻辑校验通过
