# N141: INT8权重大小计算：Size_INT8 = 27e9 * 1 byte = 27GB（注意：INT8通常为per-channel或per-token量化，需额

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

INT8权重大小计算：Size_INT8 = 27e9 * 1 byte = 27GB（注意：INT8通常为per-channel或per-token量化，需额外存储scale和zero_point，额外占用约1-5%）

## Corrected Claim

INT8权重大小计算：Size_INT8 = 27e9 * 1 byte = 27GB（注意：INT8通常为per-channel或per-token量化，需额外存储scale和zero_point，额外占用约1-5%）

## Evidence

先验知识/题面给定，逻辑校验通过：27e9参数 * 1字节/参数 = 27GB，量纲与数值计算正确；INT8量化额外开销1-5%符合工程常识。
