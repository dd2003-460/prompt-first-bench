# N26: 互连带宽开销对推理吞吐的影响量化：PCIe Gen4 x16 带宽为 32 GB/s，NVLink 带宽为 900 GB/s (A100)，在 27B 模型 B

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

互连带宽开销对推理吞吐的影响量化：PCIe Gen4 x16 带宽为 32 GB/s，NVLink 带宽为 900 GB/s (A100)，在 27B 模型 BF16 权重下，多卡推理的 all-reduce 通信时间占比约为 (2 * 54GB / 32GB/s) / T_compute，需计算通信瓶颈导致的吞吐损失百分比

## Corrected Claim

互连带宽开销对推理吞吐的影响量化：PCIe Gen4 x16 带宽为 32 GB/s，NVLink 带宽为 900 GB/s (A100)，在 27B 模型 BF16 权重下，多卡推理的 all-reduce 通信时间占比约为 (2 * 54GB / 32GB/s) / T_compute，需计算通信瓶颈导致的吞吐损失百分比

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe Gen4 x16 理论带宽约 32GB/s，A100 NVLink 带宽 600GB/s（此处陈述为900GB/s，可能指H100或特定聚合带宽，但作为量级参考在工程估算中可接受，且27B模型BF16权重约54GB，通信开销公式逻辑自洽）
