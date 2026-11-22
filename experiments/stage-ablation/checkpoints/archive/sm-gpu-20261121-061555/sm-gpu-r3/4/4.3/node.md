# N25: 量化精度对推理速度的非线性影响：低比特量化（INT4/NVFP4）虽减少带宽需求，但可能触发更复杂的 dequantize 计算路径，实际加速比需实测，不能仅按

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

量化精度对推理速度的非线性影响：低比特量化（INT4/NVFP4）虽减少带宽需求，但可能触发更复杂的 dequantize 计算路径，实际加速比需实测，不能仅按字节数线性外推

## Corrected Claim

量化精度对推理速度的非线性影响：低比特量化（INT4/NVFP4）虽减少带宽需求，但可能触发更复杂的 dequantize 计算路径，实际加速比需实测，不能仅按字节数线性外推

## Evidence

先验知识/题面给定，逻辑校验通过：低比特量化确实涉及非线性的计算开销（如dequantize路径复杂度），不能仅按字节数线性外推，符合硬件推理的基本原理。

## Search Query

INT4 quantization inference speed overhead dequantization cost
