# N139: BF16权重大小计算：Size_BF16 = 27e9 * 2 bytes = 54GB，需验证27e9参数是否包含embedding和lm_head层，以及是

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

BF16权重大小计算：Size_BF16 = 27e9 * 2 bytes = 54GB，需验证27e9参数是否包含embedding和lm_head层，以及是否有额外的bias参数

## Corrected Claim

BF16权重大小计算：Size_BF16 = 27e9 * 2 bytes = 54GB，需验证27e9参数是否包含embedding和lm_head层，以及是否有额外的bias参数

## Evidence

先验知识/题面给定，逻辑校验通过：BF16精度为2字节，27e9参数乘以2字节等于54GB，计算逻辑自洽且量级合理。
