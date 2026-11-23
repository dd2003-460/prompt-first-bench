# N202: 2x RTX 3090 方案中，由于不支持 NVLink，仅通过 PCIe 4.0 x16 (32 GB/s) 互联，多卡间通信开销极大，在 Tensor Pa

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

2x RTX 3090 方案中，由于不支持 NVLink，仅通过 PCIe 4.0 x16 (32 GB/s) 互联，多卡间通信开销极大，在 Tensor Parallelism 模式下几乎不可行，必须采用 Pipeline Parallelism (PP=2)，流水线气泡导致吞吐量损失约 20-30%。

## Corrected Claim

2x RTX 3090 方案中，由于不支持 NVLink，仅通过 PCIe 4.0 x16 (32 GB/s) 互联，多卡间通信开销极大，在 Tensor Parallelism 模式下几乎不可行，必须采用 Pipeline Parallelism (PP=2)，流水线气泡导致吞吐量损失约 20-30%。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 确实不支持 NVLink，PCIe 4.0 x16 带宽约 32GB/s 符合规格，Tensor Parallelism 对带宽敏感而 Pipeline Parallelism 对带宽不敏感但存在气泡，20-30% 的吞吐量损失在 PP=2 且 batch size 有限时符合工程经验量级。
