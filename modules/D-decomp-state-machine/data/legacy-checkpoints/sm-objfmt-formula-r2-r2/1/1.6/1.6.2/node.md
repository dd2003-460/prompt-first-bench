# N59: AMD Threadripper PRO 7000 WX 系列（如 7995WX）支持 8通道 DDR5-4800 ECC 内存，理论峰值带宽为 307.2 G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

AMD Threadripper PRO 7000 WX 系列（如 7995WX）支持 8通道 DDR5-4800 ECC 内存，理论峰值带宽为 307.2 GB/s (8 channels x 4800 MT/s x 8 bytes / 8)。

## Corrected Claim

AMD Threadripper PRO 7000 WX 系列（如 7995WX）支持 8通道 DDR5-4800 ECC 内存，理论峰值带宽为 307.2 GB/s (8 channels x 4800 MT/s x 8 bytes / 8)。

## Evidence

先验知识/题面给定，逻辑校验通过：AMD Threadripper PRO 7000系列（基于Zen 4架构）确实支持8通道DDR5内存，官方规格中DDR5-4800为支持频率之一，带宽计算 8 * 4800 * 8 / 8 = 307.2 GB/s 正确。
