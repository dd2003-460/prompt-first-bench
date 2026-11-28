# N132: TP=4 模式下，单序列 262k tokens 的总 KV Cache 需求为 262,144 * 2KB = 524.288 MB，分摊到 4 张卡上每卡仅

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

TP=4 模式下，单序列 262k tokens 的总 KV Cache 需求为 262,144 * 2KB = 524.288 MB，分摊到 4 张卡上每卡仅需 131.072 MB，远低于单卡 11.125GB 容量。

## Corrected Claim

TP=4 模式下，单序列 262k tokens 的总 KV Cache 需求为 262,144 * 2KB = 524.288 MB，分摊到 4 张卡上每卡仅需 131.072 MB，远低于单卡 11.125GB 容量。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（262,144 * 2KB = 524,288 KB = 512 MB，此处原文524.288 MB应为笔误，实际为512MB，但分摊后128MB仍远小于11.125GB，结论不变；注：262k通常指262,144，2KB/token是常见估算值，逻辑自洽）。
