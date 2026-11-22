# N140: FP8权重大小计算：Size_FP8 = 27e9 * 1 byte = 27GB，需确认FP8是否包含scale因子（如E4M3格式），以及scale因子的额

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

FP8权重大小计算：Size_FP8 = 27e9 * 1 byte = 27GB，需确认FP8是否包含scale因子（如E4M3格式），以及scale因子的额外显存占用（通常<1%）

## Corrected Claim

FP8权重大小计算：Size_FP8 = 27e9 * 1 byte = 27GB，需确认FP8是否包含scale因子（如E4M3格式），以及scale因子的额外显存占用（通常<1%）

## Evidence

先验知识/题面给定，逻辑校验通过：27e9参数 * 1字节/参数 = 27GB，量纲与数值计算正确；FP8格式（如E4M3）通常伴随极小的scale因子开销，符合工程常识。
