# N51: W4A16权重的实际存储大小：13.59GB权重 + Scale/Zero-point开销（通常4-bit量化每通道或每块存储1个FP16 Scale，开销约1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

W4A16权重的实际存储大小：13.59GB权重 + Scale/Zero-point开销（通常4-bit量化每通道或每块存储1个FP16 Scale，开销约1-2%），总显存需求约为13.7-13.9GB。

## Corrected Claim

W4A16权重的实际存储大小：13.59GB权重 + Scale/Zero-point开销（通常4-bit量化每通道或每块存储1个FP16 Scale，开销约1-2%），总显存需求约为13.7-13.9GB。

## Evidence

先验知识/题面给定，逻辑校验通过：13.59GB权重在4-bit量化下，若采用每通道或每块存储1个FP16 Scale，其额外开销（Scale/Zero-point）通常在1-2%左右，总显存需求约为13.7-13.9GB，数值量级与逻辑自洽。

## Search Query

W4A16 quantization memory footprint scale overhead
