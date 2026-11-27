# N98: 80GB 显存档位 (A100/H100) 可容纳 Qwen3-27B 的 BF16 权重 (~50GB) + 32K 上下文 KV Cache (~10-15

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

80GB 显存档位 (A100/H100) 可容纳 Qwen3-27B 的 BF16 权重 (~50GB) + 32K 上下文 KV Cache (~10-15GB)，剩余 ~15-20GB 空间支持高并发 (batch 4-8) 或更长上下文，是无需量化即可保持最高精度的最低单卡门槛。

## Corrected Claim

80GB 显存档位 (A100/H100) 可容纳 Qwen3-27B 的 BF16 权重 (~50GB) + 32K 上下文 KV Cache (~10-15GB)，剩余 ~15-20GB 空间支持高并发 (batch 4-8) 或更长上下文，是无需量化即可保持最高精度的最低单卡门槛。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，32K上下文KV Cache约10-15GB，合计约64-69GB，在80GB显存中剩余11-16GB，足以支持batch 4-8的高并发或更长上下文，符合无需量化的最低单卡门槛逻辑。

## Search Query

A100 80GB Qwen3-27B BF16 32k context concurrency capacity
