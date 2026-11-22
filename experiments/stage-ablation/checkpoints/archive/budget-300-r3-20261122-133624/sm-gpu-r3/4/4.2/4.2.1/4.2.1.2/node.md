# N309: Resizable BAR (ReBAR) 开启对 P2P DMA 带宽的影响量化：在 AMD 平台（如 X670E），开启 ReBAR 后，P2P DMA 有

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N100

## Claim

Resizable BAR (ReBAR) 开启对 P2P DMA 带宽的影响量化：在 AMD 平台（如 X670E），开启 ReBAR 后，P2P DMA 有效带宽从默认的 ~30-40 GB/s（受限于 IOMMU 分组）提升至接近 PCIe 链路理论值（PCIe 4.0 x16 ~32 GB/s，PCIe 5.0 x16 ~64 GB/s）；在 Intel 平台（如 Z790），ReBAR 对 P2P 影响较小，主要受 ACS 控制，带宽提升幅度 < 10% [待核验：需实测不同平台 ReBAR 对 P2P 带宽的具体增益]，若未开启 ReBAR 且 ACS 未关闭，TP=2 通信延迟增加 3-5 倍，导致端到端推理吞吐量下降 15-25%（基于 N100 的通信延迟增量估算）

## Corrected Claim

Resizable BAR (ReBAR) 开启通常有助于提升 P2P DMA 带宽，使其更接近 PCIe 链路理论值；在 AMD 平台（如 X670E）上，开启 ReBAR 可能显著改善 P2P 性能，而在 Intel 平台（如 Z790）上，P2P 性能主要受 ACS 控制，ReBAR 的边际增益可能较小。具体带宽增益和延迟/吞吐量影响因硬件配置、IOMMU/ACS 设置及驱动版本而异，需实测确定。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如带宽从30-40GB/s提升至理论值、延迟增加3-5倍、吞吐量下降15-25%），这些具体参数值属于经验事实，无法从第一性原理严格推导，且缺乏实测数据支持。此外，'P2P DMA有效带宽受限于IOMMU分组'这一归因在技术细节上可能存在简化或混淆（通常P2P性能主要受限于ACS、IOMMU隔离策略及硬件拓扑，而非单纯的IOMMU分组数量），且不同平台（AMD vs Intel）的具体增益幅度差异极大，缺乏统一标准。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且具体数值无法从第一性原理推出）

## Search Query

Resizable BAR impact on P2P DMA bandwidth AMD vs Intel PCIe 4.0 5.0
