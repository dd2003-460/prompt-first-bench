# N380: 2×RTX 3090在32K上下文下的Prefill延迟实测值：基于llama.cpp基准测试，2×3090 (PCIe 4.0) 在32K输入长度下的Pref

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N129

## Claim

2×RTX 3090在32K上下文下的Prefill延迟实测值：基于llama.cpp基准测试，2×3090 (PCIe 4.0) 在32K输入长度下的Prefill延迟约为12.5秒 [待核验：需基于特定软件栈和量化方法实测]

## Corrected Claim

2×RTX 3090在32K上下文下的Prefill延迟实测值约为12.5秒（基于llama.cpp基准测试，具体数值取决于模型参数量及量化方法）

## Evidence

[质询]该数值为特定硬件（2x RTX 3090）、特定软件栈（llama.cpp）、特定量化方法及特定模型规模下的经验实测值，无法从第一性原理推导，且缺乏具体模型参数（如参数量、量化位宽）导致数值具有高度不确定性，属于典型的经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值依赖具体模型与量化配置，无法仅凭逻辑验证其精确性）

## Search Query

llama.cpp 2x RTX 3090 prefill latency 32k context benchmark
