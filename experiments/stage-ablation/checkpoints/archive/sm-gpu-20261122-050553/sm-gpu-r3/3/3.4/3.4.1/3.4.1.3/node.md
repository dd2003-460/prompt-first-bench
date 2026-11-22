# N222: W4-AWQ 量化导致 HumanEval 性能下降的主要机制：代码生成任务对数字常量、运算符顺序等细微 token 概率分布敏感，W4 量化将激活值截断至 4

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N71

## Claim

W4-AWQ 量化导致 HumanEval 性能下降的主要机制：代码生成任务对数字常量、运算符顺序等细微 token 概率分布敏感，W4 量化将激活值截断至 4bit，导致 Logit 分布熵增加 ΔH ≈ 0.05-0.1 bits/token [待核验]，使得模型在边界条件判断上错误率上升约 2-3 倍，具体需通过 Logit 分布 KL 散度量化验证。

## Corrected Claim

W4-AWQ 量化导致 HumanEval 性能下降的主要机制：代码生成任务对数字常量、运算符顺序等细微 token 概率分布敏感，W4 量化将激活值截断至 4bit，导致 Logit 分布发生偏移（熵增加或 KL 散度增大），使得模型在边界条件判断上错误率上升，具体幅度需通过 Logit 分布 KL 散度量化验证。

## Evidence

[质询]陈述中给出的具体数值（ΔH ≈ 0.05-0.1 bits/token，错误率上升 2-3 倍）缺乏通用性，属于特定实验条件下的经验数据，且未指明具体模型规模、数据集版本或量化实现细节，存在以偏概全或数值量级不准确的风险。 | 先验知识/题面给定，逻辑校验通过：W4 量化确实会引入噪声并影响 Logit 分布，导致对细微 token 概率敏感的任务（如代码生成）性能下降，机制解释符合逻辑；但具体数值缺乏来源支持，故降级。

## Search Query

low-bit quantization impact on code generation logit distribution entropy
