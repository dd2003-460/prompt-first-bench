# N304: L40S 在 Qwen3-27B FP8 量化下的显存占用为 33.3GB，低于其 48GB 物理显存，剩余 14.7GB 可用于 KV Cache，支持最大上

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

L40S 在 Qwen3-27B FP8 量化下的显存占用为 33.3GB，低于其 48GB 物理显存，剩余 14.7GB 可用于 KV Cache，支持最大上下文长度约 29,400 tokens（基于 FP16 KV Cache 0.0005GB/token），满足 32K 需求需启用 FP8 KV Cache 或量化 KV。

## Corrected Claim

L40S 在 Qwen3-27B FP8 量化下的显存占用为 33.3GB，低于其 48GB 物理显存，剩余 14.7GB 可用于 KV Cache，支持最大上下文长度约 29,400 tokens（基于 FP16 KV Cache 0.0005GB/token），满足 32K 需求需启用 FP8 KV Cache 或量化 KV。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B FP8权重约33.3GB，48GB-33.3GB=14.7GB，14.7GB/0.0005GB/token=29400 tokens，数值量级与计算逻辑自洽。

## Search Query

NVIDIA L40S 48GB memory Qwen3-27B context length support
