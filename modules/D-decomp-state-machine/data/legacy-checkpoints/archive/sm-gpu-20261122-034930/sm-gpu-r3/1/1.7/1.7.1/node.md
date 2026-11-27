# N64: Apple Silicon M2 Ultra 的统一内存带宽为 800 GB/s，而 M3 Ultra 提升至 819 GB/s；作为对比，RTX 4090 的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

Apple Silicon M2 Ultra 的统一内存带宽为 800 GB/s，而 M3 Ultra 提升至 819 GB/s；作为对比，RTX 4090 的 GDDR6X 带宽为 1008 GB/s，A100 80GB 的 HBM2e 带宽为 2039 GB/s。在 Memory-bound 的大模型推理中，理论吞吐量与带宽成正比，因此 M2/M3 Ultra 的理论峰值吞吐量低于 RTX 4090 约 20-25%，且远低于 A100。

## Corrected Claim

Apple Silicon M2 Ultra 的统一内存带宽为 800 GB/s，而 M3 Ultra 提升至 819 GB/s；作为对比，RTX 4090 的 GDDR6X 带宽为 1008 GB/s，A100 80GB 的 HBM2e 带宽为 2039 GB/s。在 Memory-bound 的大模型推理中，理论吞吐量与带宽成正比，因此 M2/M3 Ultra 的理论峰值吞吐量低于 RTX 4090 约 20-25%，且远低于 A100。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Apple M2 Ultra memory bandwidth GB/s vs NVIDIA RTX 4090 A100
