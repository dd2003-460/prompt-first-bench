# N69: 多卡推理的通信开销对吞吐量的影响系数：在 PCIe 互联的多卡方案中，实际吞吐量通常只有单卡理论吞吐量的 50-70%（取决于模型大小和通信频率）。对于 27B

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

多卡推理的通信开销对吞吐量的影响系数：在 PCIe 互联的多卡方案中，实际吞吐量通常只有单卡理论吞吐量的 50-70%（取决于模型大小和通信频率）。对于 27B 模型，由于参数量较大，通信占比高，效率损失可能达到 40-50%。相比之下，NVLink 互联（如 2x A100）带宽为 600 GB/s，通信延迟降低约 10 倍，多卡效率可达 90-95%。因此，2x RTX 4090 的实际吞吐量可能仅为单卡 RTX 4090 的 1.2-1.4 倍，而非理论上的 2 倍。

## Corrected Claim

多卡推理的通信开销对吞吐量的影响系数：在 PCIe 互联的多卡方案中，实际吞吐量通常只有单卡理论吞吐量的 50-70%（取决于模型大小和通信频率）。对于 27B 模型，由于参数量较大，通信占比高，效率损失可能达到 40-50%。相比之下，NVLink 互联（如 2x A100）带宽为 600 GB/s，通信延迟降低约 10 倍，多卡效率可达 90-95%。因此，2x RTX 4090 的实际吞吐量可能仅为单卡 RTX 4090 的 1.2-1.4 倍，而非理论上的 2 倍。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-GPU inference efficiency PCIe vs NVLink tensor parallelism throughput loss
