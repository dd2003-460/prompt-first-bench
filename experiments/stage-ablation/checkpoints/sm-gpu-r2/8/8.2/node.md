# N157: A100 80GB (PCIe) 相比 SXM 版本的性能差异：PCIe 版本互联带宽为 64 GB/s，SXM 版本为 600 GB/s (NVLink)，单

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

A100 80GB (PCIe) 相比 SXM 版本的性能差异：PCIe 版本互联带宽为 64 GB/s，SXM 版本为 600 GB/s (NVLink)，单卡推理性能差异 <5% (因单卡无互联需求)，但多卡扩展时 PCIe 版本吞吐量下降 30-50%。

## Corrected Claim

A100 80GB (PCIe) 相比 SXM 版本的性能差异：PCIe 版本互联带宽为 64 GB/s，SXM 版本为 600 GB/s (NVLink)，单卡推理性能差异 <5% (因单卡无互联需求)，但多卡扩展时 PCIe 版本吞吐量下降 30-50%。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 PCIe版NVLink带宽确为64GB/s，SXM版为600GB/s；单卡推理不依赖卡间互联，性能差异极小；多卡扩展时PCIe带宽瓶颈导致吞吐量显著下降，符合硬件架构常识。
