# N13: 显存余量安全系数：为防止OOM（Out of Memory），实际分配显存需预留10-15%作为激活值（Activations）和临时缓冲。例如，若权重+KV需

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

显存余量安全系数：为防止OOM（Out of Memory），实际分配显存需预留10-15%作为激活值（Activations）和临时缓冲。例如，若权重+KV需40GB，则需选择48GB显存卡，而非32GB卡。此系数直接影响候选卡的最小显存规格选择。

## Corrected Claim

显存余量安全系数：为防止OOM（Out of Memory），实际分配显存需预留10-15%作为激活值（Activations）和临时缓冲。例如，若权重+KV需40GB，则需选择48GB显存卡，而非32GB卡。此系数直接影响候选卡的最小显存规格选择。

## Evidence

先验知识/题面给定，逻辑校验通过
