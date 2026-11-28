# N39: FP8 精度下 KV Cache 的数据类型字节数 dtype_bytes 为 1 字节（每个元素占用 8 位），相比 BF16 可减少 50% 的 KV Ca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

FP8 精度下 KV Cache 的数据类型字节数 dtype_bytes 为 1 字节（每个元素占用 8 位），相比 BF16 可减少 50% 的 KV Cache 显存占用，且数值精度高于 INT8。

## Corrected Claim

FP8 精度下 KV Cache 的数据类型字节数 dtype_bytes 为 1 字节（每个元素占用 8 位），相比 BF16 可减少 50% 的 KV Cache 显存占用，且数值精度高于 INT8。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8（如E4M3/E5M2）确实为8位（1字节），BF16为16位（2字节），1/2=50%减少正确；FP8采用浮点格式，动态范围远优于INT8（定点），精度通常高于INT8。
