# N11: 在'分析'步骤中，数据分析代码生成的正确率 P_correct_code 依赖于代码长度 L_code，P_correct_code = exp(-beta *

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

在'分析'步骤中，数据分析代码生成的正确率 P_correct_code 依赖于代码长度 L_code，P_correct_code = exp(-beta * L_code)，beta 为错误累积系数，典型值 beta ≈ 0.001 per line [待核验]

## Corrected Claim

在'分析'步骤中，数据分析代码生成的正确率 P_correct_code 依赖于代码长度 L_code，P_correct_code = exp(-beta * L_code)，beta 为错误累积系数，典型值 beta ≈ 0.001 per line [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过
