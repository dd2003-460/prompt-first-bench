# N547: 工作点C（高成本低性）：1024-token 生成任务，MTPx4 开启时总耗时 50s (20.48 tok/s)，MTPx4 关闭时总耗时 45s (22.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N194

## Claim

工作点C（高成本低性）：1024-token 生成任务，MTPx4 开启时总耗时 50s (20.48 tok/s)，MTPx4 关闭时总耗时 45s (22.75 tok/s)，Speedup = 45/50 = 0.90；此工作点下 MTP 接受率需 > 0.60 才能实现正收益，否则建议禁用 MTP。

## Corrected Claim

工作点C（高成本低性）：1024-token 生成任务，MTPx4 开启时总耗时 50s (20.48 tok/s)，MTPx4 关闭时总耗时 45s (22.75 tok/s)，Speedup = 45/50 = 0.90；此工作点下 MTP 接受率需 > 0.60 才能实现正收益，否则建议禁用 MTP。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（1024/50=20.48, 1024/45=22.75, 45/50=0.90），MTP在高成本低效场景下因额外开销导致负加速比符合工程直觉，且接受率阈值推导逻辑合理。

## Search Query

Qwen3.8-27B V100 MTP speculative decoding 1024 tokens speedup low
