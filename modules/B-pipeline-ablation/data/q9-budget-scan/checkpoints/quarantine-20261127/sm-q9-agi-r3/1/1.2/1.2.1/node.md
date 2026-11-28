# N39: FP8 KV Cache在TP=4下，单个token的跨卡总显存占用为 5KB/4 = 1.25 KB/token（假设KV头均分且无冗余复制）。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

FP8 KV Cache在TP=4下，单个token的跨卡总显存占用为 5KB/4 = 1.25 KB/token（假设KV头均分且无冗余复制）。

## Corrected Claim

FP8 KV Cache在TP=4下，单个token的跨卡总显存占用为 5KB/4 = 1.25 KB/token（假设KV头均分且无冗余复制）。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8精度下每字节1元素，5KB总占用除以4卡均分，计算结果为1.25KB，量纲与数值均合理。
