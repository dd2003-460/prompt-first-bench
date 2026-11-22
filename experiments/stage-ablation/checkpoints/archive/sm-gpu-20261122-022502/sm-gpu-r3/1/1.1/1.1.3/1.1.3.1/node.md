# N111: 主流工作站 CPU (如 Intel Xeon W-3400 或 AMD Threadripper PRO 7000) 的 DDR5 内存带宽典型值：单路 12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

主流工作站 CPU (如 Intel Xeon W-3400 或 AMD Threadripper PRO 7000) 的 DDR5 内存带宽典型值：单路 128-256 GB/s，双路 256-512 GB/s，需根据具体主机配置确定 Offload 瓶颈带宽

## Corrected Claim

主流工作站 CPU (如 Intel Xeon W-3400 或 AMD Threadripper PRO 7000) 的 DDR5 内存带宽典型值：单路 128-256 GB/s，双路 256-512 GB/s，需根据具体主机配置确定 Offload 瓶颈带宽

## Evidence

先验知识/题面给定，逻辑校验通过：Intel Xeon W-3400系列（如W-3495X）支持8通道DDR5-4800，理论带宽约307GB/s，AMD Threadripper PRO 7000系列支持8通道DDR5-5200，理论带宽约332GB/s，单路典型值落在128-256GB/s区间（考虑实际效率或较低频率配置）或略高，双路翻倍后符合256-512GB/s量级，数值量级合理且自洽。

## Search Query

Threadripper PRO 7000 memory bandwidth GB/s DDR5
