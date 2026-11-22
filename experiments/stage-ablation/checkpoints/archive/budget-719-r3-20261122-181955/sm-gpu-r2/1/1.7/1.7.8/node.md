# N76: Qwen3-27B 的总参数量为 27.1 亿，BF16 精度下纯权重内存占用为 54.2 GB，FP8/INT8 精度下为 27.1 GB，INT4 精度下为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N14, N15

## Claim

Qwen3-27B 的总参数量为 27.1 亿，BF16 精度下纯权重内存占用为 54.2 GB，FP8/INT8 精度下为 27.1 GB，INT4 精度下为 13.55 GB。

## Corrected Claim

Qwen3-27B 的总参数量为 27.1 亿，BF16 精度下纯权重内存占用为 54.2 GB，FP8/INT8 精度下为 27.1 GB，INT4 精度下为 13.55 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27.1亿参数在BF16(2字节)下为54.2GB，FP8/INT8(1字节)下为27.1GB，INT4(0.5字节)下为13.55GB，数值计算完全自洽。

## Search Query

Qwen3-27B total parameters BF16 FP8 INT8 INT4 memory footprint
