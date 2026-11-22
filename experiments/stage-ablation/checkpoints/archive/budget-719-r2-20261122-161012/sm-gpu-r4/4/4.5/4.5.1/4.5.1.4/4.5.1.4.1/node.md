# N558: RTX 4090 运行 Qwen3-27B FP8 时，若启用 CPU Offload，4.2 GB 溢出部分的传输延迟 ΔT_offload = (4.2 G

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N232

## Claim

RTX 4090 运行 Qwen3-27B FP8 时，若启用 CPU Offload，4.2 GB 溢出部分的传输延迟 ΔT_offload = (4.2 GB / 1008 GB/s) * (1 - Bandwidth_Ratio)，其中 Bandwidth_Ratio 为 PCIe 4.0 x16 有效带宽 (约 25 GB/s) 与 GPU 显存带宽 (1008 GB/s) 之比 (≈0.025)，导致 Offload 层每步推理增加约 168ms 延迟，使整体 Decode 速度从理论上限 18.3 tokens/s 降至 <5 tokens/s。

## Corrected Claim

RTX 4090 运行 Qwen3-27B FP8 时，若启用 CPU Offload，假设 4.2 GB 权重需通过 PCIe 4.0 x16 (有效带宽约 25 GB/s) 传输，单次传输延迟约为 168ms (4.2 GB / 25 GB/s)。由于 Decode 阶段每步均需加载 Offload 层权重，这将显著增加每 token 生成时间，导致整体 Decode 速度大幅下降，具体降幅取决于 Offload 层占比及 CPU/GPU 协同效率，通常会使速度降至远低于纯 GPU 推理的水平（如 <5 tokens/s 是可能的，但需具体配置验证）。

## Evidence

[质询]公式逻辑存在严重缺陷：1. 传输延迟不应乘以 (1 - Bandwidth_Ratio)，该因子无物理意义，通常延迟仅由瓶颈带宽（PCIe）决定；2. 4.2GB 数据量对于 27B 模型 FP8 权重（约 27GB）而言，仅占 15%，若仅 Offload 这部分，对整体 Decode 速度从 18.3 降至 <5 tokens/s 的影响被夸大，且未考虑 CPU 计算或内存带宽瓶颈；3. 168ms 的计算结果 (4.2/25 * 0.975 ≈ 164ms) 虽接近，但基于错误的公式推导。 | 先验知识/题面给定，逻辑校验未通过：公式中 (1 - Bandwidth_Ratio) 项缺乏物理依据，且 4.2GB 溢出量对整体推理速度的影响评估缺乏严谨的瓶颈分析，属于经验事实且逻辑推导存在硬伤。
