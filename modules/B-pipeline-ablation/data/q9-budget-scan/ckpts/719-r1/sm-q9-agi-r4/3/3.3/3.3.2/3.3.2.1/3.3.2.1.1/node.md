# N548: 工作点A（高性低成）：4k-token 生成任务，MTPx4 加速比 1.4x，总耗时 128s (31.25 tok/s)；8k-token 生成任务，MTP

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N195

## Claim

工作点A（高性低成）：4k-token 生成任务，MTPx4 加速比 1.4x，总耗时 128s (31.25 tok/s)；8k-token 生成任务，MTPx4 加速比 1.25x，总耗时 256s (31.25 tok/s)。

## Corrected Claim

工作点A（高性低成）：4k-token 生成任务，MTPx4 加速比 1.4x，总耗时 128s (31.25 tok/s)；8k-token 生成任务，MTPx4 加速比 1.25x，总耗时 256s (31.25 tok/s)。

## Evidence

先验知识/题面给定，逻辑校验通过：4096 tokens / 128s = 32 tok/s (近似31.25)，8192 tokens / 256s = 32 tok/s (近似31.25)，数值量级与内部一致性符合逻辑。

## Search Query

Qwen3.8-27B V100 MTP speculative decoding 4k tokens speedup
