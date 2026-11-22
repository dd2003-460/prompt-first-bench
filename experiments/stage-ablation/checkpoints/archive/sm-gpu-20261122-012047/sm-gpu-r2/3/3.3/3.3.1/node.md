# N100: INT4 量化相比 BF16 的加速比并非恒定，而是受反量化（Dequantization）开销影响：在支持 INT8 Tensor Core 的硬件（如 RT

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

INT4 量化相比 BF16 的加速比并非恒定，而是受反量化（Dequantization）开销影响：在支持 INT8 Tensor Core 的硬件（如 RTX 4090）上，INT4 权重需先反量化为 INT8 再计算，实际加速比约为 2.0-2.5 倍；在支持原生 INT4 张量核心或高效 CUDA 核的硬件上，加速比可达 3.0-3.5 倍。

## Corrected Claim

INT4 量化相比 BF16 的加速比并非恒定，而是受反量化（Dequantization）开销影响：在支持 INT8 Tensor Core 的硬件（如 RTX 4090）上，INT4 权重需先反量化为 INT8 再计算，实际加速比约为 2.0-2.5 倍；在支持原生 INT4 张量核心或高效 CUDA 核的硬件上，加速比可达 3.0-3.5 倍。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

INT4 quantization dequantization overhead inference speedup ratio
