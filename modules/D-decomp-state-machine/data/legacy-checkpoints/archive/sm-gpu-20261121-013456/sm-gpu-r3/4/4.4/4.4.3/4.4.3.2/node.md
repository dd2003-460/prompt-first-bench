# N213: A100 (SXM/PCIe) 在 INT4 量化推理下的理论带宽上限为 2039 GB/s，但受限于 PCIe 4.0 x16 接口 (32 GB/s) 及内

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

A100 (SXM/PCIe) 在 INT4 量化推理下的理论带宽上限为 2039 GB/s，但受限于 PCIe 4.0 x16 接口 (32 GB/s) 及内核启动开销，实际有效带宽利用率约为 60-70%，导致实测吞吐量 (tokens/s) 显著低于基于纯显存带宽的计算值。

## Corrected Claim

A100 SXM 的 HBM2e 显存带宽为 2039 GB/s，A100 PCIe 版本为 1935 GB/s。在 INT4 量化推理中，若数据需通过 PCIe 4.0 x16 接口（约 32 GB/s）传输，则实际有效带宽受限于 PCIe 接口，利用率约为 60-70%，导致实测吞吐量显著低于基于显存带宽的计算值。

## Evidence

[质询]数值量级与硬件规格存在明显矛盾：A100 SXM 的 HBM2e 显存带宽为 2039 GB/s，但 A100 PCIe 版本的显存带宽仅为 1935 GB/s（HBM2e 降频或不同配置），且两者均远高于 PCIe 4.0 x16 的 32 GB/s。陈述将 '2039 GB/s' 笼统归为 A100 (SXM/PCIe) 的理论带宽上限，混淆了 SXM 和 PCIe 版本的显存带宽差异；更关键的是，若推理瓶颈确为 PCIe 接口（32 GB/s），则理论上限应为 32 GB/s 而非 2039 GB/s，此处将显存带宽误标为受 PCIe 限制下的'理论带宽上限'，逻辑上存在概念混淆。 | 先验知识/题面给定，逻辑校验未通过：A100 SXM 显存带宽 2039 GB/s 正确，但 A100 PCIe 显存带宽为 1935 GB/s，且 PCIe 4.0 x16 带宽约 32 GB/s。陈述将显存带宽（2039 GB/s）与 PCIe 接口带宽（32 GB/s）混为一谈，称前者为'受限于 PCIe 接口'的理论上限，逻辑不自洽。
