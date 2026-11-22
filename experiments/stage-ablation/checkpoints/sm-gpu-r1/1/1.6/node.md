# N12: CPU 内存卸载（Offloading）方案可行性：若显存不足，将部分层卸载至 CPU 内存，带宽瓶颈导致推理速度下降 50-200 倍，仅适用于离线批处理，不

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

CPU 内存卸载（Offloading）方案可行性：若显存不足，将部分层卸载至 CPU 内存，带宽瓶颈导致推理速度下降 50-200 倍，仅适用于离线批处理，不满足实时交互需求，因此排除纯 CPU 或重度 Offload 方案作为主要推荐。

## Corrected Claim

CPU 内存卸载（Offloading）方案可行性：若显存不足，将部分层卸载至 CPU 内存，带宽瓶颈导致推理速度下降 50-200 倍，仅适用于离线批处理，不满足实时交互需求，因此排除纯 CPU 或重度 Offload 方案作为主要推荐。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe带宽远低于显存带宽，导致CPU卸载推理速度大幅下降，符合物理直觉与工程常识

## Search Query

GPU CPU offloading inference speed penalty LLM
