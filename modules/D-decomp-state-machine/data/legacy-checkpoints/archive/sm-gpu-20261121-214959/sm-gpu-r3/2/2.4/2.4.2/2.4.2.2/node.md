# N199: PCIe 5.0 vs PCIe 4.0 对多卡推理的影响量化：RTX 5090 (PCIe 5.0 x16) 单向带宽 128 GB/s，是 4090 (64

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

PCIe 5.0 vs PCIe 4.0 对多卡推理的影响量化：RTX 5090 (PCIe 5.0 x16) 单向带宽 128 GB/s，是 4090 (64 GB/s) 的 2 倍。若未来出现 2x 5090 方案，T_comm 进一步降低，但瓶颈仍可能在显存带宽 (1792 GB/s) 而非 PCIe。对于 27B 模型，PCIe 5.0 带来的理论吞吐提升约为 (128-64)/64 = 100% (仅通信部分)，但由于通信占比 <5%，整体吞吐提升 <5%。结论：PCIe 版本升级对 TP 推理边际收益极低，除非模型极大导致通信数据量激增。

## Corrected Claim

PCIe 5.0 vs PCIe 4.0 对多卡推理的影响量化：RTX 5090 (PCIe 5.0 x16) 单向带宽 128 GB/s，是 4090 (64 GB/s) 的 2 倍。若未来出现 2x 5090 方案，T_comm 进一步降低，但瓶颈仍可能在显存带宽 (1792 GB/s) 而非 PCIe。对于 27B 模型，PCIe 5.0 带来的理论吞吐提升约为 (128-64)/64 = 100% (仅通信部分)，但由于通信占比 <5%，整体吞吐提升 <5%。结论：PCIe 版本升级对 TP 推理边际收益极低，除非模型极大导致通信数据量激增。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 x16 单向带宽 128 GB/s 与 PCIe 4.0 的 64 GB/s 符合标准规范；RTX 5090 显存带宽 1792 GB/s 符合 GDDR7 规格；通信占比低导致整体吞吐提升有限的推导符合 Amdahl 定律及大模型推理通信瓶颈的一般规律。

## Search Query

pcie 5.0 vs 4.0 tensor parallelism inference throughput gain small model
