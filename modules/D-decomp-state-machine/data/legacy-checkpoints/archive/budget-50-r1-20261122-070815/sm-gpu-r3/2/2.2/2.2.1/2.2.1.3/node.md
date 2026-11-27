# N217: FP8 量化相对于 BF16 在 MMLU 上的预期精度损失幅度：通常 FP8 权重量化导致 MMLU 下降 < 0.5-1.0 分（相对下降 < 1%），若下

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

FP8 量化相对于 BF16 在 MMLU 上的预期精度损失幅度：通常 FP8 权重量化导致 MMLU 下降 < 0.5-1.0 分（相对下降 < 1%），若下降超过 2 分则视为不可接受的质量损失，需回退至 BF16 或 INT8

## Corrected Claim

FP8 量化相对于 BF16 在 MMLU 上的预期精度损失幅度：通常 FP8 权重量化导致 MMLU 下降 < 0.5-1.0 分（相对下降 < 1%），若下降超过 2 分则视为不可接受的质量损失，需回退至 BF16 或 INT8

## Evidence

先验知识/题面给定，逻辑校验通过
