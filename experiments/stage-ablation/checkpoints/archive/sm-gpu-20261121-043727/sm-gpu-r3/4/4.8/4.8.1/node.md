# N83: NVIDIA FP8 (E4M3/E5M2) 推理在 Linux 下最低驱动/CUDA 版本要求：需驱动 >= 525.60.13 (对应 CUDA 12.0)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

NVIDIA FP8 (E4M3/E5M2) 推理在 Linux 下最低驱动/CUDA 版本要求：需驱动 >= 525.60.13 (对应 CUDA 12.0) 或更高，以支持 Hopper (H100) 和 Ada Lovelace (RTX 4090) 的 Tensor Core FP8 指令；A100 (Ampere) 硬件不支持原生 FP8，仅能软件模拟或降级为 BF16/INT8。

## Corrected Claim

NVIDIA FP8 (E4M3/E5M2) 推理在 Linux 下最低驱动/CUDA 版本要求：需驱动 >= 525.60.13 (对应 CUDA 12.0) 或更高，以支持 Hopper (H100) 和 Ada Lovelace (RTX 4090) 的 Tensor Core FP8 指令；A100 (Ampere) 硬件不支持原生 FP8，仅能软件模拟或降级为 BF16/INT8。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA 官方文档确认 FP8 支持始于 Hopper (H100) 和 Ada Lovelace (RTX 40 系列) 架构，Ampere (A100) 硬件不支持原生 FP8；CUDA 12.0 (驱动 525.60.13) 是引入 FP8 支持的关键版本，符合技术演进逻辑。

## Search Query

NVIDIA driver version requirement FP8 inference CUDA 12.0 Hopper Ada Lovelace
