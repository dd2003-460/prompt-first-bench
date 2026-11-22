# N266: Qwen3-27B 在 INT4 量化下的权重文件大小计算公式：Weight_Size_Bytes = (27e9 params * 4 bits) / 8 =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

Qwen3-27B 在 INT4 量化下的权重文件大小计算公式：Weight_Size_Bytes = (27e9 params * 4 bits) / 8 = 13.5 GB，该数值为 Dequantize 延迟计算中的 Model_Size_Bytes 基础项。

## Corrected Claim

Qwen3-27B 在 INT4 量化下的权重文件大小计算公式：Weight_Size_Bytes = (27e9 params * 4 bits) / 8 = 13.5 GB，该数值为 Dequantize 延迟计算中的 Model_Size_Bytes 基础项。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 4 / 8 = 13.5e9 Bytes = 13.5 GB，计算无误且符合INT4量化定义。
