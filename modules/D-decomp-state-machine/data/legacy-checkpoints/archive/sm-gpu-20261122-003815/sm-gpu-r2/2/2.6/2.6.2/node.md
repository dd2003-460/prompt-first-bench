# N103: 2x RTX 4090 运行 BF16 Qwen3-27B 的不可行性确认：BF16 权重 54 GB > 总显存 48 GB。即使采用 Pipeline Pa

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

2x RTX 4090 运行 BF16 Qwen3-27B 的不可行性确认：BF16 权重 54 GB > 总显存 48 GB。即使采用 Pipeline Parallelism (PP=2)，每卡承载 27 GB 权重。加上 KV Cache (每卡至少 4.3 GB) 和激活/运行时 (2 GB)，每卡需求 ≈ 33.3 GB > 24 GB，不可行。结论：2x 4090 无法运行 BF16 32K 上下文。

## Corrected Claim

2x RTX 4090 运行 BF16 Qwen3-27B 的不可行性确认：BF16 权重 54 GB > 总显存 48 GB。即使采用 Pipeline Parallelism (PP=2)，每卡承载 27 GB 权重。加上 KV Cache (每卡至少 4.3 GB) 和激活/运行时 (2 GB)，每卡需求 ≈ 33.3 GB > 24 GB，不可行。结论：2x 4090 无法运行 BF16 32K 上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存为 24GB，2 卡共 48GB；Qwen3-27B BF16 权重约 54GB，超出总显存；即使 PP=2 分片，单卡权重 27GB 加上 KV Cache 和激活值远超 24GB 单卡上限，物理上不可行。
