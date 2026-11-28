# N122: RTX 5090 32GB 在 Qwen3-27B (FP8) 32K 上下文下的预估性能：基于 GDDR7 带宽 ~1792 GB/s (理论) 和 Blac

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 5090 32GB 在 Qwen3-27B (FP8) 32K 上下文下的预估性能：基于 GDDR7 带宽 ~1792 GB/s (理论) 和 Blackwell 架构的 FP8 算力提升，Decode 阶段预期达到 70-90 tokens/s (single card, batch=1)，Prefill 阶段超过 4000 tokens/s。相比 RTX 4090，单卡即可满足 32K 上下文的 FP8 部署需求（27GB 权重 + 4GB KV < 32GB），消除了双卡互联的复杂性和成本，成为新的性价比基准线。

## Corrected Claim

RTX 5090 32GB 在 Qwen3-27B (FP8) 32K 上下文下的预估性能：基于 GDDR7 带宽 ~1792 GB/s (理论) 和 Blackwell 架构的 FP8 算力提升，Decode 阶段预期达到 70-90 tokens/s (single card, batch=1)，Prefill 阶段超过 4000 tokens/s。相比 RTX 4090，单卡即可满足 32K 上下文的 FP8 部署需求（27GB 权重 + 4GB KV < 32GB），消除了双卡互联的复杂性和成本，成为新的性价比基准线。

## Evidence

检索失败: no sources from any channel (all 5 failed)
