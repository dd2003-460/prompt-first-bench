# N171: 约束条件2：精度容忍度 Precision_Loss_Max。若任务为通用对话，允许 INT4 (Loss ~5%)；若为代码/数学推理，仅允许 FP8/INT

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

约束条件2：精度容忍度 Precision_Loss_Max。若任务为通用对话，允许 INT4 (Loss ~5%)；若为代码/数学推理，仅允许 FP8/INT8 (Loss <1-2%)。该阈值决定可选精度集合，进而影响显存需求和硬件选择。

## Corrected Claim

约束条件2：精度容忍度 Precision_Loss_Max。若任务为通用对话，允许 INT4 (Loss ~5%)；若为代码/数学推理，仅允许 FP8/INT8 (Loss <1-2%)。该阈值决定可选精度集合，进而影响显存需求和硬件选择。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

quantization accuracy loss threshold LLM code generation
