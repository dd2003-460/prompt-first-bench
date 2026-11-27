# N157: 量化质量损失的临界阈值定义：业务侧可接受的 Perplexity 增加上限（如 <1% 为透明，1-3% 为可接受，>3% 为不可接受），以及对应的下游任务（如

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

量化质量损失的临界阈值定义：业务侧可接受的 Perplexity 增加上限（如 <1% 为透明，1-3% 为可接受，>3% 为不可接受），以及对应的下游任务（如代码生成 HumanEval Pass@1）准确率下降容忍度（如 <2%）。此阈值用于判断 N49/N50 的数值是否满足'质量损失可接受'的标准。

## Corrected Claim

量化质量损失的临界阈值定义：业务侧可接受的 Perplexity 增加上限（如 <1% 为透明，1-3% 为可接受，>3% 为不可接受），以及对应的下游任务（如代码生成 HumanEval Pass@1）准确率下降容忍度（如 <2%）。此阈值用于判断 N49/N50 的数值是否满足'质量损失可接受'的标准。

## Evidence

先验知识/题面给定，逻辑校验通过
