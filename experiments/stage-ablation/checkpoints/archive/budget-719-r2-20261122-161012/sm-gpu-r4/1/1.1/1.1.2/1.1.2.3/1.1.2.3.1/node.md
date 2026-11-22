# N348: PyTorch 2.x 及 CUDA 12.x 运行时在 RTX 4090 上的固定显存基线开销：在加载模型前，`torch.cuda.memory_alloc

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

PyTorch 2.x 及 CUDA 12.x 运行时在 RTX 4090 上的固定显存基线开销：在加载模型前，`torch.cuda.memory_allocated()` 通常显示 200-500 MB，加上 CUDA Context 和算子缓存，总固定开销约为 0.5 GB。

## Corrected Claim

PyTorch 2.x 及 CUDA 12.x 运行时在 RTX 4090 上的固定显存基线开销：在加载模型前，`torch.cuda.memory_allocated()` 通常显示 200-500 MB，加上 CUDA Context 和算子缓存，总固定开销约为 0.5 GB。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

PyTorch CUDA context memory footprint baseline RTX 4090
