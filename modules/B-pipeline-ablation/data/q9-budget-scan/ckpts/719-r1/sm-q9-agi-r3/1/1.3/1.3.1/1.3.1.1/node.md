# N134: 数学推理损失的归因分解：ΔAccuracy = ΔSyntax_Error_Rate + ΔLogic_Error_Rate，其中 Syntax_Error_R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

数学推理损失的归因分解：ΔAccuracy = ΔSyntax_Error_Rate + ΔLogic_Error_Rate，其中 Syntax_Error_Rate 指无法解析的代码/公式比例，Logic_Error_Rate 指公式正确但推导步骤错误比例，需通过 Chain-of-Thought 逐步比对金标答案进行拆解

## Corrected Claim

数学推理损失的归因分解：ΔAccuracy = ΔSyntax_Error_Rate + ΔLogic_Error_Rate，其中 Syntax_Error_Rate 指无法解析的代码/公式比例，Logic_Error_Rate 指公式正确但推导步骤错误比例，需通过 Chain-of-Thought 逐步比对金标答案进行拆解

## Evidence

先验知识/题面给定，逻辑校验通过：该分解符合误差分析的基本互斥完备原则（MECE），即总准确率变化可归因为语法错误率变化和逻辑错误率变化的线性叠加（假设两者互斥且覆盖所有错误类型），且CoT比对是标准的评估方法。
