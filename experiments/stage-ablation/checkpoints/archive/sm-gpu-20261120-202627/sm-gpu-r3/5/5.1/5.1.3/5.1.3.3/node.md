# N375: 2× RTX 4090 方案中 NVLink Bridge 的可选性分析：RTX 4090 不支持 NVLink，因此无法通过硬件桥接提升带宽，只能依赖 PCI

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

2× RTX 4090 方案中 NVLink Bridge 的可选性分析：RTX 4090 不支持 NVLink，因此无法通过硬件桥接提升带宽，只能依赖 PCIe 4.0 x16，这导致其在多卡并行下的通信开销远高于支持 NVLink 的架构，是性能瓶颈的根本原因。

## Corrected Claim

2× RTX 4090 方案中 NVLink Bridge 的可选性分析：RTX 4090 不支持 NVLink，因此无法通过硬件桥接提升带宽，只能依赖 PCIe 4.0 x16，这导致其在多卡并行下的通信开销远高于支持 NVLink 的架构，是性能瓶颈的根本原因。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 确实取消了 NVLink 支持，仅依赖 PCIe 4.0 x16 进行多卡通信，带宽远低于 NVLink，导致多卡并行通信开销大，逻辑自洽且符合硬件事实。
