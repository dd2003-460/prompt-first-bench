# N25: Qwen3.8-27B 在 TP=4 模式下，draft model 的单卡有效显存占用约为 3.4 GB（13.5 GB 权重 / 4），剩余可用 KV 缓存

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

Qwen3.8-27B 在 TP=4 模式下，draft model 的单卡有效显存占用约为 3.4 GB（13.5 GB 权重 / 4），剩余可用 KV 缓存空间约为 11.8 GB（15.2 GB - 3.4 GB），支持长上下文下的并行草稿生成

## Corrected Claim

Qwen3.8-27B 在 TP=4 模式下，draft model 的单卡有效显存占用约为 3.4 GB（13.5 GB 权重 / 4），剩余可用 KV 缓存空间约为 11.8 GB（15.2 GB - 3.4 GB），支持长上下文下的并行草稿生成

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（13.5/4≈3.375≈3.4，15.2-3.4=11.8），符合TP分片显存计算逻辑。
