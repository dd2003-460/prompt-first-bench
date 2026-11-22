# N375: vLLM 或 PyTorch ROCm 后端的依赖安装与编译（包括 PyTorch ROCm wheel 下载、HIP 编译器配置、vLLM 源码编译或预编译包

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N147

## Claim

vLLM 或 PyTorch ROCm 后端的依赖安装与编译（包括 PyTorch ROCm wheel 下载、HIP 编译器配置、vLLM 源码编译或预编译包安装）耗时约为 1-3 小时；若需从源码编译 PyTorch ROCm 版本（非预编译 wheel），耗时可达 4-8 小时，取决于 CPU 核心数与内存大小。

## Corrected Claim

vLLM 或 PyTorch ROCm 后端的依赖安装与编译耗时受硬件配置影响显著：使用预编译 wheel 通常需 1-3 小时；若从源码编译 PyTorch ROCm，耗时可能长达 4-8 小时或更久，具体取决于 CPU 核心数、内存大小及网络条件。

## Evidence

[质询]具体耗时数值（1-3小时 vs 4-8小时）属于高度依赖硬件配置（CPU核心数、内存、网络带宽）的经验事实，缺乏统一标准，且不同版本/环境差异巨大，无法从第一性原理严格推导。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

PyTorch ROCm build from source time HIP compiler vLLM AMD GPU installation duration
