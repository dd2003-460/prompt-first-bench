# N48: Intel Arc A770 (16GB) 的显存带宽为 560 GB/s，TDP 225W；其 LLM 推理支持主要依赖 IPEX 或 llama.cpp 的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

Intel Arc A770 (16GB) 的显存带宽为 560 GB/s，TDP 225W；其 LLM 推理支持主要依赖 IPEX 或 llama.cpp 的 Vulkan/ONEAPI 后端，需核实其在 W4A16 量化下的实际吞吐量及驱动稳定性，以确认其是否值得作为消费级替代方案纳入候选集 [待核验]

## Corrected Claim

Intel Arc A770 (16GB) 的显存带宽约为 560 GB/s，TDP 为 225W；其 LLM 推理支持主要依赖 IPEX 或 llama.cpp 的 Vulkan/ONEAPI 后端，需进一步核实其在 W4A16 量化下的实际吞吐量及驱动稳定性，以确认其是否值得作为消费级替代方案纳入候选集。

## Evidence

[质询]该陈述包含具体的硬件规格（显存带宽 560 GB/s，TDP 225W）和软件生态现状（IPEX/llama.cpp 支持情况），属于经验事实。由于检索失败，无法通过外部来源直接验证这些具体数值和当前驱动/后端支持的稳定性，存在数值偏差或软件支持状态过时的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体硬件参数及软件生态现状）

## Search Query

Intel Arc A770 LLM inference benchmark llama.cpp Vulkan throughput stability
