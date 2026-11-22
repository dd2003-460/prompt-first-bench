# N172: 消费级主板 (如 Z790/X670E) 的 PCIe P2P 支持状态矩阵：Intel 平台 (Z790) 通常通过 IOMMU 支持 P2P，但需手动启用 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

消费级主板 (如 Z790/X670E) 的 PCIe P2P 支持状态矩阵：Intel 平台 (Z790) 通常通过 IOMMU 支持 P2P，但需手动启用 BIOS 选项 (IOMMU/VT-d) 并配置 IOMMU Group，否则数据经 CPU 中转；AMD 平台 (X670E) 对 P2P 支持更友好，多数主板默认启用，但需确认 CPU 是否支持 ACS (Access Control Services) 绕过；若 P2P 未启用，跨卡通信带宽从 PCIe 4.0 x16 (~32 GB/s) 降至 PCIe 3.0 x4 或更低 (~4-8 GB/s)，导致 TP=2 的通信延迟增加 4-8 倍，使有效吞吐量下降至单卡的 60-70% 水平，因此部署前必须通过 `lspci -vv | grep P2P` 或 `nvidia-smi topo -m` 验证 P2P 状态。

## Corrected Claim

消费级主板 (如 Z790/X670E) 的 PCIe P2P 支持状态需手动验证：Intel 平台 (Z790) 通常需手动启用 BIOS 中的 IOMMU/VT-d 选项并配置 IOMMU Group 以支持 P2P，否则数据经 CPU 中转；AMD 平台 (X670E) 对 P2P 支持相对友好，但需确认 ACS (Access Control Services) 状态。若 P2P 未启用，跨卡通信带宽将从 PCIe 4.0 x16 (~32 GB/s) 显著降低（可能降至 PCIe 3.0 x4 或更低，约 4-8 GB/s），导致 TP=2 场景下通信成为瓶颈，有效吞吐量可能大幅下降（具体比例取决于模型架构与负载，通常显著低于理想 P2P 状态）。部署前必须通过 `lspci -vv | grep P2P` 或 `nvidia-smi topo -m` 验证 P2P 状态。

## Evidence

[质询]数值量级与因果归因存在严重偏差：1. 带宽下降幅度描述错误，PCIe 4.0 x16 (~32GB/s) 降至 PCIe 3.0 x4 (~4GB/s) 是约 8 倍差距，而非陈述中暗示的线性对应；2. 'TP=2 通信延迟增加 4-8 倍' 缺乏理论依据，P2P 失效通常导致带宽瓶颈而非单纯延迟倍增，且延迟与带宽在通信模型中是不同维度；3. '有效吞吐量下降至单卡的 60-70%' 是高度依赖具体模型（如 Transformer 层数、Batch Size）的经验值，并非通用物理/工程常数，将其作为绝对结论缺乏严谨性。 | 经验事实，逻辑自洽但缺来源支持；且部分数值推导（如延迟倍数、吞吐量比例）过于绝对，未考虑具体负载场景，故降级为定性表述。

## Search Query

consumer motherboard PCIe peer to peer support Intel AMD LLM multi-GPU
