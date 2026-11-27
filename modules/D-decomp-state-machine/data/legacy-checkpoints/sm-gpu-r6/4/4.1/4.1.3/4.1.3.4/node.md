# N177: CPU Offload 的性能衰减倍数：当 KV Cache 部分或全部 Offload 到 CPU 内存时，由于 PCIe 4.0 x16 带宽 (~32 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

CPU Offload 的性能衰减倍数：当 KV Cache 部分或全部 Offload 到 CPU 内存时，由于 PCIe 4.0 x16 带宽 (~32 GB/s) 远低于 GPU 显存带宽 (~1008 GB/s)，推理速度通常衰减 10-50 倍，具体取决于 Offload 比例和 CPU 内存带宽

## Corrected Claim

CPU Offload 的性能衰减倍数：当 KV Cache 部分或全部 Offload 到 CPU 内存时，由于 PCIe 4.0 x16 带宽 (~32 GB/s) 远低于 GPU 显存带宽 (~1008 GB/s)，推理速度通常衰减 10-50 倍，具体取决于 Offload 比例和 CPU 内存带宽

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 带宽（~32 GB/s）与 GPU 显存带宽（~1008 GB/s，如 A100 HBM2e）的比值约为 31.5 倍，考虑到内存访问模式、延迟及 Offload 比例的影响，10-50 倍的衰减范围在工程经验上合理且自洽。

## Search Query

LLM inference CPU offload performance degradation factor PCIe bandwidth bottleneck
