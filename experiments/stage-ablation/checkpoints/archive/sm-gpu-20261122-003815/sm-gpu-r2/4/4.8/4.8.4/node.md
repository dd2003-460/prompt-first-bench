# N146: PCIe 5.0 互连带宽对多卡推理的影响：PCIe 5.0 x16 单向带宽为 64 GB/s (双向 128 GB/s)，相比 PCIe 4.0 翻倍。对于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

PCIe 5.0 互连带宽对多卡推理的影响：PCIe 5.0 x16 单向带宽为 64 GB/s (双向 128 GB/s)，相比 PCIe 4.0 翻倍。对于 2×RTX 5090 或 2×4090 方案，PCIe 5.0 可将 All-Reduce 延迟降低 50%，使多卡方案的 TCO 竞争力提升。

## Corrected Claim

PCIe 5.0 互连带宽对多卡推理的影响：PCIe 5.0 x16 单向带宽为 64 GB/s (双向 128 GB/s)，相比 PCIe 4.0 翻倍。对于 2×RTX 5090 或 2×4090 方案，PCIe 5.0 可将 All-Reduce 延迟降低 50%，使多卡方案的 TCO 竞争力提升。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 x16 单向带宽确为 64 GB/s（双向 128 GB/s），是 PCIe 4.0 的两倍；带宽翻倍在理想情况下可将通信延迟降低约 50%，逻辑自洽。

## Search Query

PCIe 5.0 bandwidth impact on multi-GPU LLM inference latency
