# N57: INT8量化在代码生成任务（HumanEval/MBPP）上相比BF16的通过率下降通常为2.0%-4.0%，代码逻辑对token级精度敏感，若超过N15定义的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

INT8量化在代码生成任务（HumanEval/MBPP）上相比BF16的通过率下降通常为2.0%-4.0%，代码逻辑对token级精度敏感，若超过N15定义的5.0%阈值则判定为不可接受 [待核验: Qwen3-27B INT8 HumanEval pass@1]

## Corrected Claim

INT8量化在代码生成任务上相比BF16通常存在一定程度的通过率下降，具体幅度取决于模型规模与任务难度，若下降超过5.0%阈值则判定为不可接受。

## Evidence

[质询]该陈述包含具体的经验性数值范围（2.0%-4.0%）和特定模型（Qwen3-27B）的性能指标，属于硬件/模型规格类的经验事实，无法从第一性原理推导，且当前无可用外部来源支持该具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无可用外部证据）

## Search Query

Qwen3-27B INT8 W8A8 HumanEval pass@1 code generation accuracy loss
