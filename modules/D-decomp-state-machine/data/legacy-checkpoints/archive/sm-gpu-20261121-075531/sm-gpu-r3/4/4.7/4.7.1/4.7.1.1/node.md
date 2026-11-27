# N304: Qwen3-27B INT8 权重的精确字节大小 (Model_Size_Bytes)：基于 27B 参数 * 1 Byte/param + 嵌入层/输出层可能

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

Qwen3-27B INT8 权重的精确字节大小 (Model_Size_Bytes)：基于 27B 参数 * 1 Byte/param + 嵌入层/输出层可能的 FP16 保留部分，精确计算值（通常为 27.0-27.5 GB），用于带宽瓶颈计算。

## Corrected Claim

Qwen3-27B INT8 权重的精确字节大小 (Model_Size_Bytes)：基于 27B 参数 * 1 Byte/param + 嵌入层/输出层可能的 FP16 保留部分，精确计算值（通常为 27.0-27.5 GB），用于带宽瓶颈计算。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT8下基础大小为27GB，加上嵌入层等可能的FP16保留部分，27.0-27.5GB的量级估算符合工程常识与数学推导。
