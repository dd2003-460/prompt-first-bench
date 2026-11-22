# N80: INT8 精度下每参数字节数为 1 byte，但需额外存储缩放因子 (scale) 和零点 (zero_point)，通常每 128 个参数共享一组缩放因子，额

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

INT8 精度下每参数字节数为 1 byte，但需额外存储缩放因子 (scale) 和零点 (zero_point)，通常每 128 个参数共享一组缩放因子，额外开销约 1-2%。

## Corrected Claim

INT8 精度下每参数字节数为 1 byte，但需额外存储缩放因子 (scale) 和零点 (zero_point)，通常每 128 个参数共享一组缩放因子，额外开销约 1-2%。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8 每参数 1 字节符合定义；每 128 参数共享一组 scale/zero_point（通常各占 1 字节或 2 字节），额外开销约为 2/128 ≈ 1.56%，落在 1-2% 区间内，量级与逻辑均自洽。
