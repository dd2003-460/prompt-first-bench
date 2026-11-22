# N117: H100 80GB 在 BF16 下运行 Qwen3-27B 32K 上下文的理论解码吞吐量上限为 57.4 tokens/s (3.35TB/s HBM3 带

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

H100 80GB 在 BF16 下运行 Qwen3-27B 32K 上下文的理论解码吞吐量上限为 57.4 tokens/s (3.35TB/s HBM3 带宽 / 54GB 权重大小)，实际受限于计算瓶颈，预计实测值为 20-30 tokens/s。

## Corrected Claim

H100 80GB 在 BF16 下运行 Qwen3-27B 32K 上下文的理论解码吞吐量上限约为 62 tokens/s (3.35TB/s HBM3 带宽 / 54GB 权重大小)，实际受限于计算瓶颈及 KV Cache 开销，预计实测值为 20-30 tokens/s。

## Evidence

[质询]数值计算存在内部矛盾：H100 80GB 的 HBM3 带宽通常为 3.35 TB/s，但 Qwen3-27B 在 BF16 下的权重大小约为 54GB (27B * 2 bytes)。理论解码吞吐量上限 = 带宽 / 权重大小 = 3.35 TB/s / 54 GB ≈ 62.04 tokens/s，而非陈述中的 57.4 tokens/s。此外，32K 上下文的 KV Cache 会占用额外显存，进一步降低有效带宽或导致 OOM，但陈述未考虑 KV Cache 对带宽瓶颈的影响，仅用权重大小计算上限是不严谨的。 | 逻辑校验发现数值计算错误：3.35 TB/s / 54 GB ≈ 62 tokens/s，与陈述的 57.4 tokens/s 不符；且未考虑 KV Cache 占用对实际可用带宽/显存的影响。
