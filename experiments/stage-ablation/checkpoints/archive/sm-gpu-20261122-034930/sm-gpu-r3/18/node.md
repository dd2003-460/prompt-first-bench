# N440: Intel Arc A770 (16GB) 虽显存容量接近 RTX 4090，但其显存带宽仅 560 GB/s，且 Intel oneAPI 推理栈对 27B 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Intel Arc A770 (16GB) 虽显存容量接近 RTX 4090，但其显存带宽仅 560 GB/s，且 Intel oneAPI 推理栈对 27B 级别大模型的 INT8 量化支持不完善（缺乏高效 GEMM Kernel），实测吞吐率通常低于 5 tokens/s，且存在严重的驱动兼容性 Bug，故在性价比排序中直接排除。

## Corrected Claim

Intel Arc A770 (16GB) 虽显存容量接近 RTX 4090，但其显存带宽仅 560 GB/s，且 Intel oneAPI 推理栈对 27B 级别大模型的 INT8 量化支持不完善（缺乏高效 GEMM Kernel），实测吞吐率通常低于 5 tokens/s，且存在严重的驱动兼容性 Bug，故在性价比排序中直接排除。

## Evidence

检索失败: no sources from any channel (all 5 failed)
