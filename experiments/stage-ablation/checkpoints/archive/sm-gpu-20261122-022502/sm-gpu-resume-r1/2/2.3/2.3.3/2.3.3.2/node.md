# N193: 4x RTX 4090 方案中，若采用 Pipeline Parallelism (PP=4) 而非 Tensor Parallelism，虽可避免每层 All

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

4x RTX 4090 方案中，若采用 Pipeline Parallelism (PP=4) 而非 Tensor Parallelism，虽可避免每层 All-Reduce，但存在气泡 (bubble) 问题：在 batch_size=1 时，流水线填充/排空导致的空闲时间占比高达 75% (3/4 层空闲)，实际有效吞吐仅为理论峰值的 25%，即约 4.0 tokens/s，远低于 TP 方案的 16.1 tokens/s，因此 TP 是更优策略但受限于 PCIe 带宽。

## Corrected Claim

4x RTX 4090 方案中，若采用 Pipeline Parallelism (PP=4) 而非 Tensor Parallelism，虽可避免每层 All-Reduce，但存在气泡 (bubble) 问题：在 batch_size=1 时，流水线填充/排空导致的空闲时间占比高达 75% (3/4 层空闲)，实际有效吞吐仅为理论峰值的 25%，即约 4.0 tokens/s，远低于 TP 方案的 16.1 tokens/s，因此 TP 是更优策略但受限于 PCIe 带宽。

## Evidence

先验知识/题面给定，逻辑校验通过：PP=4且batch_size=1时，流水线气泡占比为(p-1)/p=75%，有效吞吐为理论峰值的25%，计算自洽。

## Search Query

pipeline parallelism bubble overhead batch size 1 LLM inference efficiency
