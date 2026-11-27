# N308: 2×RTX 4090 双卡互联带宽为 PCIe 4.0 x16 双向 ~32 GB/s，而单卡显存带宽为 1008 GB/s，带宽比为 32/1008 ≈ 3.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N127

## Claim

2×RTX 4090 双卡互联带宽为 PCIe 4.0 x16 双向 ~32 GB/s，而单卡显存带宽为 1008 GB/s，带宽比为 32/1008 ≈ 3.2%，导致 KV Cache 跨卡传输成为主要瓶颈，尤其在长上下文场景下通信开销占比显著增加。

## Corrected Claim

2×RTX 4090 双卡互联带宽为 PCIe 4.0 x16 双向 ~32 GB/s，而单卡显存带宽为 1008 GB/s，带宽比为 32/1008 ≈ 3.2%，导致 KV Cache 跨卡传输成为主要瓶颈，尤其在长上下文场景下通信开销占比显著增加。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s 与 PCIe 4.0 x16 双向带宽 ~32 GB/s 均为标准硬件规格，比值计算正确，符合长上下文下 KV Cache 传输瓶颈的工程常识。

## Search Query

PCIe 4.0 x16 bandwidth GB/s vs GPU memory bandwidth ratio
