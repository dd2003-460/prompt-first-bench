# N49: INT8推理的校准成本：需使用校准数据集（如WikiText）进行量化校准，耗时通常为分钟级，但需评估校准数据集对目标领域分布的敏感性（若领域偏差大，质量损失可

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

INT8推理的校准成本：需使用校准数据集（如WikiText）进行量化校准，耗时通常为分钟级，但需评估校准数据集对目标领域分布的敏感性（若领域偏差大，质量损失可能超过5%）。

## Corrected Claim

INT8推理的校准成本：需使用校准数据集（如WikiText）进行量化校准，耗时通常为分钟级，但需评估校准数据集对目标领域分布的敏感性（若领域偏差大，质量损失可能超过5%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

INT8 quantization calibration dataset sensitivity domain shift
