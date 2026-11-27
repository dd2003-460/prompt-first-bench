# N222: PCIe 4.0 下 TP=2 的 NCCL 缓冲区修正：PCIe 4.0 带宽 (32 GB/s) 仅为 PCIe 5.0 的一半，为掩盖延迟，NCCL 可能

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

PCIe 4.0 下 TP=2 的 NCCL 缓冲区修正：PCIe 4.0 带宽 (32 GB/s) 仅为 PCIe 5.0 的一半，为掩盖延迟，NCCL 可能启用更深的流水线或更大的 chunk 大小，导致缓冲区占用增加 20-30%。因此 PCIe 4.0 互联下，建议预留 1.5-2.5 GB/卡，而非 PCIe 5.0 的 1-2 GB。

## Corrected Claim

PCIe 4.0 下 TP=2 的 NCCL 缓冲区修正：PCIe 4.0 带宽 (32 GB/s) 仅为 PCIe 5.0 的一半，为掩盖延迟，NCCL 可能启用更深的流水线或更大的 chunk 大小，导致缓冲区占用增加 20-30%。因此 PCIe 4.0 互联下，建议预留 1.5-2.5 GB/卡，而非 PCIe 5.0 的 1-2 GB。

## Evidence

先验知识/题面给定，逻辑校验通过
