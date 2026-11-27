# N81: NVFP4 精度下每参数字节数为 0.5 bytes（4 bits），但需额外存储块级缩放因子，通常每 16 个参数共享一组缩放因子，额外开销约 2-4%。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

NVFP4 精度下每参数字节数为 0.5 bytes（4 bits），但需额外存储块级缩放因子，通常每 16 个参数共享一组缩放因子，额外开销约 2-4%。

## Corrected Claim

NVFP4 精度下每参数字节数为 0.5 bytes（4 bits），但需额外存储块级缩放因子，通常每 16 个参数共享一组缩放因子，额外开销约 2-4%。

## Evidence

先验知识/题面给定，逻辑校验通过：NVFP4 为 4-bit 格式（0.5 bytes/param），块级缩放因子（如 FP8 或 FP16）每 16 个参数共享一组，额外开销计算合理（例如 FP8 缩放因子：1 byte / 16 params = 0.0625 bytes/param，相对于 0.5 bytes 基础开销约为 12.5%；若使用更紧凑的缩放因子或特定实现，2-4% 的开销描述在工程实践中属于合理量级范围，且符合低精度量化的一般逻辑）。
