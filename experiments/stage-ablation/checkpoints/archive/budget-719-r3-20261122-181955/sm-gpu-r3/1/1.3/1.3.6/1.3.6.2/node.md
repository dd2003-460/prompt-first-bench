# N186: ROCm 平台 INT8/INT4 量化推理的性能损失量化：在 MI300X 上，使用 GPTQ/AWQ INT4 量化 Qwen3-27B 时，实测吞吐量相比

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

ROCm 平台 INT8/INT4 量化推理的性能损失量化：在 MI300X 上，使用 GPTQ/AWQ INT4 量化 Qwen3-27B 时，实测吞吐量相比 CUDA 平台同等量化方案通常降低 15-25%，主要瓶颈在于 ROCm 的量化内核优化滞后于 cuBLAS/cuDNN [待核验]

## Corrected Claim

在 MI300X 上，使用 GPTQ/AWQ INT4 量化 Qwen3-27B 时，实测吞吐量相比 CUDA 平台同等量化方案通常存在一定程度的性能差距，主要瓶颈在于 ROCm 的量化内核优化滞后于 cuBLAS/cuDNN。

## Evidence

[质询]具体数值区间（15-25%）及特定模型（Qwen3-27B）在 MI300X 上的实测数据属于高度具体的经验事实，缺乏公开基准测试支持，且 ROCm 性能随版本迭代波动大，该具体数值可能过时或不准确。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

ROCm MI300X INT4 quantization inference performance loss vs CUDA
