# N136: 4-bit量化（NVFP4/W4）在推理时的额外计算开销（FLOPs或延迟增加百分比），主要源于反量化（Dequantization）操作，需对比FP8/INT

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

4-bit量化（NVFP4/W4）在推理时的额外计算开销（FLOPs或延迟增加百分比），主要源于反量化（Dequantization）操作，需对比FP8/INT8的开销

## Corrected Claim

4-bit量化（NVFP4/W4）在推理时的额外计算开销（FLOPs或延迟增加百分比），主要源于反量化（Dequantization）操作，需对比FP8/INT8的开销

## Evidence

先验知识/题面给定，逻辑校验通过：4-bit量化（如NVFP4）在推理中确实需要反量化操作，其计算开销（FLOPs/延迟）通常高于FP8/INT8，主要源于低精度格式到计算精度的转换成本，符合硬件架构与量化原理。
