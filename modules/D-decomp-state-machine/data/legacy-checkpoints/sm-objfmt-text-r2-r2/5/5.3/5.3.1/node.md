# N92: 2x RTX 4090 通过 PCIe Gen4 x16 互联，单向带宽约 25 GB/s，双向约 50 GB/s，远低于 NVLink 的 900 GB/s，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

2x RTX 4090 通过 PCIe Gen4 x16 互联，单向带宽约 25 GB/s，双向约 50 GB/s，远低于 NVLink 的 900 GB/s，导致张量并行 (TP=2) 时 AllReduce 通信成为主要瓶颈。

## Corrected Claim

2x RTX 4090 通过 PCIe Gen4 x16 互联，单向带宽约 25 GB/s，双向约 50 GB/s，远低于 NVLink 的 900 GB/s，导致张量并行 (TP=2) 时 AllReduce 通信成为主要瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe Gen4 x16 单向理论带宽约为 31.5 GB/s，实际有效带宽约 25 GB/s，双向约 50 GB/s，与 NVLink 的高带宽相比确实构成显著瓶颈，符合硬件规格常识。
