# N242: Apple M3 Ultra 实际内存带宽利用率系数 (η) 为 0.75-0.85，基于 Apple Silicon 统一内存架构及 llama.cpp/Me

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N92

## Claim

Apple M3 Ultra 实际内存带宽利用率系数 (η) 为 0.75-0.85，基于 Apple Silicon 统一内存架构及 llama.cpp/Metal 后端在 LLM Decode 阶段（小批量、高延迟敏感）的实测数据，用于修正理论峰值 800 GB/s 以计算有效吞吐。

## Corrected Claim

Apple M3 Ultra 在 LLM Decode 阶段的实际内存带宽利用率系数 (η) 估计在 0.75-0.85 之间，该数值基于 Apple Silicon 统一内存架构及 llama.cpp/Metal 后端的典型实测表现，用于修正理论峰值 800 GB/s 以估算有效吞吐。

## Evidence

[质询]该数值（0.75-0.85）属于特定硬件与软件栈组合下的经验性实测数据，无法从第一性原理或数学公理中严格推导得出，且缺乏公开权威基准测试的直接引用支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Apple M3 Ultra llama.cpp effective memory bandwidth utilization LLM decode
