# N99: H100 SXM5 的标称显存带宽为 3352 GB/s（HBM3），H100 PCIe 版本的标称显存带宽同样为 3352 GB/s，显存子系统无差异，但 P

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

H100 SXM5 的标称显存带宽为 3352 GB/s（HBM3），H100 PCIe 版本的标称显存带宽同样为 3352 GB/s，显存子系统无差异，但 PCIe 版在大规模分布式推理中互联效率较低 [待核验]。

## Corrected Claim

H100 SXM5 的标称显存带宽为 3352 GB/s（HBM3），而 H100 PCIe 版本通常配备 HBM2e，标称显存带宽约为 2039 GB/s（80GB版）或 2039 GB/s（40GB版），显存子系统存在显著差异，且 PCIe 版在大规模分布式推理中互联效率较低。

## Evidence

[质询]H100 PCIe 版本通常配备 HBM2e 而非 HBM3，且其显存容量和带宽通常低于 SXM5 版本（SXM5 为 80GB HBM3 @ 3.35TB/s，PCIe 常见为 80GB HBM2e @ 2.0TB/s 或 40GB HBM2e @ 2.0TB/s），声称两者带宽均为 3352 GB/s 且显存子系统无差异与主流硬件规格不符。 | 先验知识/题面给定，逻辑校验发现数值与已知硬件规格矛盾（PCIe版通常非HBM3且带宽较低），故降级。

## Search Query

H100 SXM5 vs PCIe memory bandwidth GB/s
