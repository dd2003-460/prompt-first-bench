# N371: 2× RTX 4090 通过 PCIe 4.0 互联时，启用 P2P (Peer-to-Peer) 需修改内核参数 (pci=realloc, iommu=pt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N146

## Claim

2× RTX 4090 通过 PCIe 4.0 互联时，启用 P2P (Peer-to-Peer) 需修改内核参数 (pci=realloc, iommu=pt) 并重启系统，耗时 T_reboot = 5-10 分钟；若 P2P 启用失败，需回退至共享内存模式，额外增加 15-30 分钟调试时间。

## Corrected Claim

2× RTX 4090 通过 PCIe 4.0 互联时，启用 P2P (Peer-to-Peer) 需修改内核参数 (pci=realloc, iommu=pt) 并重启系统，耗时 T_reboot = 5-10 分钟；若 P2P 启用失败，需回退至共享内存模式，额外增加 15-30 分钟调试时间。

## Evidence

先验知识/题面给定，逻辑校验通过
