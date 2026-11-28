# N228: GPQA Diamond 基准中逻辑推理错误（Logical Error）的量化判定标准：模型最终答案错误，但通过中间步骤回溯发现某一步推理违反了演绎逻辑规则（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

GPQA Diamond 基准中逻辑推理错误（Logical Error）的量化判定标准：模型最终答案错误，但通过中间步骤回溯发现某一步推理违反了演绎逻辑规则（如否定前件谬误、无效归纳），而所用前提事实均为真

## Corrected Claim

GPQA Diamond 基准中逻辑推理错误（Logical Error）的量化判定标准：模型最终答案错误，但通过中间步骤回溯发现某一步推理违反了演绎逻辑规则（如否定前件谬误、无效归纳），而所用前提事实均为真

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM logical reasoning error detection intermediate step verification GPQA
