# N52: CUDA Context 与 Driver 开销：在 NVIDIA GPU 上，加载 CUDA 上下文及驱动初始化通常占用 1.5-3.0 GB 显存，该部分开

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

CUDA Context 与 Driver 开销：在 NVIDIA GPU 上，加载 CUDA 上下文及驱动初始化通常占用 1.5-3.0 GB 显存，该部分开销与模型大小无关，但随 GPU 驱动版本和 CUDA 版本略有波动，是固定预留项。

## Corrected Claim

CUDA Context 与 Driver 开销：在 NVIDIA GPU 上，加载 CUDA 上下文及驱动初始化通常占用 1.5-3.0 GB 显存，该部分开销与模型大小无关，但随 GPU 驱动版本和 CUDA 版本略有波动，是固定预留项。

## Evidence

先验知识/题面给定，逻辑校验通过
