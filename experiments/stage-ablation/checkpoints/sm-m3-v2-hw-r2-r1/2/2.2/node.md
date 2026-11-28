# N13: Prompt 工程策略需采用‘思维链（CoT）+ 自我一致性（Self-Consistency）’组合，针对 27B 模型，建议采样温度 0.7-0.8，top

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

Prompt 工程策略需采用‘思维链（CoT）+ 自我一致性（Self-Consistency）’组合，针对 27B 模型，建议采样温度 0.7-0.8，top_p 0.9，以平衡探索性与稳定性；科研假设生成环节需增加‘反事实检查’指令以提升可靠性。

## Corrected Claim

Prompt 工程策略需采用‘思维链（CoT）+ 自我一致性（Self-Consistency）’组合，针对 27B 模型，建议采样温度 0.7-0.8，top_p 0.9，以平衡探索性与稳定性；科研假设生成环节需增加‘反事实检查’指令以提升可靠性。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM prompt engineering self-consistency scientific hypothesis generation parameters
