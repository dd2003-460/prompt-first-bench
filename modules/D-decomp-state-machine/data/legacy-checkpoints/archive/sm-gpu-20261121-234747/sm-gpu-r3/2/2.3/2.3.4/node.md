# N80: NVFP4 (NVIDIA 4-bit floating point) 仅在 Blackwell 架构 (如 RTX 5090, B100/B200) 上获得原

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12, N13, N14

## Claim

NVFP4 (NVIDIA 4-bit floating point) 仅在 Blackwell 架构 (如 RTX 5090, B100/B200) 上获得原生 Tensor Core 支持，提供 4x 于 BF16 的理论算力密度；在 Ada (RTX 4090) 或 Ampere (RTX 3090) 上运行 NVFP4 需完全软件模拟，性能惩罚系数预计 > 5x [待核验：需确认 Ada 架构对 FP4 的软件模拟效率]。

## Corrected Claim

NVFP4 (NVIDIA 4-bit floating point) 仅在 Blackwell 架构 (如 RTX 5090, B100/B200) 上获得原生 Tensor Core 支持，提供 4x 于 BF16 的理论算力密度；在 Ada (RTX 4090) 或 Ampere (RTX 3090) 上运行 NVFP4 需依赖软件模拟或低效的混合精度路径，性能显著低于原生支持架构，具体惩罚系数因实现方式而异，通常远高于原生性能。

## Evidence

[质询]NVFP4 是 NVIDIA 专有的 4-bit 浮点格式，其硬件加速依赖于 Blackwell 架构中特定的 Tensor Core 指令集。在 Ada/Ampere 架构上，由于缺乏原生硬件支持，所谓的“软件模拟”通常指通过 FP16/BF16 的多次运算或查表法来近似，其性能惩罚系数是否严格大于 5x 缺乏公开的基准测试数据支持，且“完全软件模拟”这一表述可能过于绝对（可能存在部分硬件辅助的混合精度路径，尽管效率极低）。此外，4x 于 BF16 的理论算力密度是基于理想吞吐量的对比，实际受限于内存带宽和精度转换开销，未必能线性体现。 | 经验事实，逻辑自洽但缺来源支持。NVFP4 为 Blackwell 专有特性，Ada/Ampere 无原生支持，需软件模拟，性能大幅下降符合硬件架构差异的基本逻辑，但具体惩罚系数 >5x 缺乏直接来源佐证。

## Search Query

NVFP4 support Ada Lovelace RTX 4090 software emulation performance overhead
