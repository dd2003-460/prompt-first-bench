# N58: PCIe 互联带宽限制：PCIe Gen4 x16 单向带宽为 32 GB/s，双向为 64 GB/s；多卡 All-Reduce 通信需双向传输，有效通信带宽

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

PCIe 互联带宽限制：PCIe Gen4 x16 单向带宽为 32 GB/s，双向为 64 GB/s；多卡 All-Reduce 通信需双向传输，有效通信带宽为 32 GB/s，此值决定了多卡并行时的通信延迟下限。

## Corrected Claim

PCIe 互联带宽限制：PCIe Gen4 x16 单向带宽为 32 GB/s，双向为 64 GB/s；多卡 All-Reduce 通信需双向传输，有效通信带宽为 32 GB/s，此值决定了多卡并行时的通信延迟下限。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe Gen4 x16 单向带宽约 32 GB/s，双向 64 GB/s，多卡 All-Reduce 通信需双向传输，有效通信带宽为 32 GB/s，符合基本物理/工程直觉。
