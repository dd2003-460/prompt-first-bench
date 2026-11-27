# N379: INT8 AWQ 量化对 HumanEval Pass@1 的影响机制：代码生成任务对语法结构、变量命名一致性和逻辑完整性敏感，INT8 量化导致的 token

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N149

## Claim

INT8 AWQ 量化对 HumanEval Pass@1 的影响机制：代码生成任务对语法结构、变量命名一致性和逻辑完整性敏感，INT8 量化导致的 token 概率分布微小偏移可能在代码生成中放大，导致语法错误率上升或逻辑分支错误增加；AWQ 算法通过保护显著权重（activation-aware）可部分缓解此问题，但相比 GPTQ，AWQ 在代码生成任务上的质量保持能力需通过对比实验验证。

## Corrected Claim

INT8 AWQ 量化对 HumanEval Pass@1 的影响机制：代码生成任务对语法结构、变量命名一致性和逻辑完整性敏感，INT8 量化导致的 token 概率分布微小偏移可能在代码生成中放大，导致语法错误率上升或逻辑分支错误增加；AWQ 算法通过保护显著权重（activation-aware）可部分缓解此问题，但相比 GPTQ，AWQ 在代码生成任务上的质量保持能力需通过对比实验验证。

## Evidence

先验知识/题面给定，逻辑校验通过
