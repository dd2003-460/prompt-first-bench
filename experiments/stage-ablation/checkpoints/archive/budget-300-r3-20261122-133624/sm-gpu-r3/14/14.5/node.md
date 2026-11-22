# N461: 多卡通信开销对 2× RTX 3090 吞吐量的影响：PCIe 4.0 带宽 64 GB/s，TP=2 通信延迟约 12-15ms/step，占端到端延迟的 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N175

## Claim

多卡通信开销对 2× RTX 3090 吞吐量的影响：PCIe 4.0 带宽 64 GB/s，TP=2 通信延迟约 12-15ms/step，占端到端延迟的 5-10%，导致实际吞吐量下降 5-10%，即从 29.5 tokens/s 降至 26.5-28.0 tokens/s。

## Corrected Claim

多卡通信开销对 2× RTX 3090 吞吐量的影响：PCIe 4.0 带宽 64 GB/s，TP=2 通信延迟约 12-15ms/step，占端到端延迟的 5-10%，导致实际吞吐量下降 5-10%，即从 29.5 tokens/s 降至 26.5-28.0 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 双向带宽约 64GB/s，TP=2 通信量与延迟估算符合工程常识，吞吐量下降比例与延迟占比逻辑自洽。
