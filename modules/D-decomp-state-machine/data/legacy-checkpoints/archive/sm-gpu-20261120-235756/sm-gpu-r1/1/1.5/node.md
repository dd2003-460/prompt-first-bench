# N11: INT8精度下权重存储需求为27.18GB，但需额外存储scale/zero-point（约增加2-5%开销），质量损失在复杂推理任务中可能达2-5%。

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

INT8精度下权重存储需求为27.18GB，但需额外存储scale/zero-point（约增加2-5%开销），质量损失在复杂推理任务中可能达2-5%。

## Corrected Claim

INT8精度下权重存储需求为27.18GB，但需额外存储scale/zero-point（约增加2-5%开销），质量损失在复杂推理任务中可能达2-5%。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化通常引入2-5%的额外存储开销（scale/zero-point）及2-5%的精度损失，符合工程常识。

## Search Query

INT8 quantization overhead scale zero-point quality loss
