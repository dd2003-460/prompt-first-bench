# N381: 1×RTX 4090在32K上下文下的Prefill延迟实测值：基于llama.cpp基准测试，1×4090在32K输入长度下的Prefill延迟约为8.2秒 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N129

## Claim

1×RTX 4090在32K上下文下的Prefill延迟实测值：基于llama.cpp基准测试，1×4090在32K输入长度下的Prefill延迟约为8.2秒 [待核验：需基于特定软件栈和量化方法实测]

## Corrected Claim

1×RTX 4090在32K上下文下的Prefill延迟实测值高度依赖于模型规模与量化方法；在llama.cpp基准测试中，针对特定中等规模模型（如7B-13B级别）的量化版本，Prefill延迟可能在数秒至数十秒之间波动，8.2秒仅为特定配置下的参考值。

## Evidence

[质询]该数值为特定硬件（RTX 4090）、特定软件栈（llama.cpp）、特定模型（未指明，通常默认为Llama-2/3 7B/13B/70B等）及特定量化方式（如Q4_K_M）下的经验实测值，属于硬件性能与软件优化相关的经验事实，无法从第一性原理推导，且不同模型尺寸和量化精度会导致延迟差异巨大（例如7B模型可能远低于8.2秒，70B模型可能远高于8.2秒），缺乏具体上下文导致数值具有高度不确定性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值依赖未指定的模型规模与量化参数，无法通过第一性原理验证）。

## Search Query

llama.cpp 1x RTX 4090 prefill latency 32k context benchmark
