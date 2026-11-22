# N46: Apple M2 Ultra 的内存子系统架构为双 M1 Ultra 芯片通过 UltraFusion 互联，总带宽 800 GB/s (400 GB/s pe

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

Apple M2 Ultra 的内存子系统架构为双 M1 Ultra 芯片通过 UltraFusion 互联，总带宽 800 GB/s (400 GB/s per chip)，该带宽是 LLM 推理 Decode 阶段（Memory-Bound）的吞吐上限决定因素，需对比 NVIDIA HBM/GDDR 带宽评估其相对劣势。

## Corrected Claim

Apple M2 Ultra 的内存子系统架构为双 M1 Ultra 芯片通过 UltraFusion 互联，总带宽 800 GB/s (400 GB/s per chip)，该带宽是 LLM 推理 Decode 阶段（Memory-Bound）的吞吐上限决定因素，需对比 NVIDIA HBM/GDDR 带宽评估其相对劣势。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 确由双 M1 Ultra 通过 UltraFusion 互联，总带宽 800GB/s 符合 Apple 官方规格；LLM Decode 阶段受内存带宽限制（Memory-Bound）符合计算密集型与内存密集型任务的基本原理。

## Search Query

Apple M2 Ultra UltraFusion memory bandwidth 800GB/s architecture
