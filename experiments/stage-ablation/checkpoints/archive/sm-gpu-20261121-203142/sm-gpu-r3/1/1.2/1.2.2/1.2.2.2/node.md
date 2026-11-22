# N139: 若采用Block-wise量化（如128x128 blocks），Scale/Zeropoint开销显著增加：每个block需存储1个scale和1个zero 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

若采用Block-wise量化（如128x128 blocks），Scale/Zeropoint开销显著增加：每个block需存储1个scale和1个zero point，总block数 = (params / 128^2)，对于27.2B参数，开销约为 (27.2e9 / 16384) * 2 bytes * 2 ≈ 6.6 MB，仍远低于权重显存，但需考虑量化误差累积对长上下文推理的影响。

## Corrected Claim

若采用Block-wise量化（如128x128 blocks），Scale/Zeropoint开销显著增加：每个block需存储1个scale和1个zero point，总block数 = (params / 128^2)，对于27.2B参数，开销约为 (27.2e9 / 16384) * 2 bytes * 2 ≈ 6.6 MB，仍远低于权重显存，但需考虑量化误差累积对长上下文推理的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：27.2e9 / 16384 ≈ 1.66e6 blocks，每block 2个float16参数(4 bytes)或2个float32参数(8 bytes)，计算结果6.6MB量级合理且远小于权重显存。

## Search Query

block-wise INT8 quantization scale overhead 128x128
