# N64: 激活值显存占用分解：Activations_GB = Attention_Head_GB + MLP_Intermediate_GB + Residual_St

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

激活值显存占用分解：Activations_GB = Attention_Head_GB + MLP_Intermediate_GB + Residual_Stream_GB，三者互斥且需分别计算以评估峰值。

## Corrected Claim

激活值显存占用分解：Activations_GB = Attention_Head_GB + MLP_Intermediate_GB + Residual_Stream_GB，三者互斥且需分别计算以评估峰值。

## Evidence

先验知识/题面给定，逻辑校验通过
