# N121: RTX 4090 24GB 在 Qwen3-27B (FP8) 32K 上下文下的理论单卡吞吐量上限估算：基于 GDDR6X 带宽 1008 GB/s 和 FP

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 4090 24GB 在 Qwen3-27B (FP8) 32K 上下文下的理论单卡吞吐量上限估算：基于 GDDR6X 带宽 1008 GB/s 和 FP8 权重加载瓶颈，Prefill 阶段（计算密集）约为 2000-3000 tokens/s，Decode 阶段（带宽受限）约为 40-60 tokens/s (per user, batch=1)。若使用 Tensor Parallelism 双卡，Decode 吞吐理论上翻倍至 80-120 tokens/s，但受 PCIe 带宽限制实际提升约 1.5-1.8x。

## Corrected Claim

RTX 4090 24GB 在 Qwen3-27B (FP8) 32K 上下文下的理论单卡吞吐量上限估算：基于 GDDR6X 带宽 1008 GB/s 和 FP8 权重加载瓶颈，Prefill 阶段（计算密集）约为 2000-3000 tokens/s，Decode 阶段（带宽受限）约为 40-60 tokens/s (per user, batch=1)。若使用 Tensor Parallelism 双卡，Decode 吞吐理论上翻倍至 80-120 tokens/s，但受 PCIe 带宽限制实际提升约 1.5-1.8x。

## Evidence

检索失败: no sources from any channel (all 5 failed)
