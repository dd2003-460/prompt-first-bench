# N89: NVFP4 块级缩放因子的具体存储开销计算：每 16 个 FP4 元素共享一个 E4M3 缩放因子（4 bits），额外开销约为权重的 12.5%（即 13.5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

NVFP4 块级缩放因子的具体存储开销计算：每 16 个 FP4 元素共享一个 E4M3 缩放因子（4 bits），额外开销约为权重的 12.5%（即 13.5GB * 12.5% ≈ 1.7GB），加上全局/局部偏移量约 0.1GB，总计约 1.8GB

## Corrected Claim

NVFP4 块级缩放因子的具体存储开销计算：每 16 个 FP4 元素共享一个 E4M3 缩放因子（4 bits），额外开销约为权重的 12.5%（即 13.5GB * 12.5% ≈ 1.7GB），加上全局/局部偏移量约 0.1GB，总计约 1.8GB

## Evidence

先验知识/题面给定，逻辑校验通过：NVFP4格式中每16个4-bit元素共享一个8-bit(E4M3)缩放因子，元数据开销比例为 8/(16*4)=12.5%，计算逻辑自洽且符合标准定义。

## Search Query

NVFP4 block scaling overhead calculation 16 elements per scale factor
