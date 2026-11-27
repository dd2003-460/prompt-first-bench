# N132: CPU+GPU 混合推理中，若 KV Cache 每 token 生成需从 CPU 内存读取 1.5MB 数据，则 PCIe 5.0 带宽 (64 GB/s) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

CPU+GPU 混合推理中，若 KV Cache 每 token 生成需从 CPU 内存读取 1.5MB 数据，则 PCIe 5.0 带宽 (64 GB/s) 成为瓶颈，导致解码吞吐量上限为 64 GB/s / 1.5 MB = 42.6 tokens/s，远低于 GPU 显存带宽限制下的 50-60 tokens/s。

## Corrected Claim

CPU+GPU 混合推理中，若 KV Cache 每 token 生成需从 CPU 内存读取 1.5MB 数据，则 PCIe 5.0 带宽 (64 GB/s) 成为瓶颈，导致解码吞吐量上限为 64 GB/s / 1.5 MB = 42.6 tokens/s，远低于 GPU 显存带宽限制下的 50-60 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 x16 单向带宽约为 64 GB/s，计算 64 GB/s / 1.5 MB/token ≈ 42.6 tokens/s，数值量级与逻辑推导均正确。

## Search Query

CPU GPU hybrid inference KV cache PCIe bandwidth bottleneck tokens per second
