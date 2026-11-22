# N692: 4x RTX 4090 多卡系统的主板 (ASUS Pro WS WRX80E-SAGE SE, ~$2,500) 支持 4 条 PCIe 4.0 x16 插槽

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N214

## Claim

4x RTX 4090 多卡系统的主板 (ASUS Pro WS WRX80E-SAGE SE, ~$2,500) 支持 4 条 PCIe 4.0 x16 插槽，但实际带宽受限于 CPU 直连 PCIe lanes (AMD Threadripper PRO 7995WX 提供 128 条 PCIe 5.0 lanes)，4 张 4090 需占用 64 条 lanes，剩余 64 条用于 NVMe/网卡，无带宽瓶颈。

## Corrected Claim

4x RTX 4090 多卡系统的主板 (ASUS Pro WS WRX80E-SAGE SE, ~$2,500) 支持 4 条 PCIe 4.0 x16 插槽，但实际带宽受限于 CPU 直连 PCIe lanes (AMD Threadripper PRO 7995WX 提供 128 条 PCIe 5.0 lanes)，4 张 4090 需占用 64 条 lanes，剩余 64 条用于 NVMe/网卡，无带宽瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：Threadripper PRO 7995WX 确实提供 128 条 PCIe 5.0 lanes，4 张 RTX 4090 占用 64 条 lanes 在物理上可行且无带宽瓶颈，主板规格与 CPU 能力匹配。
