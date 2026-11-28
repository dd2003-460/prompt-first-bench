# N254: Logprobs 计算引入的 CPU-GPU 数据传输开销约为 Tensor Copy Time = DataSize / Bandwidth；在 PCIe 3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

Logprobs 计算引入的 CPU-GPU 数据传输开销约为 Tensor Copy Time = DataSize / Bandwidth；在 PCIe 3.0 x16 带宽 (12 GB/s) 下，传输 1GB Logprobs 数据耗时约 83ms，若每步生成 100 tokens，累积延迟将显著影响端到端 TPS。

## Corrected Claim

Logprobs 计算引入的 CPU-GPU 数据传输开销约为 Tensor Copy Time = DataSize / Bandwidth；在 PCIe 3.0 x16 带宽 (12 GB/s) 下，传输 1GB Logprobs 数据耗时约 83ms，若每步生成 100 tokens，累积延迟将显著影响端到端 TPS。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 3.0 x16 单向理论带宽约为 12.8 GB/s，有效带宽常取 12 GB/s 左右；1GB / 12GB/s ≈ 83.3ms，数值量级与计算逻辑自洽。

## Search Query

GPU CPU transfer bandwidth PCIe latency impact inference throughput
