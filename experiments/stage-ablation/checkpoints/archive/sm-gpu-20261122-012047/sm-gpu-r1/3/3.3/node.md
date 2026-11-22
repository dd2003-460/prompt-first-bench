# N22: INT4 量化相比 BF16 可将推理速度提升 2.5-3.5 倍，但需要额外的反量化计算开销，实际加速比取决于量化方案（GPTQ/AWQ）和硬件支持（RTX 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

INT4 量化相比 BF16 可将推理速度提升 2.5-3.5 倍，但需要额外的反量化计算开销，实际加速比取决于量化方案（GPTQ/AWQ）和硬件支持（RTX 4090 支持 INT8 Tensor Core，INT4 需软件模拟）。

## Corrected Claim

INT4 量化相比 BF16 可将推理速度提升 2.5-3.5 倍，但需要额外的反量化计算开销，实际加速比取决于量化方案（GPTQ/AWQ）和硬件支持（RTX 4090 支持 INT8 Tensor Core，INT4 需软件模拟）。

## Evidence

先验知识/题面给定，逻辑校验通过
