# N562: Intel Arc A770 在 llama.cpp Vulkan 后端下的实测 Decode 吞吐量（Q4_K_M, 32K ctx）在公开基准中无直接数据，

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N195

## Claim

Intel Arc A770 在 llama.cpp Vulkan 后端下的实测 Decode 吞吐量（Q4_K_M, 32K ctx）在公开基准中无直接数据，基于内存带宽限制估算：若权重部分卸载，有效带宽受限于 PCIe 而非显存带宽，理论上限 1.5-2.0 tokens/s；若强制使用 Q3_K_M (13.5GB) 以适配 16GB 显存（KV Cache 需 INT8 或更小），理论上限可达 512 GB/s / (13.5GB + 4GB KV) ≈ 29 tokens/s，但实测受 Vulkan 驱动效率（~0.6x）影响，预计 17-18 tokens/s。

## Corrected Claim

Intel Arc A770 在 llama.cpp Vulkan 后端下的实测 Decode 吞吐量（Q4_K_M, 32K ctx）在公开基准中无直接数据。基于内存带宽限制估算：若权重部分卸载，有效带宽受限于 PCIe，理论上限约为 1.5-2.0 tokens/s；若强制使用 Q3_K_M 以适配 16GB 显存，理论上限可达约 29 tokens/s，但实际性能受 Vulkan 驱动效率影响，预计显著低于理论值。

## Evidence

[质询]该陈述包含具体的经验性参数（如Vulkan驱动效率系数~0.6x、KV Cache具体占用4GB、Q3_K_M模型大小13.5GB），这些并非第一性原理可推导的数学或物理常数，而是依赖于特定硬件、驱动版本和软件实现的实测经验值。在缺乏直接来源支持的情况下，将其作为确定的理论上限或预计值存在不确定性。 | 逻辑推导过程自洽（带宽/数据量=吞吐量），但关键经验参数（驱动效率、KV大小）缺乏来源支持，属于经验事实，依据规则降级。

## Search Query

llama.cpp Vulkan Intel Arc A770 Q4_K_M decode speed benchmark
