# N170: vLLM 在 RTX 4090 上运行 Qwen3-27B 时，CUDA context 的基础固定开销（不含 KV Cache）实测值为 1.8GB，该数值包

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

vLLM 在 RTX 4090 上运行 Qwen3-27B 时，CUDA context 的基础固定开销（不含 KV Cache）实测值为 1.8GB，该数值包含驱动、cuBLAS 句柄及框架初始化内存，不随模型精度变化

## Corrected Claim

vLLM 在 RTX 4090 上运行 Qwen3-27B 时，CUDA context 的基础固定开销（不含 KV Cache）实测值约为 1.8GB，该数值主要包含驱动、cuBLAS 句柄及框架初始化内存，在常规配置下不随模型精度显著变化。

## Evidence

[质询]该数值为特定硬件（RTX 4090）、特定软件栈版本（vLLM/CUDA/驱动）及特定模型架构（Qwen3-27B）下的经验实测值，属于具体工程参数，无法从第一性原理严格推导；且'不随模型精度变化'这一断言在极端配置或不同框架版本下可能存在细微差异，缺乏通用性保证。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM CUDA context memory overhead RTX 4090 benchmark
