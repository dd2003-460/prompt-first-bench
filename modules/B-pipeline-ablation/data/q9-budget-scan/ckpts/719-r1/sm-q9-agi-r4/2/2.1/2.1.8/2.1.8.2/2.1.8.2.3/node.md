# N478: 工作点C（长上下文深推理）：单循环Token消耗上限为8000 tokens，对应假设生成1000 tokens、实验设计1500 tokens、代码执行反馈2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N170

## Claim

工作点C（长上下文深推理）：单循环Token消耗上限为8000 tokens，对应假设生成1000 tokens、实验设计1500 tokens、代码执行反馈2500 tokens、数据分析2000 tokens、结论生成1000 tokens，适用于复杂数值模拟或多步推导，单次耗时约400s，边际收益递减明显。

## Corrected Claim

工作点C（长上下文深推理）：单循环Token消耗上限为8000 tokens，对应假设生成1000 tokens、实验设计1500 tokens、代码执行反馈2500 tokens、数据分析2000 tokens、结论生成1000 tokens，适用于复杂数值模拟或多步推导，单次耗时约400s，边际收益递减明显。

## Evidence

先验知识/题面给定，逻辑校验通过：各分项Token之和（1000+1500+2500+2000+1000=8000）与总上限一致，耗时与Token量级符合大模型推理常识，无内部矛盾。
