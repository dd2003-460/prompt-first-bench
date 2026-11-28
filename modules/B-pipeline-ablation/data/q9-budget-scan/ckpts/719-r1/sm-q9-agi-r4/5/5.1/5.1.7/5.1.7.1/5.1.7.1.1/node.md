# N678: T_process_start (vLLM engine init) 的实测分解：包括 Python 模块导入、CUDA 上下文创建及 Tensor Paral

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N246

## Claim

T_process_start (vLLM engine init) 的实测分解：包括 Python 模块导入、CUDA 上下文创建及 Tensor Parallel 初始化；在 4x V100 环境下，实测耗时通常为 1.5s-2.5s，取决于 SSD 读取速度和 CPU 核心数

## Corrected Claim

T_process_start (vLLM engine init) 的实测分解：包括 Python 模块导入、CUDA 上下文创建及 Tensor Parallel 初始化；在 4x V100 环境下，实测耗时通常为 1.5s-2.5s，取决于 SSD 读取速度和 CPU 核心数

## Evidence

先验知识/题面给定，逻辑校验通过
