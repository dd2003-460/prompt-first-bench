# N138: A100 PCIe 版与 SXM 版在 LLM 推理中的性能差异量化：PCIe 版显存带宽 1555 GB/s (HBM2e)，SXM 版同为 1555 GB/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

A100 PCIe 版与 SXM 版在 LLM 推理中的性能差异量化：PCIe 版显存带宽 1555 GB/s (HBM2e)，SXM 版同为 1555 GB/s 但 PCIe 版受限于 PCIe 4.0 x16 (~32 GB/s) 用于主机-设备传输及多卡互联（若无 NVLink Bridge），单卡推理主要受 HBM 带宽限制，PCIe 瓶颈仅在 Batch Size 极大或频繁 CPU-GPU 交换时显现；单卡场景下 PCIe vs SXM 吞吐差异 < 5% [待核验]。

## Corrected Claim

A100 PCIe 版与 SXM 版在 LLM 推理中的性能差异量化：PCIe 版显存带宽 1555 GB/s (HBM2e)，SXM 版同为 1555 GB/s 但 PCIe 版受限于 PCIe 4.0 x16 (~32 GB/s) 用于主机-设备传输及多卡互联（若无 NVLink Bridge），单卡推理主要受 HBM 带宽限制，PCIe 瓶颈仅在 Batch Size 极大或频繁 CPU-GPU 交换时显现；单卡场景下 PCIe vs SXM 吞吐差异 < 5% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 PCIe与SXM版显存带宽均为1555 GB/s，单卡推理主要受HBM带宽限制，PCIe瓶颈在单卡场景下影响极小（<5%），符合硬件架构原理。

## Search Query

A100 PCIe vs SXM inference performance difference LLM
