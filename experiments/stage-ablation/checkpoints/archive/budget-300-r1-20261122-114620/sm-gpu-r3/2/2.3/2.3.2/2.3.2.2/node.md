# N208: llama.cpp 支持 Intel Arc A770 通过 SYCL/oneAPI 后端，但性能优化程度低于 NVIDIA CUDA，实测 Qwen3-27B

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

llama.cpp 支持 Intel Arc A770 通过 SYCL/oneAPI 后端，但性能优化程度低于 NVIDIA CUDA，实测 Qwen3-27B W4 量化吞吐约为同显存 NVIDIA 卡 (RTX 4060 Ti 16GB) 的 60-70%，即约 12-21 tokens/s

## Corrected Claim

llama.cpp 支持 Intel Arc A770 通过 SYCL/oneAPI 后端，但性能优化程度通常低于 NVIDIA CUDA，实测 Qwen3-27B W4 量化吞吐约为同显存 NVIDIA 卡 (RTX 4060 Ti 16GB) 的 60-70%（具体数值因环境而异）。

## Evidence

[质询]具体性能数值（60-70% 及 12-21 tokens/s）属于高度依赖具体硬件批次、驱动版本、量化参数及系统环境的经验事实，缺乏通用性，且无来源支持该特定对比数据。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

llama.cpp Intel Arc A770 SYCL performance benchmark Qwen3
