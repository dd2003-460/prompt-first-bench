# N724: FP8 精度下 A6000 48GB 的并发能力：剩余显存 = 48 - 31 = 17 GB，单请求 KV Cache = 4 GB，可支持 17 / 4 =

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N254

## Claim

FP8 精度下 A6000 48GB 的并发能力：剩余显存 = 48 - 31 = 17 GB，单请求 KV Cache = 4 GB，可支持 17 / 4 = 4.25，即最大 4 个并发请求（保留 1GB 系统余量后为 3 个）。

## Corrected Claim

FP8 精度下 A6000 48GB 的并发能力：剩余显存 = 48 - 31 = 17 GB，单请求 KV Cache = 4 GB，可支持 17 / 4 = 4.25，即最大 4 个并发请求（保留 1GB 系统余量后为 3 个）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 48-31=17, 17/4=4.25 正确，向下取整及余量扣除逻辑自洽。
