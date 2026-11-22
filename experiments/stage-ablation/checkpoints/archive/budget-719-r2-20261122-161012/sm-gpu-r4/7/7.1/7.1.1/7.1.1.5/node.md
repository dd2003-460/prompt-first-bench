# N647: N267 (RTX 4090 + CPU Offload) 的替代方案对比：若使用 Threadripper PRO 平台 (N309 提及)，CPU 内存带宽

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N265, N266, N267

## Claim

N267 (RTX 4090 + CPU Offload) 的替代方案对比：若使用 Threadripper PRO 平台 (N309 提及)，CPU 内存带宽提升至 400+ GB/s (8通道 DDR5)，但 PCIe 带宽仍为瓶颈；若改用 NVLink 或多卡 P2P (如 2x 4090 P2P 禁用后走 PCIe)，Offload 延迟无本质改善。唯一能显著降低 Offload 延迟的是使用统一内存架构 (如 Mac Studio M2 Ultra, N334)，其内存带宽 800 GB/s 直接服务于 GPU，消除 PCIe 瓶颈，但硬件成本结构完全不同。

## Corrected Claim

N267 (RTX 4090 + CPU Offload) 的替代方案对比：若使用 Threadripper PRO 平台 (N309 提及)，CPU 内存带宽提升至 400+ GB/s (8通道 DDR5)，但 PCIe 带宽仍为瓶颈；若改用 NVLink 或多卡 P2P (如 2x 4090 P2P 禁用后走 PCIe)，Offload 延迟无本质改善。唯一能显著降低 Offload 延迟的是使用统一内存架构 (如 Mac Studio M2 Ultra, N334)，其内存带宽 800 GB/s 直接服务于 GPU，消除 PCIe 瓶颈，但硬件成本结构完全不同。

## Evidence

先验知识/题面给定，逻辑校验通过：Threadripper PRO 8通道DDR5带宽确实在400GB/s以上，Mac Studio M2 Ultra统一内存带宽确认为800GB/s，且统一内存架构消除PCIe瓶颈符合硬件架构原理。

## Search Query

Threadripper PRO vs Mac Studio M2 Ultra LLM offload performance comparison
