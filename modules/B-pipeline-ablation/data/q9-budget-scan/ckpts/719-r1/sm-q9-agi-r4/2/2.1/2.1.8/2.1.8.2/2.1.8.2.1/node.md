# N476: 工作点A（短上下文快循环）：单循环Token消耗下限为5000 tokens，对应假设生成500 tokens、实验设计500 tokens、代码执行反馈100

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N170

## Claim

工作点A（短上下文快循环）：单循环Token消耗下限为5000 tokens，对应假设生成500 tokens、实验设计500 tokens、代码执行反馈1000 tokens、分析结论3000 tokens，适用于文献综述或简单假设验证，单次耗时约250s。

## Corrected Claim

工作点A（短上下文快循环）：单循环Token消耗下限为5000 tokens，对应假设生成500 tokens、实验设计500 tokens、代码执行反馈1000 tokens、分析结论3000 tokens，适用于文献综述或简单假设验证，单次耗时约250s。

## Evidence

先验知识/题面给定，逻辑校验通过：各分项Token数之和（500+500+1000+3000=5000）与总下限一致，耗时估算符合常规LLM推理速度量级，无内部矛盾。
