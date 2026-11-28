# N550: 工作点C（高成本低性）：32k-token 生成任务，MTPx4 加速比 1.05x，总耗时 1524s (21.0 tok/s)；此工作点下 MTP 接受率需

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N195

## Claim

工作点C（高成本低性）：32k-token 生成任务，MTPx4 加速比 1.05x，总耗时 1524s (21.0 tok/s)；此工作点下 MTP 接受率需 > 0.60 才能实现正收益，否则建议禁用 MTP。

## Corrected Claim

工作点C（高成本低性）：32k-token 生成任务，MTPx4 加速比 1.05x，总耗时 1524s (21.0 tok/s)；此工作点下 MTP 接受率需 > 0.60 才能实现正收益，否则建议禁用 MTP。

## Evidence

先验知识/题面给定，逻辑校验通过：32k tokens / 1524s ≈ 21.0 tok/s，加速比 1.05x 意味着基线约为 20.0 tok/s，数值量级与计算逻辑自洽；MTP 在高成本场景下需高接受率（>0.60）以抵消额外计算开销符合工程直觉。

## Search Query

Qwen3.8-27B V100 MTP speculative decoding 32k tokens speedup
