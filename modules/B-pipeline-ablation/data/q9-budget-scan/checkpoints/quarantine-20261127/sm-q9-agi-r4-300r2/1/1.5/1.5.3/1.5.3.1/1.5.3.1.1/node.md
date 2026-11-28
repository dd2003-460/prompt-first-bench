# N287: V100-SXM2-16GB 的实际 HBM2 峰值带宽为 900 GB/s (官方规格)，在 TP=4 模式下，由于 NVLink 互联带宽 (300 GB/

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N115, N116, N117

## Claim

V100-SXM2-16GB 的实际 HBM2 峰值带宽为 900 GB/s (官方规格)，在 TP=4 模式下，由于 NVLink 互联带宽 (300 GB/s/卡) 低于 HBM 带宽，AllReduce 通信引入的等效带宽损耗系数 η_comm ≈ 0.85，导致有效聚合带宽降至约 765 GB/s，使得理论 Memory-Bound 吞吐上限从 900k tok/s 修正为 ~765k tok/s (仍远高于实际 45 tok/s，证明非带宽绝对瓶颈而是延迟/调度瓶颈)。

## Corrected Claim

V100-SXM2-16GB 的 HBM2 峰值带宽为 900 GB/s。在 TP=4 模式下，受限于 NVLink 互联带宽及通信开销，有效带宽会低于 HBM 峰值带宽，导致理论 Memory-Bound 吞吐上限显著降低（例如降至数百 k tok/s 量级），但仍远高于实际观测到的 45 tok/s，表明主要瓶颈在于延迟或调度而非绝对带宽。

## Evidence

[质询]NVLink 互联带宽数值存疑：V100 SXM2 的 NVLink 总带宽通常为 300 GB/s（双向聚合），但 AllReduce 在 TP=4 下的等效带宽损耗系数 η_comm ≈ 0.85 是一个高度依赖具体实现（如 NCCL 算法、拓扑、消息大小）的经验估算值，并非固定物理常数；此外，将 HBM 带宽直接乘以该系数得到“有效聚合带宽”并进而线性推导吞吐上限，忽略了计算与通信重叠（overlap）的可能性以及 Kernel Launch 等固定开销，逻辑链条过于简化。 | 先验知识/题面给定，逻辑校验通过（量级合理，V100 HBM2 带宽确为 900 GB/s，NVLink 带宽量级正确，但 η_comm 为经验估算值，缺乏通用性保证，故降级为定性表述）

## Search Query

Tesla V100 SXM2 HBM2 bandwidth spec NVLink bandwidth TP4 efficiency
