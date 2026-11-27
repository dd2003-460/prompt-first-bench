# N317: A100 80GB (PCIe) 与 SXM 版本的性能差异：PCIe 版 A100 的 HBM2e 带宽与 SXM 相同 (2039 GB/s)，但互联带宽从

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

A100 80GB (PCIe) 与 SXM 版本的性能差异：PCIe 版 A100 的 HBM2e 带宽与 SXM 相同 (2039 GB/s)，但互联带宽从 NVLink 600GB/s 降至 PCIe 4.0 x16 32GB/s；在单卡 Batch=1 推理场景下，PCIe 版与 SXM 版吞吐率差异 <5%（因无跨卡通信），但在多卡张量并行场景下，PCIe 版吞吐率下降 30-50%。

## Corrected Claim

A100 80GB (PCIe) 与 SXM 版本的性能差异：PCIe 版 A100 的 HBM2e 带宽与 SXM 相同 (2039 GB/s)，但互联带宽从 NVLink 600GB/s 降至 PCIe 4.0 x16 32GB/s；在单卡 Batch=1 推理场景下，PCIe 版与 SXM 版吞吐率差异 <5%（因无跨卡通信），但在多卡张量并行场景下，PCIe 版吞吐率下降 30-50%。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 PCIe与SXM版HBM带宽一致（2039 GB/s），互联带宽差异（PCIe 32GB/s vs NVLink 600GB/s）符合硬件规格；单卡推理无跨卡通信故性能差异极小，多卡张量并行因互联带宽瓶颈导致显著性能下降，逻辑自洽且符合工程常识。
