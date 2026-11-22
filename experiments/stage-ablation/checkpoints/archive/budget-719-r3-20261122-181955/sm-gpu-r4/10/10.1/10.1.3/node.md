# N367: 2x RTX 4090 在 32K 上下文 Prefill 阶段的实际吞吐量损失估算：理论计算时间（基于 N92 公式修正为双卡并行）≈ 0.67s，通信时间 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N123

## Claim

2x RTX 4090 在 32K 上下文 Prefill 阶段的实际吞吐量损失估算：理论计算时间（基于 N92 公式修正为双卡并行）≈ 0.67s，通信时间 0.512s，总时间 ≈ 1.18s；单卡 A100 理论 Prefill 时间 ≈ 0.18s（N92 数据）；因此 2x 4090 的 Prefill 延迟比 A100 高约 6.5 倍，主要源于 PCIe 带宽瓶颈及较低的单卡算力。

## Corrected Claim

2x RTX 4090 在 32K 上下文 Prefill 阶段的实际吞吐量损失估算：理论计算时间（基于 N92 公式修正为双卡并行）≈ 0.67s，通信时间 0.512s，总时间 ≈ 1.18s；单卡 A100 理论 Prefill 时间 ≈ 0.18s（N92 数据）；因此 2x 4090 的 Prefill 延迟比 A100 高约 6.5 倍，主要源于 PCIe 带宽瓶颈及较低的单卡算力。

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 4090 受限于 PCIe 带宽（~32GB/s）及较低单卡算力，在 32K 长上下文 Prefill 阶段，通信开销（0.512s）与计算时间（0.67s）叠加导致总延迟（1.18s）显著高于单卡 A100（0.18s），6.5 倍的延迟差异符合硬件性能量级与并行通信瓶颈的物理直觉。
