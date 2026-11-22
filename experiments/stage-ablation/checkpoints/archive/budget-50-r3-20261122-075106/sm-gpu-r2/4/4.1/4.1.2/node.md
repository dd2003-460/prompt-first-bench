# N75: 在 CPU Offload 模式下，每生成一个 Token 需从内存加载所有未缓存权重，理论最大 Token/s 上限为 DRAM_Bandwidth / Mo

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

在 CPU Offload 模式下，每生成一个 Token 需从内存加载所有未缓存权重，理论最大 Token/s 上限为 DRAM_Bandwidth / Model_Size_Bytes，即 100 GB/s / 54 GB ≈ 1.85 Token/s，远低于 N27 声称的 15-25 Token/s，表明 N27 数据可能基于量化或错误假设

## Corrected Claim

在 CPU Offload 模式下，每生成一个 Token 需从内存加载所有未缓存权重，理论最大 Token/s 上限为 DRAM_Bandwidth / Model_Size_Bytes，即 100 GB/s / 54 GB ≈ 1.85 Token/s，远低于 N27 声称的 15-25 Token/s，表明 N27 数据可能基于量化或错误假设

## Evidence

先验知识/题面给定，逻辑校验通过：CPU Offload 模式下每生成一个 Token 需加载全部未缓存权重，理论带宽上限为 DRAM 带宽除以模型大小，100 GB/s / 54 GB ≈ 1.85 Token/s，量纲与量级合理，与 N27 声称的 15-25 Token/s 存在数量级矛盾，表明 N27 数据可能基于量化或错误假设。
