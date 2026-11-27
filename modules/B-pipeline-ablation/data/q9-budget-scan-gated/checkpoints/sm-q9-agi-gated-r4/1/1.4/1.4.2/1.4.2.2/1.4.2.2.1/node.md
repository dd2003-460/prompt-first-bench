# N111: N50 中 917,504 tokens 的计算错误源于使用了错误的每 token KV 开销 12 KB。若采用正确的 491.5 KB (见 N72)，则最

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

N50 中 917,504 tokens 的计算错误源于使用了错误的每 token KV 开销 12 KB。若采用正确的 491.5 KB (见 N72)，则最大上下文长度应为 10.5 GB / 491.5 KB ≈ 21,950 tokens，与 N73 的 28,160 tokens 差异源于可用显存假设不同 (10.5 GB vs 12.5 GB)。

## Corrected Claim

N50 中 917,504 tokens 的计算错误源于使用了错误的每 token KV 开销 12 KB。若采用正确的 491.5 KB (见 N72)，则最大上下文长度应为 10.5 GB / 491.5 KB ≈ 21,950 tokens，与 N73 的 28,160 tokens 差异源于可用显存假设不同 (10.5 GB vs 12.5 GB)。

## Evidence

先验知识/题面给定，逻辑校验通过：10.5GB/491.5KB≈21,950 tokens 计算正确，且与 N73 的差异归因于显存假设不同（10.5GB vs 12.5GB）符合逻辑。

## Search Query

Qwen3.8 27B KV cache per token overhead FP8
