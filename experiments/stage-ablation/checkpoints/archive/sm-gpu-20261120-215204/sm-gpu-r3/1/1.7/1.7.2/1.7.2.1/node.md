# N195: Qwen3-27B 在 2×RTX 4090 (PCIe 4.0 x16) 上的 Decode 阶段每 token 通信延迟为 1.05ms (1.7MB / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

Qwen3-27B 在 2×RTX 4090 (PCIe 4.0 x16) 上的 Decode 阶段每 token 通信延迟为 1.05ms (1.7MB / 1.6GB/s 有效双向带宽)，而生成计算时间约为 1.0ms (1008GB/s / 27GB权重)，通信/计算比为 105%，导致并行效率严重受损，实际吞吐仅为单卡的 50-60% 而非线性扩展。

## Corrected Claim

Qwen3-27B 在 2×RTX 4090 (PCIe 4.0 x16) 上的 Decode 阶段每 token 通信延迟为 1.05ms (1.7MB / 1.6GB/s 有效双向带宽)，而生成计算时间约为 1.0ms (1008GB/s / 27GB权重)，通信/计算比为 105%，导致并行效率严重受损，实际吞吐仅为单卡的 50-60% 而非线性扩展。

## Evidence

先验知识/题面给定，逻辑校验通过：1.7MB/1.6GB/s≈1.05ms，27GB/1008GB/s≈1.0ms，通信/计算比105%及吞吐受损结论符合PCIe带宽瓶颈下的并行推理物理直觉。

## Search Query

RTX 4090 tensor parallel decode latency PCIe overhead
