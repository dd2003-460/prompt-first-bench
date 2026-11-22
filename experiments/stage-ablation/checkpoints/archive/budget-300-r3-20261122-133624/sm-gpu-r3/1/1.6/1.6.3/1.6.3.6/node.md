# N229: 多卡方案中 PCIe 互联带宽对 TP=2 推理延迟的影响量化：RTX 4090 (PCIe 4.0 x16, ~64 GB/s) 相比 NVLink (900

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

多卡方案中 PCIe 互联带宽对 TP=2 推理延迟的影响量化：RTX 4090 (PCIe 4.0 x16, ~64 GB/s) 相比 NVLink (900 GB/s) 在 Decode 阶段的通信开销增加约 10-15%，导致有效吞吐量下降 5-8%。

## Corrected Claim

多卡方案中，PCIe 4.0 x16互联带宽（~64 GB/s）相比NVLink（~900 GB/s）在TP=2推理Decode阶段会引入显著的通信开销，通常导致有效吞吐量出现可观测的下降（具体幅度取决于模型规模与实现优化，经验上可能在5%-15%区间）。

## Evidence

[质询]具体数值（10-15%延迟增加，5-8%吞吐下降）缺乏通用性，高度依赖模型架构（如Attention头数、FFN维度）、序列长度及具体实现优化（如通信重叠），将其作为固定量化指标存在过度泛化风险。 | 先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16带宽（~64GB/s）远低于NVLink（~900GB/s），在TP=2场景下通信瓶颈显著，导致性能下降符合物理直觉；但具体百分比为经验估算值，非绝对物理定律，故降级为定性/范围表述。
