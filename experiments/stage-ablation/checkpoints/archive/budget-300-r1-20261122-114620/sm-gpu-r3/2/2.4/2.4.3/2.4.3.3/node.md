# N229: ROCm 生态下 Qwen3-27B 的 INT8 量化支持主要依赖 bitsandbytes 或 ExLlamaV2，其量化精度损失比 NVIDIA CUDA

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

ROCm 生态下 Qwen3-27B 的 INT8 量化支持主要依赖 bitsandbytes 或 ExLlamaV2，其量化精度损失比 NVIDIA CUDA 下的 AWQ/GPTQ 高约 1-2% PPL，因校准工具链成熟度较低 [待核验]

## Corrected Claim

ROCm 生态下 Qwen3-27B 的 INT8 量化支持主要依赖 bitsandbytes 或 ExLlamaV2，其量化精度损失通常比 NVIDIA CUDA 下的 AWQ/GPTQ 高，因校准工具链成熟度较低。

## Evidence

[质询]具体数值（1-2% PPL）和特定工具链依赖（bitsandbytes/ExLlamaV2）属于经验事实，缺乏直接来源支持，且不同量化方法在ROCm下的表现可能因模型版本和硬件配置而异，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

ROCm INT8 quantization accuracy loss vs CUDA AWQ Qwen3
